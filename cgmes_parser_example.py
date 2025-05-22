import sys
import os

# Add paths for imports
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
v24_path = os.path.join(os.path.dirname(__file__), 'v24')
sys.path.append(v24_path)

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
    
    # Example of accessing specific object types with their relationships
    substations = parser.get_objects_by_type("Substation")
    if substations:
        print(f"\nDetailed Substation Information:")
        for substation_id, substation in substations.items():
            print(f"Substation: {getattr(substation, 'name', 'Unknown')} (ID: {substation_id})")
            
            # Check if voltage levels are properly connected
            if hasattr(substation, 'VoltageLevels'):
                voltage_levels = getattr(substation, 'VoltageLevels', [])
                print(f"  Connected Voltage Levels: {len(voltage_levels)}")
                for i, vl in enumerate(voltage_levels):
                    if i >= 3:  # Limit to first 3 for brevity
                        print(f"    ... and {len(voltage_levels) - 3} more")
                        break
                    print(f"    - {getattr(vl, 'name', 'Unknown')} (ID: {getattr(vl, 'mRID', 'No ID')})")
            
            # Check if region is properly connected
            if hasattr(substation, 'Region_ref') and substation.Region_ref:
                region = substation.Region_ref
                print(f"  Connected to Region: {getattr(region, 'name', 'Unknown')} (ID: {getattr(region, 'mRID', 'No ID')})")

if __name__ == "__main__":
    main()
