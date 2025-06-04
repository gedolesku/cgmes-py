# c:\git-code\tna\python-cgmes\generate_cgmes_project.py

import os
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Optional, Dict, List, Tuple
from dataclasses import dataclass, field

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
    documentation: Optional[str] = None

@dataclass
class LinkInfo:
    link_type: str  # Association, Generalization, Dependency, etc.
    target_id: str
    target_name: Optional[str] = None
    multiplicity: str = "1"
    is_optional: bool = False

@dataclass 
class ClassInfo:
    name: str
    package_path: str
    is_abstract: bool = False
    parent_class: Optional[str] = None
    attributes: List[AttributeInfo] = None
    links: List[LinkInfo] = None  # Add links field
    xml_id: Optional[str] = None
    package_id: Optional[str] = None
    documentation: Optional[str] = None
    
    def __post_init__(self):
        if self.attributes is None:
            self.attributes = []
        if self.links is None:
            self.links = []

def parse_xmi_to_classes(xml_file: str) -> Dict[str, ClassInfo]:
    """Parse the XMI file and extract complete class information"""
    tree = ET.parse(xml_file)
    root = tree.getroot()
    
    # Maps for lookups
    class_by_id = {}  # xmi:id -> ClassInfo
    package_by_id = {}  # xmi:id -> package path
    type_by_id = {}  # xmi:id -> type name (for primitives and classes)
    element_docs = {}  # xmi:id -> documentation from element sections
    attribute_docs = {}  # attribute xmi:id -> documentation
    element_links = {}  # element xmi:id -> list of LinkInfo
    
    # Extract documentation and links from element sections
    for element in root.findall(".//element[@xmi:type='uml:Class']", namespaces):
        element_id = element.get("{http://schema.omg.org/spec/XMI/2.1}idref")
        if element_id:
            # Get class documentation
            props = element.find("properties")
            if props is not None:
                doc = props.get("documentation")
                if doc:
                    element_docs[element_id] = doc
            
            # Get attribute documentation
            for attr in element.findall(".//attribute"):
                attr_id = attr.get("{http://schema.omg.org/spec/XMI/2.1}idref")
                if attr_id:
                    doc_elem = attr.find("documentation")
                    if doc_elem is not None:
                        doc_value = doc_elem.get("value")
                        if doc_value:
                            attribute_docs[attr_id] = doc_value
            
            # Extract links
            links_section = element.find("links")
            if links_section is not None:
                element_links[element_id] = []
                
                # Parse different types of links
                for association in links_section.findall("Association"):
                    start_id = association.get("start")
                    end_id = association.get("end")
                    
                    # For associations, we need to determine the relationship
                    # If this class is the start, then end is the target
                    # If this class is the end, then start is the target
                    target_id = None
                    if start_id == element_id and end_id:
                        target_id = end_id
                    elif end_id == element_id and start_id:
                        target_id = start_id
                    
                    if target_id:
                        element_links[element_id].append(LinkInfo(
                            link_type="Association",
                            target_id=target_id
                        ))
                
                for generalization in links_section.findall("Generalization"):
                    start_id = generalization.get("start")
                    end_id = generalization.get("end")
                    
                    # For generalization, if this class is the start, then end is the parent
                    if start_id == element_id and end_id:
                        element_links[element_id].append(LinkInfo(
                            link_type="Generalization",
                            target_id=end_id
                        ))
                
                for dependency in links_section.findall("Dependency"):
                    start_id = dependency.get("start")
                    end_id = dependency.get("end")
                    
                    # For dependencies, if this class is the start, then end is the target
                    if start_id == element_id and end_id:
                        element_links[element_id].append(LinkInfo(
                            link_type="Dependency",
                            target_id=end_id
                        ))
    
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
            
            # Get class documentation from element section
            class_doc = element_docs.get(class_id)
            
            # Get links from element section
            class_links = element_links.get(class_id, [])
            
            class_info = ClassInfo(
                name=class_name,
                package_path=pkg_path,
                is_abstract=is_abstract,
                xml_id=class_id,
                package_id=pkg_id,
                documentation=class_doc,
                links=class_links
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
    
    # Resolve link target names and handle inheritance from links
    for class_info in class_by_id.values():
        for link in class_info.links:
            if link.target_id in class_by_id:
                target_class = class_by_id[link.target_id]
                link.target_name = target_class.name
                
                # Handle generalization links as inheritance
                if link.link_type == "Generalization":
                    class_info.parent_class = target_class.name
            else:
                # If target is not a class, it might be a primitive or external reference
                # For now, we'll skip these associations
                continue
    
    # Third pass: handle inheritance from UML structure (fallback)
    for class_elem in root.findall(".//packagedElement[@xmi:type='uml:Class']", namespaces):
        class_id = class_elem.get("{http://schema.omg.org/spec/XMI/2.1}id")
        if class_id not in class_by_id:
            continue
            
        # Only set parent if not already set from links
        if not class_by_id[class_id].parent_class:
            # Find generalization
            for gen in class_elem.findall(".//generalization[@xmi:type='uml:Generalization']", namespaces):
                parent_id = gen.get("general")
                if parent_id and parent_id in class_by_id:
                    class_by_id[class_id].parent_class = class_by_id[parent_id].name
                    break
    
    # Fourth pass: collect attributes with proper typing, multiplicity, and documentation
    for class_elem in root.findall(".//packagedElement[@xmi:type='uml:Class']", namespaces):
        class_id = class_elem.get("{http://schema.omg.org/spec/XMI/2.1}id")
        if class_id not in class_by_id:
            continue
            
        class_info = class_by_id[class_id]
        
        for attr in class_elem.findall(".//ownedAttribute[@xmi:type='uml:Property']", namespaces):
            attr_id = attr.get("{http://schema.omg.org/spec/XMI/2.1}id")
            attr_name = attr.get("name", "unknown")
            
            # Get attribute documentation
            attr_doc = attribute_docs.get(attr_id)
            
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
                is_optional=is_optional,
                documentation=attr_doc
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
            # Generate proper imports for __init__.py
            package_classes = [cls for cls in classes.values() if cls.package_path == package]
            imports = []
            
            for cls in package_classes:
                # Use proper case filename
                filename = cls.name  # Keep original case
                imports.append(f"from .{filename} import {cls.name}")
            
            with open(init_file, 'w') as f:
                f.write(f'"""Package: {package}"""\n\n')
                for imp in sorted(imports):
                    f.write(f'{imp}\n')

def generate_class_code(class_info: ClassInfo, all_classes: Dict[str, ClassInfo]) -> str:
    """Generate Python code for a single class"""
    lines = []
    
    # Imports
    imports = set()
    needs_field_import = any("List[" in attr.type_name and not attr.is_optional for attr in class_info.attributes)
    
    # Check if we need List import from attributes or association links
    association_links = [link for link in class_info.links if link.link_type == "Association" and link.target_name]
    
    if any("List[" in attr.type_name for attr in class_info.attributes) or association_links:
        imports.add("from typing import List, Optional, Protocol")
    else:
        imports.add("from typing import Optional, Protocol")
    
    if not class_info.is_abstract:
        if needs_field_import:
            imports.add("from dataclasses import dataclass, field")
        else:
            imports.add("from dataclasses import dataclass")
    
    # Add imports for referenced classes AND parent class
    classes_to_import = set()
    
    # Add parent class to imports
    if class_info.parent_class:
        for other_class in all_classes.values():
            if other_class.name == class_info.parent_class:
                classes_to_import.add((class_info.parent_class, other_class.package_path))
                break
    
    # Add attribute type classes to imports
    for attr in class_info.attributes:
        attr_type = attr.type_name
        if "List[" in attr_type:
            attr_type = attr_type.replace("List[", "").replace("]", "")
        
        # Check if this is a class we know about
        for other_class in all_classes.values():
            if other_class.name == attr_type and other_class.package_path != class_info.package_path:
                classes_to_import.add((attr_type, other_class.package_path))
    
    # Add association link classes to imports
    for link in association_links:
        if link.target_name:
            for other_class in all_classes.values():
                if other_class.name == link.target_name and other_class.package_path != class_info.package_path:
                    classes_to_import.add((link.target_name, other_class.package_path))
                    break
    
    # Generate import statements for classes
    for class_name, other_package_path in classes_to_import:
        if other_package_path != class_info.package_path:
            # Calculate relative import path
            current_parts = class_info.package_path.split('.') if class_info.package_path else []
            other_parts = other_package_path.split('.') if other_package_path else []
            
            # Find common prefix
            common_len = 0
            for i in range(min(len(current_parts), len(other_parts))):
                if current_parts[i] == other_parts[i]:
                    common_len += 1
                else:
                    break
            
            # Build relative path
            if common_len == len(current_parts) and common_len < len(other_parts):
                # Other is deeper, use relative import
                relative_path = '.'.join(other_parts[common_len:])
                imports.add(f"from .{relative_path}.{class_name} import {class_name}")
            elif common_len < len(current_parts):
                # Need to go up
                up_levels = len(current_parts) - common_len
                dots = '.' * (up_levels + 1)
                if common_len < len(other_parts):
                    relative_path = '.'.join(other_parts[common_len:])
                    imports.add(f"from {dots}{relative_path}.{class_name} import {class_name}")
                else:
                    imports.add(f"from {dots}{class_name} import {class_name}")
            else:
                # Same level
                imports.add(f"from .{class_name} import {class_name}")
    
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
    
    # Add enhanced docstring with XML IDs and documentation
    docstring_lines = [f'    """CGMES class: {class_info.name}']
    if class_info.xml_id:
        docstring_lines.append(f'    XML ID: {class_info.xml_id}')
    if class_info.package_id:
        docstring_lines.append(f'    Package ID: {class_info.package_id}')
    
    # Add class documentation if available
    if class_info.documentation:
        docstring_lines.append('')
        docstring_lines.append(f'    {class_info.documentation}')
    
    # Add attributes documentation to class docstring
    if class_info.attributes:
        attrs_with_docs = [attr for attr in class_info.attributes if attr.documentation]
        if attrs_with_docs:
            docstring_lines.append('')
            docstring_lines.append('    Attributes:')
            for attr in attrs_with_docs:
                # Clean up documentation text
                doc_text = attr.documentation.strip().replace('\n', ' ').replace('\r', '')
                # Limit line length for docstring
                if len(doc_text) > 60:
                    doc_text = doc_text[:60] + "..."
                docstring_lines.append(f'        {attr.name}: {doc_text}')
    
    docstring_lines.append('    """')
    
    lines.extend(docstring_lines)
    
    # Attributes without individual comments
    all_fields = list(class_info.attributes)
    
    # Add association links as attributes (but avoid duplicates and filter out non-class targets)
    existing_field_names = {field.name for field in all_fields}
    for link in association_links:
        if link.target_name and link.target_name not in existing_field_names:
            # Check if target is actually a class we know about
            target_exists = any(cls.name == link.target_name for cls in all_classes.values())
            if target_exists:
                # Create a field name from the target class name
                field_name = link.target_name
                all_fields.append(AttributeInfo(
                    name=field_name,
                    type_name=link.target_name,
                    is_optional=True
                ))
    
    if not all_fields:
        lines.append("    pass")
    else:
        for field in all_fields:
            if field.is_optional:
                lines.append(f"    {field.name}: Optional[{field.type_name}] = None")
            else:
                if "List[" in field.type_name:
                    lines.append(f"    {field.name}: {field.type_name} = field(default_factory=list)")
                else:
                    lines.append(f"    {field.name}: {field.type_name}")
    
    return "\n".join(lines)

def write_classes_to_files(classes: Dict[str, ClassInfo]) -> None:
    """Write all classes to their respective files in package structure"""
    for class_info in classes.values():
        # Generate code for the class
        code = generate_class_code(class_info, classes)
        
        # Determine file path
        if class_info.package_path:
            file_dir = OUTPUT_DIR / class_info.package_path.replace('.', '/')
        else:
            file_dir = OUTPUT_DIR
        
        file_path = file_dir / f"{class_info.name}.py"
        
        # Create directory if it doesn't exist
        file_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Write code to file
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
    
    print("Creating package structure...")
    create_package_structure(classes)
    
    print("Generating Python files...")
    write_classes_to_files(classes)
    
    print("Done!")

if __name__ == "__main__":
    main()