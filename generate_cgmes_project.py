# c:\git-code\tna\python-cgmes\generate_dataclasses.py

import os
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Optional, Protocol

OUTPUT_DIR = Path("c:/git-code/tna/python-cgmes/models")

namespaces = {
    "xmi": "http://schema.omg.org/spec/XMI/2.1",
    "uml": "http://www.omg.org/spec/UML/20090901"
}


def parse_xmi_to_classes(xml_file: str):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    # Store class metadata, keyed by XMI ID
    xmi_classes = {}
    # Store known primitives
    primitive_map = {
        "Integer": "int",
        "Boolean": "bool",
        "Float": "float",
        "String": "str"
    }

    # Pass 1: Gather all classes
    for elem in root.findall(".//packagedElement[@xmi:type='uml:Class']", namespaces=namespaces):
        class_id = elem.get("xmi:id")
        name = elem.get("name", "UnnamedClass")
        is_abstract = (elem.get("isAbstract") == "true")
        xmi_classes[class_id] = {
            "name": name,
            "isAbstract": is_abstract,
            "attributes": [],
            "parent": None  # we'll fill in from generalization
        }

    # Pass 2: Gather attributes, parse type references
    for elem in root.findall(".//packagedElement[@xmi:type='uml:Class']", namespaces=namespaces):
        class_id = elem.get("xmi:id")
        # <ownedAttribute xmi:type="uml:Property" ...>
        for prop in elem.findall(".//ownedAttribute[@xmi:type='uml:Property']", namespaces=namespaces):
            attr_name = prop.get("name", "UnnamedProperty")
            type_ref = prop.find(".//type", namespaces=namespaces)
            attr_type = "str"
            if type_ref is not None:
                ref_id = type_ref.get("xmi:idref")
                # Check if this points to another class or a primitive
                if ref_id in xmi_classes:
                    # It's another class
                    attr_type = xmi_classes[ref_id]["name"]
                else:
                    # Might be a primitive definition
                    # search for it
                    p_elem = root.find(f".//*[@xmi:id='{ref_id}']", namespaces=namespaces)
                    if p_elem is not None:
                        p_name = p_elem.get("name", "String")
                        attr_type = primitive_map.get(p_name, p_name)
            xmi_classes[class_id]["attributes"].append((attr_name, attr_type))

        # <generalization xmi:type="uml:Generalization" general="someID">
        for gen in elem.findall(".//generalization[@xmi:type='uml:Generalization']", namespaces=namespaces):
            parent_id = gen.get("general")
            if parent_id and parent_id in xmi_classes:
                xmi_classes[class_id]["parent"] = parent_id

    return xmi_classes


def generate_dataclass_code(xmi_classes):
    """Return a dict {className: codeString} for each UML class."""
    # Step 3: Build Python code with possible inheritance
    code_by_class = {}
    for class_id, info in xmi_classes.items():
        class_name = info["name"]
        parent_id = info["parent"]
        parent_name = None
        if parent_id:
            parent_name = xmi_classes[parent_id]["name"]

        lines = []
        # If isAbstract => Protocol, else => dataclass
        if info["isAbstract"]:
            if parent_name:
                # Inherit from parent's name + Protocol if parent is also abstract
                if xmi_classes[parent_id]["isAbstract"]:
                    lines.append(f"class {class_name}({parent_name}, Protocol):")
                else:
                    lines.append(f"class {class_name}({parent_name}, Protocol):")
            else:
                lines.append(f"class {class_name}(Protocol):")
        else:
            # Non-abstract => dataclass
            if parent_name:
                if xmi_classes[parent_id]["isAbstract"]:
                    # Parent is a protocol, so just normal dataclass with parent
                    lines.append(f"@dataclass\nclass {class_name}({parent_name}):")
                else:
                    lines.append(f"@dataclass\nclass {class_name}({parent_name}):")
            else:
                lines.append(f"@dataclass\nclass {class_name}:")
        # Build attributes
        if not info["attributes"]:
            lines.append(f"    pass")
        else:
            for attr, atype in info["attributes"]:
                lines.append(f"    {attr}: {atype} = None")

        code_by_class[class_name] = "\n".join(lines)
    return code_by_class


def write_classes_to_files(classes_data):
    codes = generate_dataclass_code(classes_data)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    for cls_name, code_str in codes.items():
        file_path = OUTPUT_DIR / f"{cls_name.lower()}.py"
        with open(file_path, "w") as f:
            f.write("from dataclasses import dataclass\n")
            f.write("from typing import Optional, Protocol\n\n")
            f.write(code_str)


def main():
    xml_file = r"cgmes-models\v24\ENTSOE_CGMES_v2.4.14_28May2014.xml"
    classes_data = parse_xmi_to_classes(xml_file)
    if not classes_data:
        print("No UML classes found; check XMI content/namespace.")
    else:
        write_classes_to_files(classes_data)


if __name__ == "__main__":
    main()