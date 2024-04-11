UnnDee5
UnnDee5 is the counterpart script to EmmDee5, designed to undo the file renaming performed by EmmDee5 using the provided CSV file. This Python script ensures the restoration of original filenames by comparing MD5 hashes before and after the renaming process, ensuring the integrity of the files.

Features
File Restoration: UnnDee5 restores the original filenames by reverting the changes made by EmmDee5, based on the information provided in the CSV file.
MD5 Hash Comparison: The script verifies the integrity of files by comparing their MD5 hashes before and after the renaming process. This ensures that no unauthorized alterations have been made to the files during the renaming process.
CSV Input and Output: UnnDee5 takes the CSV file generated by EmmDee5 as input and produces another CSV file (undo_renaming_results.csv) containing the comparison results of the file restoration process.

Usage
Ensure you have Python installed on your system.
Copy the UnnDee5 script to the directory containing the files you want to restore.
Place the CSV file generated by EmmDee5 (EmmDee5.csv) in the same directory as UnnDee5.
Open a terminal or command prompt and navigate to the directory containing UnnDee5.

Run UnnDee5 using the following command:
python UnnDee5.py

UnnDee5 will read the CSV file and restore the original filenames based on the mapping provided.
The script will then perform a hash comparison to verify the integrity of each file before and after the renaming process.
Finally, UnnDee5 will generate another CSV file (undo_renaming_results.csv) containing the comparison results of the file restoration process.
You can review this CSV file to ensure that the restoration process was successful and that file integrity has been maintained.

Disclaimer
UnnDee5 relies on the information provided in the CSV file generated by EmmDee5. Please ensure that you have the correct CSV file and that it has not been altered or corrupted before running UnnDee5. Additionally, make sure to have proper backups of your files before executing the script to avoid any unintended data loss.

Note: Exercise caution and verify the integrity of the restored files as needed.

/VooDooFus/
