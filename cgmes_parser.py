import xml.etree.ElementTree as ET

class CGMESParser:
    def __init__(self):
        self.entities = {}

    def parse_file(self, file_path: str):
        tree = ET.parse(file_path)
        root = tree.getroot()
        for substation in root.findall('.//{http://iec.ch/TC57/2013/CIM-schema-cim16#}Substation'):
            rdf_id = substation.get('{http://www.w3.org/1999/02/22-rdf-syntax-ns#}ID')
            name_element = substation.find('.//{http://iec.ch/TC57/2013/CIM-schema-cim16#}IdentifiedObject.name')
            self.entities[rdf_id] = {
                'type': 'Substation',
                'name': name_element.text if name_element is not None else None,
            }
        return self.entities