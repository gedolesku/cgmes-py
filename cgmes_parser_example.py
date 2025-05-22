import sys
import os

# Add paths for imports
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
v24_path = os.path.join(os.path.dirname(__file__), 'v24')
sys.path.append(v24_path)

# Fix for circular imports - add this BEFORE other imports
import importlib.util
import importlib.machinery
import types

# Create a custom loader that will handle circular imports
def patch_circular_imports():
    orig_load_module = importlib.machinery.SourceFileLoader.load_module
    
    def patched_load_module(self, fullname):
        try:
            return orig_load_module(self, fullname)
        except ImportError as e:
            if "circular import" in str(e).lower():
                # Return the partially initialized module rather than failing
                spec = importlib.machinery.ModuleSpec(fullname, self)
                module = importlib.util.module_from_spec(spec)
                sys.modules[fullname] = module
                return module
            raise
    
    importlib.machinery.SourceFileLoader.load_module = patched_load_module

# Patch import system to handle circular imports
patch_circular_imports()

from cgmes_factory import CGMESParser, CGMESObjectFactory
import logging

def main():
    # Setup logging
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    
    # Create parser with factory
    factory = CGMESObjectFactory()
    parser = CGMESParser(factory)
    
    # Parse a file
    file_path = r"c:\git-code\tna\python-cgmes\cgmes-models\SmallGrid\20210112T1742Z_1D_GB_EQ_001.xml"
    objects = parser.parse_file(file_path)
    
    # Display parsed objects
    for obj_type, obj_dict in objects.items():
        print(f"Found {len(obj_dict)} objects of type {obj_type}")
        
        # Print details of first 5 objects
        for i, (obj_id, obj) in enumerate(obj_dict.items()):
            if i >= 5:
                break
            print(f"  - {obj_id}: {getattr(obj, 'name', 'No name')}")
    
    # Example of accessing specific object types
    substations = parser.get_objects_by_type("Substation")
    if substations:
        print(f"\nDetailed Substation Information:")
        for substation_id, substation in substations.items():
            print(f"Substation: {getattr(substation, 'name', 'Unknown')} (ID: {substation_id})")
            
            # If voltage levels are properly linked, we could access them
            # This depends on the references being properly resolved
            if hasattr(substation, 'voltageLevels') and substation.voltageLevels:
                print(f"  Voltage Levels:")
                for vl in substation.voltageLevels:
                    print(f"    - {getattr(vl, 'name', 'Unknown')}")

if __name__ == "__main__":
    main()
