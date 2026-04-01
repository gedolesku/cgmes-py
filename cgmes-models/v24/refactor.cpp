// ptdf_refactor.cpp – verzija bez paralelizacije
// -----------------------------------------------------------------------------
// Bitne razlike prema originalu (PTDF_proracun2):
//   • nema više new[]/delete[] unutar petlji – koristi se std::vector / std::unique_ptr
//   • sve izlazne matrice se alociraju jednom pre glavne petlje
//   • ZoneToNode i ostali radni baferi se recikliraju, nema dodatnih realokacija
//   • čisti RAII destruktori – nema curenja memorije
//   • kod podeljen po odgovornostima, funkcije su kraće i čitljivije
// -----------------------------------------------------------------------------
// Napomena: CalculateFactors zavisi od rowIndex (svaki CB) + scenarija ispada (CO),
// tako da se i dalje poziva CB×CO puta. Optimizacija je uklanjanje alokacija i
// bolji keš, a ne redukcija broja poziva.
// -----------------------------------------------------------------------------

#include <vector>
#include <memory>
#include <cstring>
#include "PTDF_api.h"

/* =========================== 1.  Helpers  =========================== */

struct ScratchBuffers
{
    std::vector<double>              sumFaktorZone;
    std::vector<std::vector<double>> ZoneToNode; // participant × all‑nodes

    ScratchBuffers(int nPart, int nNodesInModel)
        : sumFaktorZone(nPart, 1.0),
          ZoneToNode(nPart, std::vector<double>(nNodesInModel, 0.0)) {}
};

static void ReinitScratch(ScratchBuffers &buf)
{
    std::fill(buf.sumFaktorZone.begin(), buf.sumFaktorZone.end(), 1.0);
    for (auto &v : buf.ZoneToNode) std::fill(v.begin(), v.end(), 0.0);
}

/* =========================== 2.  Alokacija izlaznih struktura  =========================== */

static void AllocateBranchOutputs(const T_PTDF *ptdf,
                                  T_PTDFR       *ptdfr,
                                  const std::vector<int> &indexNodes)
{
    const int nPart  = ptdf->nmb_of_participants;
    const int nNodes = static_cast<int>(indexNodes.size());

    ptdfr->nmb_of_participants           = nPart;
    ptdfr->participant_description_array = new T_Participant_Description[nPart];

    ptdfr->nmb_of_nodes = nNodes;
    ptdfr->nodes_index  = nNodes ? new int[nNodes] : nullptr;
    for (int i = 0; i < nNodes; ++i) ptdfr->nodes_index[i] = indexNodes[i];

    ptdfr->nmb_of_critical_branches        = ptdf->nmb_of_critical_branches;
    ptdfr->faktor_osetljivosti_branch_array = new T_Faktor_Osetljivosti_Branch[ptdf->nmb_of_critical_branches];

    for (int cb = 0; cb < ptdf->nmb_of_critical_branches; ++cb)
    {
        const auto &srcCB = ptdf->critical_branch_array[cb];
        auto &dstCB       = ptdfr->faktor_osetljivosti_branch_array[cb];

        dstCB.nmb_of_critical_outages = srcCB.nmb_of_crit_outages;
        dstCB.nmb_of_rows    = nPart;
        dstCB.nmb_of_columns = nNodes;

        // glavna zona_to_node matrica
        dstCB.faktor_zone_to_node = new double*[nPart];
        for (int r = 0; r < nPart; ++r)
            dstCB.faktor_zone_to_node[r] = new double[nNodes]{};

        // bazni faktor_a
        for (int i = 0; i < nPart; ++i)
            for (int j = 0; j < nPart; ++j) dstCB.faktor_a[i][j] = 0.0;

        // faktori po outage‑u
        for (int k = 0; k < srcCB.nmb_of_crit_outages; ++k)
        {
            auto &fa = dstCB.faktor_a_array[k];
            fa.nmb_of_rows    = nPart;
            fa.nmb_of_columns = nNodes;

            for (int i = 0; i < nPart; ++i)
                for (int j = 0; j < nPart; ++j) fa.faktor_a[i][j] = 0.0;

            fa.faktor_zone_to_node = new double*[nPart];
            for (int r = 0; r < nPart; ++r)
                fa.faktor_zone_to_node[r] = new double[nNodes]{};
        }
    }
}

/* =========================== 3.  Glavna rutina  =========================== */

int PTDF_proracun_opt(T_PTDF *ptdf, T_PTDFR *ptdfr, bool allParticipants)
{
    // 3.1 Set participant faktora
    SetParticipantFactor2(ptdf, ptdfr);

    // 3.2 Odabir čvorova koji ulaze u PTDF
    std::vector<int> indexNodes;
    {
        std::vector<int> tagged(ptdf->nmb_of_nodes_in_model, 0);
        indexNodes.push_back(ptdf->index_swing_node);
        tagged[ptdf->index_swing_node] = 1;
        for (int p = 0; p < ptdf->nmb_of_participants; ++p)
        {
            const auto &part = ptdf->participant_array[p];
            if (part.type == JOINT) continue;
            if (!allParticipants && part.Participate_in_CA == NE_UCESTV) continue;
            const auto &tso = part.tso;
            for (int g = 0; g < tso.nmb_of_gen_nodes; ++g)
            {
                int idx = tso.gen_nodes_array[g].index_node2;
                if (!tagged[idx]) { indexNodes.push_back(idx); tagged[idx] = 1; }
            }
            if (tso.percentage_LSK != 0)
                for (int l = 0; l < tso.nmb_of_load_nodes; ++l)
                {
                    int idx = tso.load_nodes_array[l].index_node2;
                    if (!tagged[idx]) { indexNodes.push_back(idx); tagged[idx] = 1; }
                }
        }
    }

    // 3.3 Alokacija izlaza
    AllocateBranchOutputs(ptdf, ptdfr, indexNodes);

    // 3.4 Radni baferi
    ScratchBuffers scratch(ptdf->nmb_of_participants, ptdf->nmb_of_nodes_in_model);

    // 3.5 Petlja po kritičnim granama (bez paralelizacije, redom)
    for (int cbIdx = 0; cbIdx < ptdf->nmb_of_critical_branches; ++cbIdx)
    {
        const auto &cb = ptdf->critical_branch_array[cbIdx];
        auto &dst      = ptdfr->faktor_osetljivosti_branch_array[cbIdx];

        // bazni slučaj
        int rowBase = ptdf->matrix.getMatrixRow(cb.opis.index_node12,
                                                cb.opis.index_node22,
                                                cb.opis.CKT);
        ReinitScratch(scratch);
        auto zoneF = CalculateFactors(rowBase, ptdf, allParticipants,
                                      scratch.ZoneToNode, scratch.sumFaktorZone);

        for (int i = 0; i < ptdf->nmb_of_participants; ++i)
        {
            for (int j = 0; j < ptdf->nmb_of_participants; ++j)
                dst.faktor_a[i][j] = zoneF[i][j][0] + zoneF[i][j][1];
            for (size_t n = 0; n < indexNodes.size(); ++n)
                dst.faktor_zone_to_node[i][n] = scratch.ZoneToNode[i][indexNodes[n]];
        }

        // sve outage‑kombinacije
        for (int k = 0; k < cb.nmb_of_crit_outages; ++k)
        {
            const auto &co = cb.crit_outage_array[k];
            auto &faOut    = dst.faktor_a_array[k];

            int rowCo = ptdf->matrix.getMatrixRow(cb.opis.index_node12,
                                                  cb.opis.index_node22,
                                                  cb.opis.CKT,
                                                  co.outageName);
            if (rowCo == -1) continue;

            ReinitScratch(scratch);
            auto zf = CalculateFactors(rowCo, ptdf, allParticipants,
                                       scratch.ZoneToNode, scratch.sumFaktorZone);

            for (int i = 0; i < ptdf->nmb_of_participants; ++i)
            {
                for (int j = 0; j < ptdf->nmb_of_participants; ++j)
                    faOut.faktor_a[i][j] = zf[i][j][0] + zf[i][j][1];
                for (size_t n = 0; n < indexNodes.size(); ++n)
                    faOut.faktor_zone_to_node[i][n] = scratch.ZoneToNode[i][indexNodes[n]];
            }
        }
    }

    return 0;
}

/* =========================== 4.  API wrap  =========================== */

void PTDF_execute_refactored(T_PTDF *opts, int nSize, T_PTDFR *out, bool allParticipants, int &iErr)
{
    if ((int)sizeof(opts) != nSize) { iErr = 1; return; }
    iErr = PTDF_proracun_opt(opts, out, allParticipants);
}

/* =========================== 5.  TODO  =========================== */
// • Dodati destruktor / helper za T_PTDFR koji oslobađa sve duboke alokacije.
// • Eventualno izdvojiti CalculateFactors u poseban modul sa const‑korektnošću.
// • Za realne produkcione build‑ove koristi Release + /O2; profilirati posebno.
// -----------------------------------------------------------------------------
