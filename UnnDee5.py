import os
import hashlib
import csv
from tqdm import tqdm

def get_md5(filename):
    """Calculate the MD5 hash of a file."""
    hash_md5 = hashlib.md5()
    with open(filename, "rb") as file:
        for chunk in iter(lambda: file.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def read_csv(filename):
    """Read data from a CSV file."""
    data = {}
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        for row in reader:
            data[row[1]] = row[0]  # New filename -> Old filename
    return data

def undo_renaming(csv_filename):
    """Undo the renaming done by EmmDee5.py script based on the data in EmmDee5.csv."""
    current_dir = os.path.dirname(os.path.realpath(__file__))
    csv_filepath = os.path.join(current_dir, csv_filename)
    if not os.path.exists(csv_filepath):
        print(f"Error: '{csv_filename}' not found in the current directory.")
        return

    original_filenames = read_csv(csv_filepath)
    renamed_files = [f for f in original_filenames.keys() if f != "EmmDee5.py" and f != csv_filename]
    hashes_before = {}
    hashes_after = {}
    results = {}  # To store the comparison results
    
    with tqdm(total=len(renamed_files), desc="Total Progress") as pbar_total:
        for renamed_file in renamed_files:
            old_filename = original_filenames[renamed_file]
            old_filepath = os.path.join(current_dir, old_filename)
            renamed_filepath = os.path.join(current_dir, renamed_file)
            
            # Calculate MD5 hash before renaming
            hash_before = get_md5(renamed_filepath)
            hashes_before[renamed_file] = hash_before
            
            # Rename the file back to its original name
            os.rename(renamed_filepath, old_filepath)
            
            # Calculate MD5 hash after renaming
            hash_after = get_md5(old_filepath)
            hashes_after[old_filename] = hash_after
            
            # Check if hashes match before and after renaming
            if hash_before == hash_after:
                results[old_filename] = "Matched"
            else:
                results[old_filename] = "Not Matched"
            
            pbar_total.update(1)
            tqdm.write(f"Restored {renamed_file} to {old_filename}")
    
    # Write comparison results to CSV file
    csv_output = os.path.join(current_dir, "undo_renaming_results.csv")
    with open(csv_output, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Old Filename", "Hash Before Renaming", "Hash After Renaming", "Hashes Matched"])
        for filename, hash_match_status in results.items():
            writer.writerow([filename, hashes_before.get(filename, ""), hashes_after.get(filename, ""), hash_match_status])
    
    tqdm.write(f"CSV file '{csv_output}' has been generated successfully.")

if __name__ == "__main__":
    undo_renaming("EmmDee5.csv")

