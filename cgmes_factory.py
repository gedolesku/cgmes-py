import xml.etree.ElementTree as ET
import importlib
import re
import sys
import types
from typing import Dict, Any, Optional, Set, Type, List, get_origin, get_args
import logging
import inspect

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
        self.module_import_failures = set()
    
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
            
            # Fall back to the original mapping logic if v24 structure fails
            possible_modules = [
                f"{self.base_package}.CoreProfile.Core.{class_name}",
                f"{self.base_package}.EquipmentProfile.Core.{class_name}",
                f"{self.base_package}.DiagramLayoutProfile.DiagramLayout.{class_name}",
                f"{self.base_package}.DynamicsProfile.StandardModels.ExcitationSystemDynamics.{class_name}",
                f"{self.base_package}.DomainProfile.{class_name}"
            ]
            
            for module_path in possible_modules:
                if module_path in self.module_import_failures:
                    continue
                    
                try:
                    self.logger.debug(f"Trying to import {module_path}")
                    module = importlib.import_module(module_path)
                    class_obj = getattr(module, class_name)
                    self.class_cache[cim_type] = class_obj
                    return class_obj
                except (ImportError, AttributeError):
                    self.module_import_failures.add(module_path)
                    continue
            
            # Last resort: create a dynamic class
            self.logger.warning(f"Creating dynamic class for CIM type: {class_name}")
            dynamic_class = type(class_name, (), {
                'mRID': None,
                'name': None,
                '__annotations__': {},
                '__doc__': f"Dynamically created class for {class_name}"
            })
            self.class_cache[cim_type] = dynamic_class
            return dynamic_class
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
            # # Set the mRID if the class has that attribute
            # if hasattr(obj, 'mRID'):
            #     obj.mRID = rdf_id
            
            # Process all attributes and references
            self._process_attributes(element, obj)
            
            # Save the created object
            self.created_objects[rdf_id] = obj
            
            # # Process any pending references to this object
            # if rdf_id in self.pending_references:
            #     for (target_obj, attr_name) in self.pending_references[rdf_id]:
            #         setattr(target_obj, attr_name, obj)
            #     del self.pending_references[rdf_id]
            
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
            if '.' in attr_name:
                _, attr_name = attr_name.split('.')
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
                    
                    # Handle specific case for Region references in Substation objects
                    if attr_name == "Region" and hasattr(obj, "Region_ref"):
                        attr_name = "Region_ref"  # Use the reference attribute instead
                    
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
    
    def connect_cgmes(self) -> None:
        """Connect all reference objects after all objects have been loaded"""
        self.logger.info("Starting to connect CGMES objects...")
        
        # Process each object to find and connect references
        for obj_id, obj in self.created_objects.items():
            self._connect_object_references(obj)
        
        self.logger.info("Finished connecting CGMES objects")

    def _connect_object_references(self, obj: Any) -> None:
        """Connect references for a specific object"""
        try:
            # Get all attributes of the object
            for attr_name in dir(obj):
                # Skip special/private attributes and methods
                if attr_name.startswith('_') or callable(getattr(obj, attr_name)):
                    continue
                
                # If this is a reference attribute (ends with _ref)
                if attr_name.endswith('_ref') and getattr(obj, attr_name) is not None:
                    # Get the referenced object
                    ref_obj = getattr(obj, attr_name)#todo should be here at first? it should not be assigned?
                    
                    # Find the base attribute name without _ref
                    base_attr_name = attr_name[:-4]  # Remove _ref suffix
                    
                    # Also set the string attribute if it exists
                    if hasattr(obj, base_attr_name):
                        try:
                            # Try to set the string attribute with the mRID of the referenced object
                            if hasattr(ref_obj, 'mRID'):
                                setattr(obj, base_attr_name, ref_obj.mRID)
                            else:
                                setattr(obj, base_attr_name, str(ref_obj))
                        except Exception as e:
                            self.logger.debug(f"Could not set string attribute {base_attr_name} for {obj.__class__.__name__}: {str(e)}")
                    
                    # Now find the inverse relationship
                    try:
                        self._establish_bidirectional_link(obj, ref_obj, base_attr_name)
                    except Exception as e:
                        self.logger.debug(f"Could not establish bidirectional link for {obj.__class__.__name__}.{attr_name}: {str(e)}")
                
        except Exception as e:
            self.logger.error(f"Error connecting references for {obj.__class__.__name__}: {str(e)}")

    def _establish_bidirectional_link(self, source_obj: Any, target_obj: Any, source_attr_base: str) -> None:
        """Establish bidirectional links between objects"""
        # Determine the type name of the source object to find matching list attributes in target
        source_type = source_obj.__class__.__name__
        
        # Look for a list attribute in the target object with a type matching the source object
        potential_list_attrs = self._find_list_attributes(target_obj, source_type)
        
        # If we found a matching list attribute, add the source object to it
        for list_attr in potential_list_attrs:
            try:
                # Safely add the source object to the list
                self._add_to_list(target_obj, list_attr, source_obj)
                self.logger.debug(f"Added {source_obj.__class__.__name__} to {target_obj.__class__.__name__}.{list_attr}")
                break  # Successfully added to one list, stop looking
            except Exception as e:
                self.logger.debug(f"Failed to add to list {list_attr}: {str(e)}")

    def _find_list_attributes(self, obj: Any, type_name: str) -> List[str]:
        """Find list attributes in an object that might contain objects of a specific type"""
        result = []
        
        # Check all attributes of the object
        for attr_name in dir(obj):
            # Skip special/private attributes and methods
            if attr_name.startswith('_') or callable(getattr(obj, attr_name)):
                continue
            
            # Try to get the attribute value
            try:
                attr_value = getattr(obj, attr_name)
                
                # Check if it's a list
                if isinstance(attr_value, list):
                    # Check type annotation if available
                    annotations = getattr(obj.__class__, '__annotations__', {})
                    if attr_name in annotations:
                        annotation = annotations[attr_name]
                        
                        # Check if annotation is List[X] and X matches our type name
                        try:
                            # For Python 3.8+
                            origin = get_origin(annotation)
                            args = get_args(annotation)
                            
                            if origin is list and args and args[0].__name__ == type_name:
                                result.append(attr_name)
                                continue
                        except (AttributeError, TypeError):
                            # Fallback for older Python or simple type hints
                            pass
                    
                    # Naming convention check - plural of the type name
                    if attr_name.lower() == f"{type_name.lower()}s":
                        result.append(attr_name)
                    # Or the attribute name ends with the type name
                    elif attr_name.endswith(type_name + 's'):
                        result.append(attr_name)
            except Exception:
                continue
        
        return result

    def _add_to_list(self, obj: Any, list_attr: str, item: Any) -> None:
        """Safely add an item to a list attribute of an object"""
        attr_value = getattr(obj, list_attr)
        
        # If it's None, initialize it
        if attr_value is None:
            setattr(obj, list_attr, [item])
        # If it's already a list, append to it
        elif isinstance(attr_value, list):
            if item not in attr_value:  # Avoid duplicates
                attr_value.append(item)
        else:
            raise TypeError(f"{list_attr} is not a list")
    
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
        
        # Connect objects after all have been loaded
        self.factory.connect_cgmes()
        
        return self.objects_by_type
    
    def get_objects_by_type(self, obj_type: str) -> Dict[str, Any]:
        """Get all objects of a specific type"""
        return self.objects_by_type.get(obj_type, {})
