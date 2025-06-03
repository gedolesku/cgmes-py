import os
import xml.etree.ElementTree as ET

# Config
input_file = r"cgmes-models\v24\ENTSOE_CGMES_v2.4.14_28May2014.xml"
output_dir = "split_xml"
max_file_size_mb = 5  # Set a target max file size for uploads

# Create output directory
os.makedirs(output_dir, exist_ok=True)

# Parse the large XML
tree = ET.parse(input_file)
root = tree.getroot()

# Namespace handling if present
ns = {'cim': root.tag.split('}')[0].strip('{')} if '}' in root.tag else {}

# Split by each direct child of root
for i, child in enumerate(root):
    new_root = ET.Element(root.tag)
    new_root.append(child)

    # Create a new tree and write it to a file
    new_tree = ET.ElementTree(new_root)
    filename = os.path.join(output_dir, f"chunk_{i+1:04d}.xml")
    new_tree.write(filename, encoding='utf-8', xml_declaration=True)

    # Check file size
    size_mb = os.path.getsize(filename) / (1024 * 1024)
    if size_mb > max_file_size_mb:
        print(f"Warning: {filename} is {size_mb:.2f}MB, may be too large.")

print("Done splitting. You can now try uploading the smaller files.")
