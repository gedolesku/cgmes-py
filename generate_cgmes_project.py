# c:\git-code\tna\python-cgmes\generate_dataclasses.py

import os
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Optional

OUTPUT_DIR = Path("c:/git-code/tna/python-cgmes/models")

namespaces = {
    "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "cim": "http://iec.ch/TC57/CIM100#",
    "md": "http://iec.ch/TC57/61970-552/ModelDescription/1#"
}


def parse_xml_to_classes(xml_file: str):
    """Parse the XML file and extract class definitions."""
    tree = ET.parse(xml_file)
    root = tree.getroot()

    classes = {}
    for description in root.findall(".//rdf:Description", namespaces=namespaces):
        class_name = description.find("rdfs:label", namespaces=namespaces).text
        attributes = []

        for attribute in description.findall("cims:datatype", namespaces=namespaces):
            attr_name = attribute.get("name")
            attr_type = attribute.get("type")
            attributes.append((attr_name, attr_type))

        classes[class_name] = attributes

    return classes


def generate_dataclass_code(class_name: str, attributes: list):
    """Generate Python dataclass code for a given class."""
    lines = [f"@dataclass", f"class {class_name}:"]
    for attr_name, attr_type in attributes:
        lines.append(f"    {attr_name}: {attr_type}")
    return "\n".join(lines)


def write_classes_to_files(classes: dict):
    """Write each class to a separate Python file."""
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    for class_name, attributes in classes.items():
        file_path = OUTPUT_DIR / f"{class_name.lower()}.py"
        with open(file_path, "w") as f:
            f.write("from dataclasses import dataclass\n")
            f.write("from typing import Optional\n\n")
            f.write(generate_dataclass_code(class_name, attributes))


def main():
    xml_file = r"cgmes-models\v24\ENTSOE_CGMES_v2.4.14_28May2014.xml"
    classes = parse_xml_to_classes(xml_file)
    write_classes_to_files(classes)


if __name__ == "__main__":
    main()