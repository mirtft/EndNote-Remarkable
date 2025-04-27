
def extract_groups_from_endnote_library(file_path):
    try:
        # Parse the EndNote XML file
        tree = ET.parse(file_path)
        root = tree.getroot()

        # Extract groups
        groups = []
        for group in root.findall(".//Group"):
            group_name = group.find("GroupName")
            if group_name is not None:
                groups.append(group_name.text)

        return groups
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except ET.ParseError:
        print("Error parsing the EndNote library file.")
    return []

if __name__ == "__main__":
    import xml.etree.ElementTree as ET
    import os
    import sys
    
    # Replace with the path to your EndNote library XML file
    endnote_library_path = "/Users/s/sync/PubsTools/My EndNote Library.enlp"
    groups = extract_groups_from_endnote_library(endnote_library_path)

    if groups:
        print("Extracted Groups:")
        for group in groups:
            print(f"- {group}")
    else:
        print("No groups found or failed to extract groups.")