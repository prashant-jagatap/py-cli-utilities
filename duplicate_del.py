import os
import csv
import hashlib

def read_csv(file_path):
    """
    Reads the CSV file and returns a list of dictionaries containing file information.
    :param file_path: Path to the CSV file.
    :return: A list of dictionaries containing file information.
    """
    file_info = []
    try:
        with open(file_path, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                file_info.append(row)
    except FileNotFoundError:
        print(f"The file {file_path} does not exist.")
    return file_info

def calculate_hash(file_path):
    """
    Calculates the hash of a file.
    :param file_path: Path to the file.
    :return: The hash of the file.
    """
    try:
        with open(file_path, 'rb') as file:
            return hashlib.md5(file.read()).hexdigest()
    except FileNotFoundError:
        print(f"The file {file_path} does not exist.")
        return None

def identify_duplicates(file_info):
    """
    Identifies duplicate files based on their hashes.
    :param file_info: A list of dictionaries containing file information.
    :return: A dictionary where the keys are file hashes and the values are lists of file paths.
    """
    file_hashes = {}
    for file in file_info:
        file_path = file['File Path']
        file_hash = calculate_hash(file_path)
        if file_hash is not None:
            if file_hash in file_hashes:
                file_hashes[file_hash].append(file_path)
            else:
                file_hashes[file_hash] = [file_path]
    return file_hashes

def delete_duplicates(file_hashes):
    """
    Deletes duplicate files based on the 'Action' column in the CSV file.
    :param file_hashes: A dictionary where the keys are file hashes and the values are lists of file paths.
    """
    for file_hash, file_paths in file_hashes.items():
        if len(file_paths) > 1:
            for file_path in file_paths[1:]:
                try:
                    os.remove(file_path)
                    print(f"Deleted duplicate file: {file_path}")
                except FileNotFoundError:
                    print(f"File not found: {file_path}")
                except PermissionError:
                    print(f"Permission denied: {file_path}")

def main():
    csv_file = 'file_list.csv'
    file_info = read_csv(csv_file)
    file_hashes = identify_duplicates(file_info)
    delete_duplicates(file_hashes)

if __name__ == "__main__":
    main()