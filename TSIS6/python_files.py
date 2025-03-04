import os
import shutil
import string

def list_files_and_dirs(path):
    print("Directories:", [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))])
    print("Files:", [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))])
    print("All items:", os.listdir(path))

def check_path_access(path):
    print(f"Exists: {os.path.exists(path)}")
    print(f"Readable: {os.access(path, os.R_OK)}")
    print(f"Writable: {os.access(path, os.W_OK)}")
    print(f"Executable: {os.access(path, os.X_OK)}")

def test_path(path):
    if os.path.exists(path):
        print("Path exists.")
        print("Directory portion:", os.path.dirname(path))
        print("File portion:", os.path.basename(path))
    else:
        print("Path does not exist.")

def count_lines(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            print("Number of lines:", sum(1 for line in file))
    except FileNotFoundError:
        print("File not found.")

def write_list_to_file(file_path, data_list):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines("\n".join(data_list))
    print(f"List written to {file_path}")

def generate_text_files():
    for letter in string.ascii_uppercase:
        with open(f"{letter}.txt", 'w', encoding='utf-8') as file:
            file.write(f"This is file {letter}.txt\n")
    print("26 text files created.")

def copy_file(source, destination):
    try:
        shutil.copy(source, destination)
        print(f"Copied {source} to {destination}")
    except FileNotFoundError:
        print("Source file not found.")

def delete_file(path):
    if os.path.exists(path):
        if os.access(path, os.W_OK):
            os.remove(path)
            print(f"Deleted {path}")
        else:
            print("No write access to delete the file.")
    else:
        print("File does not exist.")
