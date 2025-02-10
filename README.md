# py-cli-utilities

## excluded_directories.txt
 - Add directories path line by line, these path will be ignored by write_csv.py.

## action_csv.py
 - Run the write_csv.py script to generate the file_list.csv file.
 - Open the file_list.csv file in a spreadsheet program or text editor and modify the Action column either to 'del' or 'mov' for each file. If you choose to move a file, also fill in the Destination column with the desired destination path.
 - Save the modified file_list.csv file.
 - Run the action_csv.py script to take the specified actions on the files.

## duplicate_del.py
 - Run the write_csv.py script to generate the file_list.csv file.
 - Open the file_list.csv file in a spreadsheet program or text editor and modify the Action column either to 'keep' for each file or leave empty. 
 - Save the modified file_list.csv file.
 - Run duplicate_del.py to delete duplicate files based on the 'Action' column in the CSV file. If the 'Action' column is empty, the file is deleted. If the 'Action' column is 'keep', the file is not deleted.


Note: Tested only on MacOS.
