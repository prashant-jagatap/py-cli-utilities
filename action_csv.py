import csv
import os
import shutil

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

def take_action(file_info):
    """
    Takes action based on the 'Action' column in the CSV file.
    :param file_info: A list of dictionaries containing file information.
    """
    for file in file_info:
        if file['Action'].lower() == 'del':
            try:
                os.remove(file['File Path'])
                print(f"Deleted file: {file['File Path']}")
            except FileNotFoundError:
                print(f"File not found: {file['File Path']}")
            except PermissionError:
                print(f"Permission denied: {file['File Path']}")
        elif file['Action'].lower() == 'mov':
            try:
                shutil.move(file['File Path'], file['Destination'])
                print(f"Moved file: {file['File Path']} to {file['Destination']}")
            except FileNotFoundError:
                print(f"File not found: {file['File Path']}")
            except PermissionError:
                print(f"Permission denied: {file['File Path']}")
            except shutil.Error as e:
                print(f"Error moving file: {e}")
        else:
            print(f"No action taken for file: {file['File Path']}")

def main():
    csv_file = 'file_list.csv'
    file_info = read_csv(csv_file)
    take_action(file_info)

if __name__ == "__main__":
    main()
   