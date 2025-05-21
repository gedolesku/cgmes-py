import xml.etree.ElementTree as ET
import importlib
import re
import sys
from typing import Dict, Any, Optional, Set, Type
import logging

class CGMESObjectFactory:
    """Factory for creating CGMES model objects from XML data"""
    
    def __init__(self, base_package: str = "ENTSOE.CommonGridModelExchangeStandard"):
        self.base_package = base_package
        self.class_cache: Dict[str, Type] = {}
        self.created_objects: Dict[str, Any] = {}
        self.pending_references: Dict[str, list] = {}
        self.namespaces = {
            'cim': 'http://iec.ch/TC57/CIM100#',
            'rdf': 'http://www.w3.org/1999/02/22-rdf-syntax-ns#',
            'md': 'http://iec.ch/TC57/61970-552/ModelDescription/1#'
        }
        self.logger = logging.getLogger(__name__)
    
    def get_class_for_type(self, cim_type: str) -> Optional[Type]:
        """Get the Python class that corresponds to the CIM type"""
        if cim_type in self.class_cache:
            return self.class_cache[cim_type]
        
        try:
            # Remove namespace prefix if present
            if ':' in cim_type:
                _, class_name = cim_type.split(':')
            else:
                class_name = cim_type
            
            # Try to import from the v24 package structure first
            v24_paths = [
                f"v24.TC57CIM.IEC61970.Base.Wires.{class_name}",
                f"v24.TC57CIM.IEC61970.Base.Core.{class_name}",
                f"v24.TC57CIM.IEC61970.Base.Domain.{class_name}",
                f"v24.TC57CIM.IEC61970.Base.DiagramLayout.{class_name}",
                f"v24.TC57CIM.IEC61970.Base.Topology.{class_name}",
                f"v24.TC57CIM.IEC61970.Base.StateVariables.{class_name}"
            ]
            
            for module_path in v24_paths:
                try:
                    self.logger.debug(f"Trying to import {module_path}")
                    module = importlib.import_module(module_path)
                    class_obj = getattr(module, class_name)
                    self.class_cache[cim_type] = class_obj
                    return class_obj
                except (ImportError, AttributeError) as e:
                    self.logger.debug(f"Failed to import {module_path}: {str(e)}")
                    continue
            
            # Fall back to the original mapping logic if v24 structure fails
            possible_modules = [
                f"{self.base_package}.CoreProfile.Core.{class_name}",
                f"{self.base_package}.EquipmentProfile.Core.{class_name}",
                f"{self.base_package}.DiagramLayoutProfile.DiagramLayout.{class_name}",
                f"{self.base_package}.DynamicsProfile.StandardModels.ExcitationSystemDynamics.{class_name}",
                f"{self.base_package}.DomainProfile.{class_name}"
            ]
            
            for module_path in possible_modules:
                try:
                    self.logger.debug(f"Trying to import {module_path}")
                    module = importlib.import_module(module_path)
                    class_obj = getattr(module, class_name)
                    self.class_cache[cim_type] = class_obj
                    return class_obj
                except (ImportError, AttributeError):
                    continue
            
            self.logger.warning(f"Could not find class for CIM type: {cim_type}")
            return None
        except Exception as e:
            self.logger.error(f"Error finding class for {cim_type}: {str(e)}")
            return None
    
    def create_object(self, element: ET.Element) -> Optional[Any]:
        """Create an object from an XML element"""
        # Get the RDF ID
        rdf_id = element.get(f"{{{self.namespaces['rdf']}}}ID")
        if not rdf_id:
            self.logger.warning(f"Element has no RDF ID: {ET.tostring(element, encoding='unicode')}")
            return None
        
        # Check if object already exists
        if rdf_id in self.created_objects:
            return self.created_objects[rdf_id]
        
        # Get the CIM type (from the tag name)
        tag = element.tag
        if '}' in tag:
            cim_type = tag.split('}')[1]
        else:
            cim_type = tag
        
        # Get the Python class
        cls = self.get_class_for_type(cim_type)
        if not cls:
            self.logger.warning(f"Could not find class for {cim_type}")
            return None
        
        # Create an instance of the class
        try:
            obj = cls()
            # Set the mRID if the class has that attribute
            if hasattr(obj, 'mRID'):
                obj.mRID = rdf_id
            
            # Process all attributes and references
            self._process_attributes(element, obj)
            
            # Save the created object
            self.created_objects[rdf_id] = obj
            
            # Process any pending references to this object
            if rdf_id in self.pending_references:
                for (target_obj, attr_name) in self.pending_references[rdf_id]:
                    setattr(target_obj, attr_name, obj)
                del self.pending_references[rdf_id]
            
            return obj
        except Exception as e:
            self.logger.error(f"Error creating object for {cim_type}: {str(e)}")
            return None
    
    def _process_attributes(self, element: ET.Element, obj: Any) -> None:
        """Process all attributes and references for an object"""
        for child in element:
            tag = child.tag
            if '}' in tag:
                _, attr_name = tag.split('}')
            else:
                attr_name = tag
            
            # Check if attribute exists in the class
            if not hasattr(obj, attr_name):
                # It might be in a different format (e.g., camelCase vs snake_case)
                snake_case = self._camel_to_snake(attr_name)
                if hasattr(obj, snake_case):
                    attr_name = snake_case
                else:
                    self.logger.debug(f"Attribute {attr_name} not found in {obj.__class__.__name__}")
                    continue
            
            # Check if this is a reference to another object
            ref = child.get(f"{{{self.namespaces['rdf']}}}resource")
            if ref:
                # This is a reference to another object
                if ref.startswith('#'):
                    ref_id = ref[1:]  # Remove the leading '#'
                    
                    # If the referenced object already exists, set the reference
                    if ref_id in self.created_objects:
                        setattr(obj, attr_name, self.created_objects[ref_id])
                    else:
                        # Otherwise, add to pending references
                        if ref_id not in self.pending_references:
                            self.pending_references[ref_id] = []
                        self.pending_references[ref_id].append((obj, attr_name))
            else:
                # This is a simple attribute
                setattr(obj, attr_name, child.text)
    
    def _camel_to_snake(self, name: str) -> str:
        """Convert camelCase to snake_case"""
        name = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
        return re.sub('([a-z0-9])([A-Z])', r'\1_\2', name).lower()


class CGMESParser:
    """Parser for CGMES XML files"""
    
    def __init__(self, factory: Optional[CGMESObjectFactory] = None):
        self.factory = factory or CGMESObjectFactory()
        self.objects_by_type = {}
    
    def parse_file(self, file_path: str) -> Dict[str, Dict[str, Any]]:
        """Parse a CGMES XML file and return created objects"""
        tree = ET.parse(file_path)
        root = tree.getroot()
        
        # Register any namespaces from the file
        for key, value in root.attrib.items():
            if key.startswith('{http://www.w3.org/2000/xmlns/}'):
                prefix = key.split('}')[1]
                self.factory.namespaces[prefix] = value
        
        # Process all elements that have an rdf:ID attribute
        for element in root.findall('.//*[@{' + self.factory.namespaces['rdf'] + '}ID]'):
            obj = self.factory.create_object(element)
            if obj:
                obj_type = obj.__class__.__name__
                if obj_type not in self.objects_by_type:
                    self.objects_by_type[obj_type] = {}
                
                # Use mRID if available, otherwise generate a key
                key = getattr(obj, 'mRID', id(obj))
                self.objects_by_type[obj_type][key] = obj
        
        return self.objects_by_type
    
    def get_objects_by_type(self, obj_type: str) -> Dict[str, Any]:
        """Get all objects of a specific type"""
        return self.objects_by_type.get(obj_type, {})
