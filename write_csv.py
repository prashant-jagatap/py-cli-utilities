import os
import csv
from datetime import datetime

def list_files(root_dir):
    """
    Lists all files in a directory and its subdirectories.
    :param root_dir: The root directory to start the search from.
    :return: A list of dictionaries containing file information.
    """
    files_info = []
    for root, dirs, filenames in os.walk(root_dir):
        for filename in filenames:
            file_path = os.path.join(root, filename)
            file_size = os.path.getsize(file_path)
            file_date = datetime.fromtimestamp(os.path.getmtime(file_path)).strftime('%Y-%m-%d %H:%M:%S')
            files_info.append({
                'File Path': file_path,
                'Size (bytes)': file_size,
                'Last Modified': file_date,
                'Action': '',
                'Destination': ''
            })
    return files_info

def write_to_csv(file_info, csv_file):
    """
    Writes file information to a CSV file.
    :param file_info: A list of dictionaries containing file information.
    :param csv_file: Path to the output CSV file.
    """
    fieldnames = ['File Path', 'Size (bytes)', 'Last Modified', 'Action', 'Destination']
    with open(csv_file, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for file in file_info:
            writer.writerow(file)

def main():
    root_directory = '.'  # modify this path
    output_csv = 'file_list.csv'
    all_files = list_files(root_directory)
    write_to_csv(all_files, output_csv)
    print(f"File list has been written to {output_csv}")

if __name__ == "__main__":
    main()