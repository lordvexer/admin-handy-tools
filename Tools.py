import os
import platform
import shutil
import hashlib
import uuid
import filecmp
import datetime
from colorama import Fore, Style

def folder_tools():
    print(Fore.YELLOW + "Folder Tools Menu:")
    print("1. List contents of a folder")
    print("2. Create a new folder")
    print("3. Delete folder(s)")
    print("4. Show information of a folder")
    print("5. Search for a file")
    print("6. Copy files")
    print("7. Rename files or folders")
    print("8. Compress folder")
    print("9. Find duplicates")
    print("10. Permissions and ownership")
    print("11. View file details")
    print("12. Compare folders")
    print("13. Empty trash")
    print("14. Create symbolic links")
    choice = input("Enter your choice: ")

    if choice == '1':
        folder_path = input("Enter the path of the folder: ")
        list_folder_contents(folder_path)
    elif choice == '2':
        folder_name = input("Enter the name of the new folder (or 'random' for random names): ")
        if folder_name.lower() == "random":
            num_folders = int(input("Enter the number of random folders to create: "))
            max_name_length = int(input("Enter the maximum length of random folder names: "))
            create_many_folders(num_folders, max_name_length)
        else:
            create_folder(folder_name)
    elif choice == '3':
        delete_folders()
    elif choice == '4':
        folder_path = input("Enter the path of the folder: ")
        show_folder_info(folder_path)
    elif choice == '5':
        folder_path = input("Enter the path of the folder to search in: ")
        file_name = input("Enter the name of the file to search for: ")
        search_for_file(folder_path, file_name)
    elif choice == '6':
        source_path = input("Enter the path of the source folder: ")
        destination_path = input("Enter the path of the destination folder: ")
        copy_or_move_files(source_path, destination_path)
    elif choice == '7':
        old_name = input("Enter the current name of the file or folder: ")
        new_name = input("Enter the new name: ")
        rename_file_or_folder(old_name, new_name)
    elif choice == '8':
        folder_path = input("Enter the path of the folder to compress: ")
        compress_folder(folder_path)
    elif choice == '9':
        folder_path = input("Enter the path of the folder to search for duplicates: ")
        find_duplicates(folder_path)
    elif choice == '10':
        folder_path = input("Enter the path of the folder to manage permissions and ownership: ")
        manage_permissions_and_ownership(folder_path)
    elif choice == '11':
        file_path = input("Enter the path of the file to view details: ")
        view_file_details(file_path)
    elif choice == '12':
        folder1_path = input("Enter the path of the first folder: ")
        folder2_path = input("Enter the path of the second folder: ")
        compare_folders(folder1_path, folder2_path)
    elif choice == '13':
        trash_path = input("Enter the path of the trash folder: ")
        empty_trash(trash_path)
    elif choice == '14':
        source_path = input("Enter the path of the source file or folder: ")
        link_path = input("Enter the path of the symbolic link: ")
        create_symbolic_link(source_path, link_path)
    else:
        print("Invalid choice!")

def list_folder_contents(folder_path):
    try:
        contents = os.listdir(folder_path)
        print("Contents of folder:")
        for item in contents:
            print(item)
    except FileNotFoundError:
        print("Folder not found!")

def create_random_folder_name(max_length):
    return str(uuid.uuid4())[:max_length]

def create_many_folders(num_folders, max_name_length):
    for _ in range(num_folders):
        folder_name = create_random_folder_name(max_name_length)
        try:
            os.mkdir(folder_name)
            print(f"{Fore.GREEN}Folder '{folder_name}' created successfully.")
        except FileExistsError:
            print(f"{Fore.YELLOW}Folder '{folder_name}' already exists!")
        except Exception as e:
            print(f"{Fore.RED}An error occurred while creating folder '{folder_name}': {e}")

def create_folder(folder_name):
    folder_names = folder_name.split(',')
    for name in folder_names:
        try:
            os.mkdir(name.strip())  # Use strip() to remove any leading or trailing whitespace
            print(f"{Fore.GREEN}Folder '{name.strip()}' created successfully.")
        except FileExistsError:
            print(f"{Fore.YELLOW}Folder '{name.strip()}' already exists!")
        except Exception as e:
            print(f"{Fore.RED}An error occurred while creating folder '{name.strip()}': {e}")

def delete_folders():
    print(Fore.YELLOW + "Delete Folder(s) Menu:")
    print("1. Delete all folders in the current path")
    print("2. Delete all folders in a directory")
    print("3. Delete folder(s) by name")
    choice = input("Enter your choice: ")

    if choice == '1':
        delete_all_folders_in_current_path()
    elif choice == '2':
        folder_path = input("Enter the path of the directory: ")
        delete_all_folders(folder_path)
    elif choice == '3':
        folder_names = input("Enter the name(s) of the folder(s) to delete (separated by commas): ")
        delete_folders_by_name(folder_names)
    else:
        print("Invalid choice!")

def delete_all_folders_in_current_path():
    current_path = os.getcwd()
    delete_all_folders(current_path)

def delete_all_folders(folder_path):
    try:
        for item in os.listdir(folder_path):
            item_path = os.path.join(folder_path, item)
            if os.path.isdir(item_path):
                shutil.rmtree(item_path)
        print(f"{Fore.GREEN}All folders deleted successfully.")
    except FileNotFoundError:
        print(f"{Fore.YELLOW}Directory not found!")

def delete_folders_by_name(folder_names):
    names = folder_names.split(',')
    for name in names:
        try:
            shutil.rmtree(name.strip())  # Use strip() to remove any leading or trailing whitespace
            print(f"{Fore.GREEN}Folder '{name.strip()}' deleted successfully.")
        except FileNotFoundError:
            print(f"{Fore.YELLOW}Folder '{name.strip()}' not found!")
        except Exception as e:
            print(f"{Fore.RED}An error occurred while deleting folder '{name.strip()}': {e}")

def show_folder_info(folder_path):
    print(Fore.YELLOW + f"Information for folder: {folder_path}")
    num_folders, num_files = count_folders_and_files(folder_path)
    print(f"Number of Folders: {num_folders}")
    print(f"Number of Files: {num_files}")
    print(f"Largest File: {get_largest_file(folder_path)}")
    print(f"Smallest File: {get_smallest_file(folder_path)}")
    print(f"Last Modified: {get_last_modified(folder_path)}")
    print(f"First Modified: {get_first_modified(folder_path)}")
    print(f"Total Size: {get_folder_size(folder_path)} bytes")

def count_folders_and_files(folder_path):
    num_folders = 0
    num_files = 0
    try:
        for _, dirs, files in os.walk(folder_path):
            num_folders += len(dirs)
            num_files += len(files)
    except FileNotFoundError:
        print("Folder not found!")
    return num_folders, num_files

def get_largest_file(folder_path):
    largest_file = ""
    largest_size = 0
    for dirpath, _, filenames in os.walk(folder_path):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            file_size = os.path.getsize(file_path)
            if file_size > largest_size:
                largest_size = file_size
                largest_file = file_path
    return largest_file if largest_file else "No files found in the folder."

def get_smallest_file(folder_path):
    smallest_file = ""
    smallest_size = float('inf')
    for dirpath, _, filenames in os.walk(folder_path):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            file_size = os.path.getsize(file_path)
            if file_size < smallest_size:
                smallest_size = file_size
                smallest_file = file_path
    return smallest_file if smallest_file else "No files found in the folder."

def search_for_file(folder_path, file_name):
    found_files = []
    for dirpath, _, filenames in os.walk(folder_path):
        for filename in filenames:
            if filename == file_name:
                found_files.append(os.path.join(dirpath, filename))
    if found_files:
        print("Found files:")
        for file_path in found_files:
            print(file_path)
    else:
        print("File not found in the folder.")

def copy_or_move_files(source_path, destination_path):
    shutil.copytree(source_path, destination_path)
    print("Files copied successfully!")

def rename_file_or_folder(old_name, new_name):
    os.rename(old_name, new_name)
    print(f"{Fore.GREEN}Renamed successfully.")

def compress_folder(folder_path):
    shutil.make_archive(folder_path, 'zip', folder_path)
    print(f"{Fore.GREEN}Folder compressed successfully.")

def find_duplicates(folder_path):
    # Dictionary to store file hashes
    hash_map = {}
    duplicates = []

    # Iterate through all files in the folder and subfolders
    for root, _, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            # Calculate hash of the file
            file_hash = hash_file(file_path)
            # Check if the hash exists in the dictionary
            if file_hash in hash_map:
                # Duplicate found
                duplicates.append((file_path, hash_map[file_hash]))
            else:
                # Add hash to the dictionary
                hash_map[file_hash] = file_path

    # Prompt user for choice
    if duplicates:
        print("Duplicates found:")
        for duplicate in duplicates:
            print(f"Duplicate file: {duplicate[0]}")
            print(f"Original file: {duplicate[1]}")
        choice = input("Do you want to delete the original files? (yes/no): ")
        if choice.lower() == 'yes':
            # Delete all original files
            for duplicate in duplicates:
                os.remove(duplicate[1])
                print(f"Original file '{duplicate[1]}' deleted.")
        else:
            # Delete all duplicate files
            for duplicate in duplicates:
                os.remove(duplicate[0])
                print(f"Duplicate file '{duplicate[0]}' deleted.")
    else:
        print("No duplicates found.")

def hash_file(file_path):
    # Read the file in binary mode
    with open(file_path, 'rb') as f:
        # Create hash object
        hash_object = hashlib.md5()
        # Update hash object with file contents
        while chunk := f.read(4096):
            hash_object.update(chunk)
        # Get the hexadecimal digest
        file_hash = hash_object.hexdigest()
    return file_hash

def manage_permissions_and_ownership(folder_path):
    print("Manage Permissions and Ownership:")
    print("1. Change permissions of files and folders")
    print("2. Change ownership of files and folders")
    choice = input("Enter your choice: ")

    if choice == '1':
        change_permissions(folder_path)
    elif choice == '2':
        change_ownership(folder_path)
    else:
        print("Invalid choice!")

def change_permissions(folder_path):
    permissions = input("Enter new permissions (in octal format, e.g., 755): ")
    try:
        os.chmod(folder_path, int(permissions, 8))
        print("Permissions changed successfully.")
    except FileNotFoundError:
        print("Folder not found!")
    except Exception as e:
        print(f"An error occurred: {e}")

def change_ownership(folder_path):
    if platform.system() == "Windows":
        print("Changing ownership is not supported on Windows.")
        return

    user = input("Enter the new user (UID) for ownership: ")
    group = input("Enter the new group (GID) for ownership: ")
    try:
        os.chown(folder_path, int(user), int(group))
        print("Ownership changed successfully.")
    except FileNotFoundError:
        print("Folder not found!")
    except Exception as e:
        print(f"An error occurred: {e}")



def view_file_details(file_path):
    try:
        file_stat = os.stat(file_path)
        print("File Details:")
        print(f"Path: {file_path}")
        print(f"Size: {file_stat.st_size} bytes")
        print(f"Permissions: {oct(file_stat.st_mode & 0o777)}")
        print(f"Owner: {file_stat.st_uid if platform.system() != 'Windows' else 'N/A'}")
        print(f"Group: {file_stat.st_gid if platform.system() != 'Windows' else 'N/A'}")
        print(f"Last Modified: {datetime.datetime.fromtimestamp(file_stat.st_mtime)}")
        print(f"Last Accessed: {datetime.datetime.fromtimestamp(file_stat.st_atime)}")
        print(f"Created: {datetime.datetime.fromtimestamp(file_stat.st_ctime)}")
    except FileNotFoundError:
        print("File not found!")
    except Exception as e:
        print(f"An error occurred: {e}")


def compare_folders():
    folder1_path = input("Enter the path of the first folder: ")
    folder2_path = input("Enter the path of the second folder: ")

    print("Comparing folders:")
    print(f"Folder 1: {folder1_path}")
    print(f"Folder 2: {folder2_path}")

    # Check if the paths are valid directories
    if not os.path.isdir(folder1_path):
        print(f"Error: {folder1_path} is not a valid directory.")
        return
    if not os.path.isdir(folder2_path):
        print(f"Error: {folder2_path} is not a valid directory.")
        return

    # Get the immediate contents of each folder
    folder1_contents = set(os.listdir(folder1_path))
    folder2_contents = set(os.listdir(folder2_path))

    # Calculate the differences
    files_only_in_folder1 = folder1_contents - folder2_contents
    files_only_in_folder2 = folder2_contents - folder1_contents

    # Print out the differences
    if files_only_in_folder1:
        print(f"Files only in {folder1_path}:")
        for file in files_only_in_folder1:
            print(f"  {file}")
    else:
        print(f"No files only in {folder1_path}.")

    if files_only_in_folder2:
        print(f"Files only in {folder2_path}:")
        for file in files_only_in_folder2:
            print(f"  {file}")
    else:
        print(f"No files only in {folder2_path}.")

    common_files = folder1_contents.intersection(folder2_contents)
    if common_files:
        print(f"Common files:")
        for file in common_files:
            print(f"  {file}")
    else:
        print(f"No common files.")

    # Compare immediate subdirectories
    subdirectories_only_in_folder1 = [d for d in folder1_contents if os.path.isdir(os.path.join(folder1_path, d)) and d not in folder2_contents]
    if subdirectories_only_in_folder1:
        print(f"Subdirectories only in {folder1_path}:")
        for subdir in subdirectories_only_in_folder1:
            print(f"  {subdir}")
    else:
        print(f"No subdirectories only in {folder1_path}.")

    subdirectories_only_in_folder2 = [d for d in folder2_contents if os.path.isdir(os.path.join(folder2_path, d)) and d not in folder1_contents]
    if subdirectories_only_in_folder2:
        print(f"Subdirectories only in {folder2_path}:")
        for subdir in subdirectories_only_in_folder2:
            print(f"  {subdir}")
    else:
        print(f"No subdirectories only in {folder2_path}.")




def empty_trash(trash_path):
    # Functionality for emptying the trash folder can be added here
    pass

def create_symbolic_link(source_path, link_path):
    # Functionality for creating symbolic links can be added here
    pass

def main():
    while True:
        print(Style.RESET_ALL + "\nMain Menu:")
        print("1. Folder Tools")
        print("2. File Tools")
        print("0. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            folder_tools()
        elif choice == '2':
            # Add functionality for File Tools menu
            pass
        elif choice == '0':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")
        
    main()
