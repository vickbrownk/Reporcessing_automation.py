import os
import xml.etree.ElementTree as ET

# Placeholder for new date, the date you wan to change the transaction date to
new_date = '11072023'

# Folder path containing the XML files this would be the out folder on the server
folder_path = '/content/drive/MyDrive/Ready To Reprocess/8th-11th July'

# List of specific filenames to edit
files_to_edit = ['045RHVM998364189.xml.1','045YFAM429510198.xml.1','045STWK366795214.xml.1','045WFAR896271211.xml.1','045DDEN114220190.xml.1','0456951688994593962.xml.1','0457261688994703908.xml.1','0450001688994802050.xml.1','045JQHW395051190.xml.1','045PLLX767101218.xml.1','045MKAI057854221.xml.1','045ZZSG315587224.xml.1','045SDLM221451177.xml.1','045ZSIF216197182.xml.1','045TKJB985550219.xml.1','045TREL901448220.xml.1','045LXEL502068125.xml.1','045GWCA943543194.xml.1','0459001688999000886.xml.1']


# Specify the folder path to save the modified XML files, this will be the list of files gotten from Eco Omni
save_folder_path = '//content/drive/MyDrive/Ready for the out folder'

# Iterate over the XML files in the folder
for filename in files_to_edit:
    file_path = os.path.join(folder_path, filename)

    # Load XML file
    tree = ET.parse(file_path)
    root = tree.getroot()

    # Find all <ActivationDate> elements and update their text
    activation_date_elements = root.findall('.//ActivationDate')
    print(f'Number of ActivationDate elements found: {len(activation_date_elements)}')

    for element in activation_date_elements:
        element.text = new_date

    # Edit the <InstrumentDate> element's text with the new date placeholder
    instrument_date_element = root.find('.//InstrumentDate')
    instrument_date_element.text = new_date

    # Extract the filename without the extension and suffix
    mod_ref = filename[:-6]

    # Create a new file name with the third digit increased
    new_filename = mod_ref[:2] + str(int(mod_ref[2]) + 1) + mod_ref[3:]

    # Edit the <BatchReference>, <InstrumentRef>, and <DebitRef> elements' text with the new_filename generated
    for element_name in ['BatchReference', 'InstrumentRef', 'DebitRef']:
        element = root.find(f'.//{element_name}')
        element.text = new_filename

    # Save the modified XML file with the new name to the specified folder
    new_file_path = os.path.join(save_folder_path, new_filename + ".xml")
    tree.write(new_file_path)

    # Print the filename, new filename, and the location where the file is saved
    print(f'{filename} -> {new_filename}.xml - File modified and saved at {new_file_path}')
