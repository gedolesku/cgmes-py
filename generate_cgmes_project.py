# c:\git-code\tna\python-cgmes\generate_cgmes_project.py

import os
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Optional, Dict, List, Tuple
from dataclasses import dataclass

OUTPUT_DIR = Path("c:/git-code/tna/python-cgmes/generated")

namespaces = {
    "xmi": "http://schema.omg.org/spec/XMI/2.1",
    "uml": "http://www.omg.org/spec/UML/20090901"
}

@dataclass
class AttributeInfo:
    name: str
    type_name: str
    multiplicity: str = "1"
    is_optional: bool = False

@dataclass 
class ClassInfo:
    name: str
    package_path: str
    is_abstract: bool = False
    parent_class: Optional[str] = None
    attributes: List[AttributeInfo] = None
    
    def __post_init__(self):
        if self.attributes is None:
            self.attributes = []

def parse_xmi_to_classes(xml_file: str) -> Dict[str, ClassInfo]:
    """Parse the XMI file and extract complete class information"""
    tree = ET.parse(xml_file)
    root = tree.getroot()
    
    # Maps for lookups
    class_by_id = {}  # xmi:id -> ClassInfo
    package_by_id = {}  # xmi:id -> package path
    type_by_id = {}  # xmi:id -> type name (for primitives and classes)
    
    # First pass: collect all packages
    def build_package_tree(element, current_path=""):
        for pkg in element.findall(".//packagedElement[@xmi:type='uml:Package']", namespaces):
            pkg_id = pkg.get("{http://schema.omg.org/spec/XMI/2.1}id")
            pkg_name = pkg.get("name", "Unknown")
            full_path = f"{current_path}.{pkg_name}" if current_path else pkg_name
            package_by_id[pkg_id] = full_path
            build_package_tree(pkg, full_path)
    
    build_package_tree(root)
    
    # Second pass: collect all classes and their packages
    for pkg_elem in root.findall(".//packagedElement[@xmi:type='uml:Package']", namespaces):
        pkg_id = pkg_elem.get("{http://schema.omg.org/spec/XMI/2.1}id")
        pkg_path = package_by_id.get(pkg_id, "")
        
        for class_elem in pkg_elem.findall(".//packagedElement[@xmi:type='uml:Class']", namespaces):
            class_id = class_elem.get("{http://schema.omg.org/spec/XMI/2.1}id")
            class_name = class_elem.get("name", "UnknownClass")
            is_abstract = class_elem.get("isAbstract") == "true"
            
            class_info = ClassInfo(
                name=class_name,
                package_path=pkg_path,
                is_abstract=is_abstract
            )
            
            class_by_id[class_id] = class_info
            type_by_id[class_id] = class_name
    
    # Also collect primitive types
    primitive_map = {
        "String": "str",
        "Integer": "int", 
        "Boolean": "bool",
        "Float": "float",
        "DateTime": "datetime",
        "Date": "str"
    }
    
    for prim_elem in root.findall(".//packagedElement[@xmi:type='uml:Class']", namespaces):
        prim_id = prim_elem.get("{http://schema.omg.org/spec/XMI/2.1}id")
        prim_name = prim_elem.get("name", "")
        if prim_name in primitive_map:
            type_by_id[prim_id] = primitive_map[prim_name]
    
    # Third pass: handle inheritance
    for class_elem in root.findall(".//packagedElement[@xmi:type='uml:Class']", namespaces):
        class_id = class_elem.get("{http://schema.omg.org/spec/XMI/2.1}id")
        if class_id not in class_by_id:
            continue
            
        # Find generalization
        for gen in class_elem.findall(".//generalization[@xmi:type='uml:Generalization']", namespaces):
            parent_id = gen.get("general")
            if parent_id and parent_id in class_by_id:
                class_by_id[class_id].parent_class = class_by_id[parent_id].name
    
    # Fourth pass: collect attributes with proper typing and multiplicity
    for class_elem in root.findall(".//packagedElement[@xmi:type='uml:Class']", namespaces):
        class_id = class_elem.get("{http://schema.omg.org/spec/XMI/2.1}id")
        if class_id not in class_by_id:
            continue
            
        class_info = class_by_id[class_id]
        
        for attr in class_elem.findall(".//ownedAttribute[@xmi:type='uml:Property']", namespaces):
            attr_name = attr.get("name", "unknown")
            
            # Get type
            type_elem = attr.find(".//type", namespaces)
            attr_type = "str"  # default
            if type_elem is not None:
                type_ref = type_elem.get("{http://schema.omg.org/spec/XMI/2.1}idref")
                if type_ref and type_ref in type_by_id:
                    attr_type = type_by_id[type_ref]
            
            # Get multiplicity
            lower_val = attr.find(".//lowerValue", namespaces)
            upper_val = attr.find(".//upperValue", namespaces)
            
            is_optional = False
            multiplicity = "1"
            
            if lower_val is not None and upper_val is not None:
                lower = lower_val.get("value", "1")
                upper = upper_val.get("value", "1")
                
                if lower == "0":
                    is_optional = True
                if upper == "*" or upper == "-1":
                    multiplicity = "*"
                    attr_type = f"List[{attr_type}]"
                elif upper != "1":
                    multiplicity = f"{lower}..{upper}"
            
            attr_info = AttributeInfo(
                name=attr_name,
                type_name=attr_type,
                multiplicity=multiplicity,
                is_optional=is_optional
            )
            
            class_info.attributes.append(attr_info)
    
    return class_by_id

def create_package_structure(classes: Dict[str, ClassInfo]) -> None:
    """Create directory structure and __init__.py files"""
    packages = set()
    
    for class_info in classes.values():
        if class_info.package_path:
            parts = class_info.package_path.split('.')
            for i in range(len(parts)):
                pkg_path = '.'.join(parts[:i+1])
                packages.add(pkg_path)
    
    # Create directories and __init__.py files
    for package in packages:
        dir_path = OUTPUT_DIR / package.replace('.', '/')
        dir_path.mkdir(parents=True, exist_ok=True)
        
        init_file = dir_path / "__init__.py"
        if not init_file.exists():
            with open(init_file, 'w') as f:
                f.write(f'"""Package: {package}"""\n')

def generate_class_code(class_info: ClassInfo, all_classes: Dict[str, ClassInfo]) -> str:
    """Generate Python code for a single class"""
    lines = []
    
    # Imports
    imports = set()
    if any("List[" in attr.type_name for attr in class_info.attributes):
        imports.add("from typing import List, Optional, Protocol")
    else:
        imports.add("from typing import Optional, Protocol")
    
    if not class_info.is_abstract:
        imports.add("from dataclasses import dataclass")
    
    # Add imports for referenced classes
    for attr in class_info.attributes:
        attr_type = attr.type_name
        if "List[" in attr_type:
            attr_type = attr_type.replace("List[", "").replace("]", "")
        
        # Check if this is a class we know about
        for other_class in all_classes.values():
            if other_class.name == attr_type and other_class.package_path != class_info.package_path:
                import_path = other_class.package_path.replace('.', '.')
                imports.add(f"from {import_path} import {attr_type}")
    
    # Write imports
    for imp in sorted(imports):
        lines.append(imp)
    lines.append("")
    
    # Class definition
    class_def = ""
    if not class_info.is_abstract:
        class_def += "@dataclass\n"
    
    if class_info.parent_class:
        if class_info.is_abstract:
            class_def += f"class {class_info.name}({class_info.parent_class}, Protocol):"
        else:
            class_def += f"class {class_info.name}({class_info.parent_class}):"
    else:
        if class_info.is_abstract:
            class_def += f"class {class_info.name}(Protocol):"
        else:
            class_def += f"class {class_info.name}:"
    
    lines.append(class_def)
    
    # Add docstring
    lines.append(f'    """CGMES class: {class_info.name}"""')
    
    # Attributes
    if not class_info.attributes:
        lines.append("    pass")
    else:
        for attr in class_info.attributes:
            if attr.is_optional:
                lines.append(f"    {attr.name}: Optional[{attr.type_name}] = None")
            else:
                if "List[" in attr.type_name:
                    lines.append(f"    {attr.name}: {attr.type_name} = None")
                else:
                    lines.append(f"    {attr.name}: {attr.type_name}")
    
    return "\n".join(lines)

def write_classes_to_files(classes: Dict[str, ClassInfo]) -> None:
    """Write all classes to their respective files in package structure"""
    create_package_structure(classes)
    
    for class_info in classes.values():
        # Determine file path
        if class_info.package_path:
            file_dir = OUTPUT_DIR / class_info.package_path.replace('.', '/')
        else:
            file_dir = OUTPUT_DIR
        
        file_path = file_dir / f"{class_info.name.lower()}.py"
        
        # Generate and write code
        code = generate_class_code(class_info, classes)
        
        with open(file_path, 'w') as f:
            f.write(code)
        
        print(f"Generated: {file_path}")

def main():
    xml_file = r"cgmes-models\v24\ENTSOE_CGMES_v2.4.14_28May2014.xml"
    
    if not os.path.exists(xml_file):
        print(f"XML file not found: {xml_file}")
        return
    
    print("Parsing XMI file...")
    classes = parse_xmi_to_classes(xml_file)
    
    if not classes:
        print("No classes found in XMI file")
        return
    
    print(f"Found {len(classes)} classes")
    
    print("Generating Python files...")
    write_classes_to_files(classes)
    
    print("Done!")

if __name__ == "__main__":
    main()