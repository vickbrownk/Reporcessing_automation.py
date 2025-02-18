# XML Transaction Date Modifier

## Overview
This Python script modifies specific XML files by updating transaction dates and references within the XML structure. The script reads a predefined set of XML files, updates date-related fields, and generates new XML files with modified names.

## Features
- Updates the `<ActivationDate>` and `<InstrumentDate>` fields in XML files.
- Modifies `<BatchReference>`, `<InstrumentRef>`, and `<DebitRef>` with a dynamically generated reference.
- Saves the modified files in a designated folder with updated filenames.

## Prerequisites
Ensure you have the following installed:
- Python 3.x
- Required Python modules:
  - `os`
  - `xml.etree.ElementTree`

## Project Structure
```
project_folder/
│── script.py                 # Main Python script
│── README.md                 # Project documentation
│── input_files/              # Folder containing XML files to be processed
│── output_files/             # Folder where modified XML files are saved
```

## Usage
### 1. Set Up Folder Paths
Modify the following variables in the script to match your file locations:
```python
folder_path = '/content/drive/MyDrive/Ready To Reprocess/8th-11th July'  # Source folder
save_folder_path = '/content/drive/MyDrive/Ready for the out folder'  # Destination folder
```

### 2. Specify the New Transaction Date
Update the `new_date` variable with the desired transaction date:
```python
new_date = '11072023'
```

### 3. Define the Files to Edit
List the specific XML files you want to modify in the `files_to_edit` list:
```python
files_to_edit = ['045RHVM998364189.xml.1', '045YFAM429510198.xml.1', ...]
```

### 4. Run the Script
Execute the script using:
```sh
python script.py
```

### 5. Output
The script will:
- Locate the specified XML files.
- Modify the transaction date and reference fields.
- Generate new XML files with updated names.
- Save them to the designated folder.
- Print log messages indicating progress.

### Example Log Output
```
Number of ActivationDate elements found: 1
045RHVM998364189.xml.1 -> 045SHVM998364189.xml - File modified and saved at /content/drive/MyDrive/Ready for the out folder/045SHVM998364189.xml
```

## Notes
- Ensure the XML files have the required structure with `<ActivationDate>`, `<InstrumentDate>`, and reference fields (`<BatchReference>`, `<InstrumentRef>`, `<DebitRef>`).
- The script assumes the third character in the filename is a digit that can be incremented.
- Always verify the modified files before further processing.

## License
This project is open-source and available for modification and distribution.

## Author
[Victor Brown]

