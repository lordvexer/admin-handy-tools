import os
import platform
import subprocess
import sys
import logging

# Function to check and install packages
def check_and_install(package):
    try:
        __import__(package)
    except ImportError:
        print(f"{package} not found. Installing...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# List of required packages
required_packages = [
    "pywin32",
    "colorama",
    "Pillow",
    "psutil",
    "windows-curses",  # Assuming you need this for Windows
    "moviepy",
    "cryptography",
    "tqdm",
    "speedtest-cli",
    "iperf3"
]

# Install required packages if not already installed
# for package in required_packages:
#     check_and_install(package)

# Now import your modules
from ldap3 import Server, Connection, SIMPLE, SYNC, ALL,ALL_ATTRIBUTES, ALL_OPERATIONAL_ATTRIBUTES, SUBTREE
from PIL import Image
from colorama import Fore, Style, init
from moviepy.editor import VideoFileClip
from cryptography.fernet import Fernet
import getpass
import shutil
import hashlib
import traceback
import uuid
import string
import random
import datetime
import zipfile
import psutil
import curses
import time
import socket
import threading
import ctypes
import win32api
import winreg
import msvcrt 
import speedtest
import iperf3
import re
import patoolib
import rarfile



##################################### FOLDER TOOLS #####################################


def folder_tools():
    clear_screen()
    print(Fore.RED + "\nFolder Tools Menu:")
    print("1. List contents of a folder")
    print("2. Create a new folder")
    print("3. Delete folder(s)")
    print("4. Show information of a folder")
    print("5. Search for a File and Folders")
    print("6. Copy files")
    print("7. Rename files or folders")
    print("8. Compress folder")
    print("9. Find duplicates")
    print("10. Permissions and ownership")
    print("11. View file details")
    print("12. Compare folders")
    print("13. Create symbolic links")
    print("0. Back")
    choice = input(Fore.CYAN +"Enter your choice: ")

    if choice == '1':
        folder_path = input("Enter the path of the folder: ")
        list_folder_contents(folder_path)
    elif choice == '2':
        folder_path=input("Enter Path To Create Folder(s): ").strip()
        if not folder_path:
            print("No folder path provided. Exiting.")
        folder_name = input("Enter the name of the new folder (or 'random' for random names): ").strip()
        if folder_name.lower() == "random":
            num_folders_input = input("Enter the number of random folders to create (Default=10): ").strip()
            num_folders = int(num_folders_input) if num_folders_input else 10

            max_length_input = input("Enter the maximum length of random folder names (Default=10): ").strip()
            max_name_length = int(max_length_input) if max_length_input else 10
            
            create_many_folders(num_folders, max_name_length, folder_path)
        elif not folder_name:
            print("No folder name provided. Exiting.")
        else:
            create_folder(folder_name,folder_path)
    elif choice == '3':
        delete_folders()
    elif choice == '4':
        folder_path = input("Enter the path of the folder: ")
        show_folder_info(folder_path)
    elif choice == '5':
        folder_path = input("Enter the path of the folder to search in: ")
        if not folder_path:
            folder_path = input("Enter the path of the folder to search in: ")
        else:
            file_name = input("Enter the name of the file to search for: ")
            if not file_name:
                file_name = input("Enter the name of the file to search for: ")
            else:    
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
        compress_path = input("Enter the path to Save compress File: ")
        compress_format=input("Enter Compress Format(zip, rar, tar, gz, bz2, xz):")
        compress_level=input("Enter Compress LEVEL(0-9)(except: rar > 0-5 and tar > blank):")
        split_on_size=input("Enter Size Of You Need To Splite(MB):")
        compress_password=input("If You Need Set Password Enter It(Or Not Leave Blank):")
        compress_folder(folder_path,compress_format,compress_level,split_on_size,compress_password,compress_path)
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
        compare_folders()
    elif choice == '13':
        source_path = input("Enter the path of the source file or folder: ")
        link_path = input("Enter the path of the symbolic link: ")
        create_symbolic_link(source_path, link_path)
    elif choice == '0':
         main()
    else:
        print("Invalid choice!")
        
        
def delete_folders():
    clear_screen()
    print(Fore.RED + "\nDelete Folder(s) Menu:")
    print(Fore.YELLOW + "1. Delete all Empty folders")
    print("2. Delete all folders in a directory")
    print("3. Delete folder(s) by name")
    print("0. Back")
    choice = input(Fore.CYAN +"Enter your choice: ")

    if choice == '1':
        folder_path=input("Enter Path:")
        delete_empty_folders_in_path(folder_path)
    elif choice == '2':
        folder_path = input("Enter the path of the directory: ")
        delete_all_folders(folder_path)
    elif choice == '3':
        folder_path=input("Enter Path:")
        folder_names = input("Enter the name(s) of the folder(s) to delete (separated by commas): ")
        delete_folders_by_name(folder_names,folder_path)
    elif choice == '0':
         folder_tools()
    else:
        print("Invalid choice!")




def list_folder_contents(folder_path, indent=''):
    try:
        contents = os.listdir(folder_path)
        print(indent + "Contents of folder:")
        for item in contents:
            item_path = os.path.join(folder_path, item)
            print(indent + "|-- " + item)
            if os.path.isdir(item_path):
                list_folder_contents(item_path, indent + "|   ")
    except FileNotFoundError:
        print(indent + "Folder not found!")
    except PermissionError:
        print(indent + "Permission denied!")
        

def create_random_folder_name(max_length):
    return str(uuid.uuid4())[:max_length]

def create_many_folders(num_folders, max_name_length, folder_path):
    for _ in range(num_folders):
        folder_name = create_random_folder_name(max_name_length)
        create_folder(folder_name, folder_path)

def create_folder(folder_name, folder_path):
    folder_names = folder_name.split(',')
    try:
        for name in folder_names:
            # Validate folder name
            name = name.strip()
            if not name:
                print(f"{Fore.RED}Invalid folder name: '{name}'")
                continue
            
            full_path = os.path.join(folder_path, name)
            if os.path.exists(full_path):
                print(f"{Fore.YELLOW}Folder '{name}' already exists at '{full_path}'!")
                continue
            
            os.makedirs(full_path, exist_ok=True)  # Creates intermediate directories if needed
            print(f"{Fore.GREEN}Folder '{name}' created successfully at '{full_path}'.")
    except Exception as e:
        print(f"{Fore.RED}An error occurred while creating folders: {e}")

        
def delete_empty_folders_in_path(folder_path):
    try:
        # Walk through the directory tree starting from the given folder path
        for root, dirs, files in os.walk(folder_path, topdown=False):
            for directory in dirs:
                folder = os.path.join(root, directory)
                # Check if the folder is empty
                if not os.listdir(folder):
                    # Delete the empty folder
                    os.rmdir(folder)
                    print(f"Deleted empty folder: {folder}")
        print("Empty folders deletion completed successfully.")
    except Exception as e:
        print(f"An error occurred while deleting empty folders: {e}")

def delete_all_folders(folder_path):
    try:
        for item in os.listdir(folder_path):
            item_path = os.path.join(folder_path, item)
            if os.path.isdir(item_path):
                shutil.rmtree(item_path)
        print(f"{Fore.GREEN}All folders deleted successfully.")
    except FileNotFoundError:
        print(f"{Fore.YELLOW}Directory not found!")

def delete_folders_by_name(folder_names, folder_path):
    try:
        for name in folder_names:
            full_path = os.path.join(folder_path, name.strip())
            shutil.rmtree(full_path)
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
    total_size_bytes = get_folder_size(folder_path)
    if total_size_bytes is not None:
        total_size_readable = convert_bytes_to_readable(total_size_bytes)
        print(f"Total Size: {total_size_readable}")
    

def get_last_modified(path):
    try:
        if platform.system() == "Windows":
            last_modified_time = os.path.getmtime(path)
        else:
            stat = os.stat(path)
            last_modified_time = stat.st_mtime
        # Convert Unix timestamp to datetime object
        last_modified_dt = datetime.datetime.fromtimestamp(last_modified_time)
        # Format datetime object as a human-readable string
        last_modified_str = last_modified_dt.strftime('%Y-%m-%d %H:%M:%S')
        return last_modified_str
    except Exception as e:
        print(f"Error: {e}")
        return None

def get_first_modified(path):
    try:
        if platform.system() == "Windows":
            first_modified_time = os.path.getctime(path)
        else:
            stat = os.stat(path)
            first_modified_time = stat.st_mtime
        # Convert Unix timestamp to datetime object
        first_modified_dt = datetime.datetime.fromtimestamp(first_modified_time)
        # Format datetime object as a human-readable string
        first_modified_str = first_modified_dt.strftime('%Y-%m-%d %H:%M:%S')
        return first_modified_str
    except Exception as e:
        print(f"Error: {e}")
        return None
    
def get_folder_size(folder_path):
    total_size = 0
    try:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                total_size += os.path.getsize(file_path)
        return total_size
    except Exception as e:
        print(f"Error: {e}")
        return None

def convert_bytes_to_readable(size_bytes):
    # Define the units
    units = ['bytes', 'KB', 'MB', 'GB', 'TB']
    # Initialize the index and the size
    index = 0
    size = float(size_bytes)
    # Iterate through the units until the size is smaller than 1024
    while size >= 1024 and index < len(units) - 1:
        size /= 1024.0
        index += 1
    # Return the formatted size with the corresponding unit
    return f"{size:.2f} {units[index]}"
    
##################################### FILE TOOLS #####################################


def file_tools():
    clear_screen()
    print(Fore.RED + "\nFile Tools Menu:")
    print(Fore.YELLOW + "1. File Information")
    print("2. File Operations")
    print("3. File Comparison")
    print("4. Search File and Folders")
    print("5. File Compress")
    print("6. File DeCompress")
    print("7. File Encryption")
    print("8. File Decryption")
    print("9. File Permissions")
    print("10. File Hashing")
    print("11. File Conversion")
    print("0. Back")

    choice = input(Fore.CYAN +"Enter your choice: ")
    print(Fore.RESET)
    if choice == '1':
        file_path = input("Enter the path of the file: ")
        view_file_details(file_path)
    elif choice == '2':
        file_operations()
    elif choice == '3':
        file1_path = input("Enter the path of the first file: ")
        file2_path = input("Enter the path of the second file: ")
        compare_files(file1_path, file2_path)
    elif choice == '4':
        folder_path = input("Enter the path of the folder to search in: ")
        file_name = input("Enter the name of the file to search for: ")
        search_for_file(folder_path, file_name)
    elif choice == '5':
        file_path = input("Enter the path of the file to compress: ")
        compress_file(file_path)        
    elif choice == '6':
        file_path = input("Enter the path of the file to decompress: ")
        decompress_file(file_path)        
    elif choice == '7':
        file_path = input("Enter the path of the file to encrypt: ")
        encrypt_file(file_path) 
    elif choice == '8':
        encrypted_file_path = input("Enter the path of the file to decrypt: ")
        key = input("Enter the decryption key: ")
        decrypt_file(encrypted_file_path, key)        
    elif choice == '9':
        folder_path = input("Enter the path of the File to manage permissions and ownership: ")
        manage_permissions_and_ownership(folder_path)        
    elif choice == '10':
        file_path = input("Enter the path of the File: ")
        hash_file(file_path)
    elif choice == '11':
        conversion_tools()
    elif choice == '0':
        main()
    else:
        print("Invalid choice!")

def file_operations():
    clear_screen()
    print(Fore.RED+"\nFile Operations Menu:")
    print(Fore.YELLOW +"1. Copy File")
    print("2. Move File")
    print("3. Rename File")
    print("4. Delete File")
    print("0. Back")

    choice = input("Enter your choice: ")

    if choice == '1':
        source_path = input("Enter the path of the source file: ")
        destination_path = input("Enter the path of the destination file: ")
        copy_file(source_path, destination_path)
    elif choice == '2':
        source_path = input("Enter the path of the source file: ")
        destination_path = input("Enter the path of the destination file: ")
        move_file(source_path, destination_path)
    elif choice == '3':
        file_path = input("Enter the full path of the file to rename: ")
        new_name = input("Enter the new name: ")
        rename_file(file_path, new_name)
    elif choice == '4':
        file_path = input("Enter the path of the file to delete: ")
        delete_file(file_path)
    elif choice == '0':
        file_tools()
    else:
        print("Invalid choice!")


def conversion_tools():
    clear_screen()
    print(Fore.RED+"\nOptions:")
    print(Fore.YELLOW +"1. Convert Photo")
    print("2. Convert Video")
    print("0. Back")
    choice = input("Enter your choice: ")

    if choice == '1':
        input_path = input("Enter the path of the input photo: ")
        output_path = input("Enter the full path of the output photo (including file name and extension): ")
        convert_photo(input_path, output_path)
    elif choice == '2':
        input_path = input("Enter the path of the input video: ")
        output_path = input("Enter the full path of the output video (including file name and extension): ")
        output_format = input("Available output formats for videos: ['mp4', 'avi', 'mov', 'mkv']\nEnter the desired output format: ")
        bitrate_input = input("Enter the desired bitrate (in bits per second), or leave empty for default bitrate: ")
        bitrate = int(bitrate_input) if bitrate_input else None
        convert_video(input_path, output_path, output_format, bitrate)
    elif choice == '0':
        conversion_tools()
    else:
        print("Invalid choice!")




        
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

def search_for_file(folder_path, search_query):
    try:
        found_items = []
        # Convert search query to lowercase for case-insensitive comparison
        search_query_lower = search_query.lower()
        
        for dirpath, dirnames, filenames in os.walk(folder_path):
            # Search for files matching the search query
            for filename in filenames:
                if search_query_lower in filename.lower():
                    found_items.append((os.path.join(dirpath, filename), filename))
            # Search for folders matching the search query
            for dirname in dirnames:
                if search_query_lower in dirname.lower():
                    found_items.append((os.path.join(dirpath, dirname), dirname))
        
        if found_items:
            print("Found items:")
            for item_path, item_name in found_items:
                # Highlight matching parts in the item name
                highlighted_name = re.sub(f'({search_query})', r'\033[1;31m\1\033[0m', item_name, flags=re.IGNORECASE)
                print(f"{item_path}: {highlighted_name}")
        else:
            print("No items found matching the search query.")
    except Exception as e:
        print(f"An error occurred while searching for items: {e}")
        
        

def copy_or_move_files(source_path, destination_path):
    shutil.copytree(source_path, destination_path)
    print("Files copied successfully!")

def rename_file_or_folder(old_name, new_name):
    os.rename(old_name, new_name)
    print(f"{Fore.GREEN}Renamed successfully.")

def compress_folder(folder_path, compress_format, compress_level, split_on_size, compress_password):
    try:
        # Check if the compression format is supported
        supported_formats = ['zip', 'rar', 'tar', 'gz', 'bz2', 'xz']
        if compress_format not in supported_formats:
            raise ValueError(f"Compression format must be one of {supported_formats}.")

        # Construct the archive name
        base_name = os.path.basename(folder_path)
        archive_name = f"{folder_path}.{compress_format}"

        # Compress the folder
        if compress_format == 'zip':
            shutil.make_archive(archive_name, 'zip', folder_path)
        elif compress_format == 'rar':
            raise NotImplementedError("RAR compression is not yet supported.")
        else:
            raise NotImplementedError(f"Compression format '{compress_format}' is not supported yet.")

        print(f"{Fore.GREEN}Folder compressed successfully.")
    except Exception as e:
        print(f"{Fore.RED}Error: {e}")


        

def find_duplicates(folder_path):
    hash_map = {}
    duplicates = []

    for root, _, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            file_hash = hash_file(file_path)
            if file_hash in hash_map:
                duplicates.append((file_path, hash_map[file_hash]))
            else:
                hash_map[file_hash] = file_path

    if duplicates:
        print("Duplicates found:")
        for duplicate in duplicates:
            print(f"Duplicate file: {duplicate[0]}")
            print(f"Original file: {duplicate[1]}")
        choice = input("Do you want to delete the original files? (yes/no): ")
        if choice.lower() == 'yes':
            for duplicate in duplicates:
                os.remove(duplicate[1])
                print(f"Original file '{duplicate[1]}' deleted.")
        else:
            for duplicate in duplicates:
                os.remove(duplicate[0])
                print(f"Duplicate file '{duplicate[0]}' deleted.")
    else:
        print("No duplicates found.")

def hash_file(file_path):
    with open(file_path, 'rb') as f:
        hash_object = hashlib.md5()
        while chunk := f.read(4096):
            hash_object.update(chunk)
        file_hash = hash_object.hexdigest()
    return file_hash

def manage_permissions_and_ownership(folder_path):
    print(Fore.RED+"\nManage Permissions and Ownership:")
    print(Fore.YELLOW +"1. Change permissions of files and folders")
    print("2. Change ownership of files and folders")
    choice = input(Fore.CYAN +"Enter your choice: ")

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
    clear_screen()
    folder1_path = input("Enter the path of the first folder: ")
    folder2_path = input("Enter the path of the second folder: ")

    print("Comparing folders:")
    print(f"Folder 1: {folder1_path}")
    print(f"Folder 2: {folder2_path}")

    if not os.path.isdir(folder1_path):
        print(f"Error: {folder1_path} is not a valid directory.")
        return
    if not os.path.isdir(folder2_path):
        print(f"Error: {folder2_path} is not a valid directory.")
        return

    folder1_contents = set(os.listdir(folder1_path))
    folder2_contents = set(os.listdir(folder2_path))

    files_only_in_folder1 = folder1_contents - folder2_contents
    files_only_in_folder2 = folder2_contents - folder1_contents

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


def create_symbolic_link(source_path, link_path):
    try:
        os.symlink(source_path, link_path)
        print(f"{Fore.GREEN}Symbolic link created successfully.")
    except FileExistsError:
        print(f"{Fore.YELLOW}Symbolic link already exists!")
    except FileNotFoundError:
        print(f"{Fore.YELLOW}Source path not found!")
    except Exception as e:
        print(f"{Fore.RED}An error occurred while creating symbolic link: {e}")
def copy_file(source_path, destination_path):
    try:
        shutil.copy2(source_path, destination_path)
        print("File copied successfully.")
    except FileNotFoundError:
        print("Source file not found!")
    except Exception as e:
        print(f"An error occurred: {e}")

def move_file(source_path, destination_path):
    try:
        shutil.move(source_path, destination_path)
        print("File moved successfully.")
    except FileNotFoundError:
        print("Source file not found!")
    except Exception as e:
        print(f"An error occurred: {e}")

def rename_file(file_path, new_name):
    try:
        directory, old_name = os.path.split(file_path)
        new_file_path = os.path.join(directory, new_name)
        os.rename(file_path, new_file_path)
        print("File renamed successfully.")
    except FileNotFoundError:
        print("File not found!")
    except Exception as e:
        print(f"An error occurred: {e}")
def delete_file(file_path):
    try:
        os.remove(file_path)
        print("File deleted successfully.")
    except FileNotFoundError:
        print("File not found!")
    except Exception as e:
        print(f"An error occurred: {e}")

def compare_files(file1_path, file2_path):
    try:
        # Read the contents of the files
        with open(file1_path, 'r') as file1, open(file2_path, 'r') as file2:
            content1 = file1.read()
            content2 = file2.read()

        # Compare the contents
        if content1 == content2:
            print("The files are identical.")
        else:
            print("The files are different.")
    except FileNotFoundError:
        print("One or both files not found!")
    except Exception as e:
        print(f"An error occurred: {e}")
def compress_file(file_path):
    try:
        with zipfile.ZipFile(file_path + '.zip', 'w', zipfile.ZIP_DEFLATED) as zipf:
            zipf.write(file_path, os.path.basename(file_path))
        print("File compressed successfully.")
    except FileNotFoundError:
        print("File not found!")
    except Exception as e:
        print(f"An error occurred: {e}")

def decompress_file(file_path):
    try:
        with zipfile.ZipFile(file_path, 'r') as zipf:
            zipf.extractall(os.path.dirname(file_path))
        print("File decompressed successfully.")
    except FileNotFoundError:
        print("File not found!")
    except Exception as e:
        print(f"An error occurred: {e}")
def encrypt_file(file_path, key):
    try:
        cipher = Fernet(key)

        with open(file_path, 'rb') as f:
            plaintext = f.read()

        encrypted_text = cipher.encrypt(plaintext)

        with open(file_path + '.enc', 'wb') as f:
            f.write(encrypted_text)

        print("File encrypted successfully.")
    except FileNotFoundError:
        print("File not found!")
    except Exception as e:
        print(f"An error occurred: {e}")


def generate_key():
    """Generate a random Fernet key."""
    return Fernet.generate_key().decode()

def encrypt_file(file_path):
    try:
        # Generate a random key
        key = generate_key()
        cipher = Fernet(key.encode())

        with open(file_path, 'rb') as f:
            plaintext = f.read()

        encrypted_text = cipher.encrypt(plaintext)

        with open(file_path + '.enc', 'wb') as f:
            f.write(encrypted_text)

        print("File encrypted successfully.")
        print(f"Key: {key}")
        print("Please save this key securely. You will need it for decryption.")
    except FileNotFoundError:
        print("File not found!")
    except Exception as e:
        print(f"An error occurred: {e}")


def decrypt_file(encrypted_file_path, key):
    try:
        # Check if the file exists
        if not os.path.exists(encrypted_file_path):
            print("Error: Encrypted file not found!")
            return
        
        # Check if the key is in the correct format
        if len(key) != 44 or not all(c in string.ascii_letters + string.digits + '-_=' for c in key):
            raise ValueError("Invalid key format. The key must be 44 characters long and URL-safe base64-encoded.")

        cipher = Fernet(key.encode())

        # Read the encrypted file
        with open(encrypted_file_path, 'rb') as f:
            encrypted_text = f.read()

        # Decrypt the file
        decrypted_text = cipher.decrypt(encrypted_text)

        # Write the decrypted content to a new file
        decrypted_file_path = encrypted_file_path[:-4]  # Remove the '.enc' extension
        with open(decrypted_file_path, 'wb') as f:
            f.write(decrypted_text)

        print("File decrypted successfully.")
    except ValueError as ve:
        print(f"Error: {ve}")
    except FileNotFoundError:
        print("Error: Encrypted file not found!")
    except Exception as e:
        print("An error occurred during decryption:")
        print(traceback.format_exc())

def hash_file(file_path, algorithm='sha256'):
    try:
        # Create a hash object based on the specified algorithm
        hasher = hashlib.new(algorithm)
        
        # Read the file in binary mode and update the hasher with its content
        with open(file_path, 'rb') as f:
            while chunk := f.read(4096):  # Read the file in chunks to handle large files
                hasher.update(chunk)
        
        # Return the hexadecimal representation of the digest
        return hasher.hexdigest()
    
    except FileNotFoundError:
        print("File not found!")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Supported input and output formats for videos
video_formats = ['mp4', 'avi', 'mov', 'mkv']
video_codecs = ['libx264', 'libvpx', 'mpeg4']

# Supported input and output formats for pictures
picture_formats = ['jpg', 'jpeg', 'png', 'bmp']
picture_codecs = ['libjpeg', 'png']

def convert_photo(input_path, output_path, output_format, codec, compress_output):
    try:
        clip = mp.ImageClip(input_path)
        clip.write_videofile(output_path, codec=codec, fps=1)
        
        if compress_output.lower() == "yes":
            compress_file(output_path)
        
        print("Photo conversion successful!")
    except Exception as e:
        print("An error occurred during photo conversion:", e)



def convert_video(input_path, output_path, output_format, bitrate=None):
    try:
        clip = mp.VideoFileClip(input_path)
        if bitrate:
            clip.write_videofile(output_path, codec='libx264', audio_codec='aac', bitrate=f"{bitrate}k")
        else:
            clip.write_videofile(output_path, codec='libx264', audio_codec='aac')
        print("Video conversion successful!")
    except Exception as e:
        print("An error occurred during video conversion:", e)


##################################### ADMIN TOOLS #####################################




def admin_tools():
    clear_screen()
    print(Fore.RED+"\nAdministrator Tools Menu:")
    print(Fore.YELLOW +"1. Show System Users")
    print("2. Show System Users With Passswords")
    print("3. Add user(s)")
    print("4. Remove user(s)")
    print("5. Remove Keyboard(s)")
    print("6. Driver Status")
    print("7. Run App On Remote")
    print("0. Back")

    choice = input("Enter your choice: ")
    if choice == '1':
        if platform.system() == "Windows":
            show_system_users_windows()
        elif platform.system() == "Linux":
            show_system_users_linux()
        else:
            print("Unsupported operating system")
    elif choice == '2':
        system_users = list_system_users()
        if system_users:
            print("System users:")
            for user in system_users:
                print(user)
        else:
            print("No system users found.")
    elif choice == '3':
         usernumber = input('Set Number of users need to Create: ')
         if usernumber == '1':
            add_single_user()
         else:
            add_multiple_users(usernumber)
    elif choice == '4':
            print(Fore.RED+"\nChoose Your Options:")
            print(Fore.YELLOW +"1. Delete Special User")
            print("2. Delete All Users")
            choice=input('Enter your choice: ')
            if choice=='1':
                username=input("Enter Username To Delete: ")
                delete_user(username)
            elif choice=='2':
                deleted_users = delete_all_users_except_current()
                print("Deleted users:", deleted_users)
            else:
                print(Fore.RED+'Wrong Choice!!')
    elif choice == '5':
        layouts = list_keyboard_layouts()
        print("List of keyboard layout IDs:")
        for i, layout_id in enumerate(layouts):
            print(f"{i+1}. {layout_id}")

        current_layout = win32api.GetKeyboardLayout()
        print(f"Current keyboard layout ID: {current_layout}")

        choice = input("Enter the number of the layout you want to delete (0 to cancel): ")
        if choice.isdigit():
            choice = int(choice)
            if 0 < choice <= len(layouts):
                layout_id = layouts[choice - 1]
                if layout_id == current_layout:
                    print("Cannot delete the currently active keyboard layout.")
                else:
                    delete_keyboard_layout(layout_id)
                    delete_layout_from_registry(layout_id)
            elif choice == 0:
                print("Operation canceled.")
                admin_tools()
            else:
                print("Invalid choice.")
        else:
            print("Invalid input. Please enter a number.")
    elif choice == '6':
            print(show_not_installed_drivers())
    elif choice == '7':
            remote_pc_ip=input("Enter Target Ip Address:")
            app_path=app_selection()
            run_app_on_remote_pc(remote_pc_ip, app_path)
    elif choice == '0':
        main()
    else:
        print(Fore.RED+"Invalid choice...")

def app_selection():
    print(Fore.RED + "Select Your APP To Open On Target:")
    print(Fore.RESET + "1. Rust Desk")
    print("2. ....")
    print("3. Custom Path")
    clear_screen()
    
    rust_path = r"C:\Program Files\RustDesk\rustdesk.exe"  # Path to Rust Desk application
    print("What app You need to Open On Target?")
    print("1. RustDesk")
    print("3. Custom app Path")
    choice = input("Enter Your Choice: ")
    if choice == "1":
        return rust_path
    # Add other options here if needed
    elif choice == "3":
        custom_path = input("Enter the custom path Of application: ")
        return custom_path
    else:
        print("Invalid choice. Please try again.")
        return None

    


def show_system_users_windows():
    os.system("net user")

def show_system_users_linux():
    with open("/etc/passwd", "r") as passwd_file:
        for line in passwd_file:
            username = line.split(":")[0]
            print(username)
            
def list_system_users():
    users = []
    system = platform.system()
    if system == "Windows":
        import ctypes
        import ctypes.wintypes

        advapi32 = ctypes.WinDLL('advapi32')
        buf_size = ctypes.wintypes.DWORD(1024)
        buf = ctypes.create_unicode_buffer(buf_size.value)
        advapi32.GetUserNameW(buf, ctypes.byref(buf_size))
        users.append(buf.value)
        print(Fore.RED+"Showing password for windows users NOT supported")
    elif system == "Linux":
        import pwd
        users = [user.pw_name for user in pwd.getpwall()]
    else:
        print("Unsupported platform.")
    return users

def get_user_list():
    if platform.system() == "Windows":
        output = os.popen("net user").read()
        users = [line.split()[0] for line in output.splitlines()[4:] if line.strip()]
    elif platform.system() == "Linux":
        output = os.popen("cut -d: -f1 /etc/passwd").read()
        users = output.splitlines()
    else:
        print("Unsupported operating system.")
        users = []
    return users


        
def get_current_username():
    return getpass.getuser()

def delete_all_users_except_current():
    current_user = get_current_username()
    users = get_user_list()
    if users is None:
        print("Error: Unable to retrieve user list.")
        return
    deleted_users = []
    for user in users:
        if user != current_user:
            delete_user(user)
            deleted_users.append(user)
    return deleted_users
    
        
def add_single_user():
    if platform.system() == "Windows":
        username = input("Enter Username: ")
        password = input("Enter Password: ")
        add_user_windows(username, password)
    elif platform.system() == "Linux":
        username = input("Enter Username: ")
        password = input("Enter Password: ")
        add_user_linux(username, password)
    else:
        print("Unsupported operating system")

def add_multiple_users(usernumber):
    try:
        usernumber = int(usernumber)
        if usernumber <= 0:
            print("Invalid number of users.")
            return
        usernames = generate_random_username(usernumber)
        for username in usernames:
            password = generate_random_password()
            if platform.system() == "Windows":
                add_user_windows(username, password)
            elif platform.system() == "Linux":
                add_user_linux(username, password)
            else:
                print("Unsupported operating system")
        print("Generated", usernumber, "unique usernames.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")




def add_user_windows(username, password):
    subprocess.run(["net", "user", username, password, "/add", "/active:yes"], shell=True)



def add_user_linux(username, password):
    os.system(f"sudo useradd -m {username} -p {password}")

def generate_random_username(usernumber, username_length=8):
    usernames = set()
    usernumber = int(usernumber)  # Convert to integer

    while len(usernames) < usernumber:
        username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=username_length))
        usernames.add(username)
    return list(usernames)

def generate_random_password(length=12, complexity=3):
    lowercase_chars = string.ascii_lowercase
    uppercase_chars = string.ascii_uppercase
    digit_chars = string.digits
    special_chars = string.punctuation
    complexity = min(complexity, 4)
    password_chars = [random.choice(lowercase_chars),
                      random.choice(uppercase_chars),
                      random.choice(digit_chars)]
    if complexity == 4:
        password_chars.append(random.choice(special_chars))

    password_chars.extend(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(length - complexity))

    random.shuffle(password_chars)

    password = ''.join(password_chars)

    return password

def delete_user(username):
    if platform.system() == "Windows":
        command = f"net user {username} /delete"
    elif platform.system() == "Linux":
        command = f"sudo userdel -r {username}"
    else:
        print("Unsupported operating system.")
        return

    print(f"Executing command: {command}")
    try:
        os.system(command)
        print(f"User '{username}' deleted successfully.")
    except Exception as e:
        print(f"Error deleting user '{username}': {e}")


def list_keyboard_layouts():
    layouts = win32api.GetKeyboardLayoutList()
    return layouts


def delete_keyboard_layout(layout_id):
    if layout_id < 0:
        print("Cannot delete special keyboard layout.")
        return
    user32 = ctypes.windll.user32
    user32.UnloadKeyboardLayout(layout_id)
    print(f"Keyboard layout {layout_id} deleted successfully.")


def delete_layout_from_registry(layout_id):
    key_path = r"SYSTEM\CurrentControlSet\Control\Keyboard Layouts"
    try:
        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key_path, 0, winreg.KEY_ALL_ACCESS) as key:
            winreg.DeleteKey(key, str(layout_id))
            print(f"Keyboard layout '{layout_id}' deleted successfully from registry.")
    except FileNotFoundError:
        print(f"Keyboard layout '{layout_id}' not found in registry.")
    except PermissionError:
        print("Error: Permission denied. Please run the script with administrative privileges.")


def show_not_installed_drivers():
    system = platform.system()
    if system == "Windows":
        try:
            installed_drivers_output = subprocess.check_output(['pnputil', '-e']).decode('utf-8')
            installed_drivers = [line.strip() for line in installed_drivers_output.split('\n') if line.strip()]
            known_drivers = ["Driver1", "Driver2", "Driver3"]  # Add your list of known drivers here
            not_installed_drivers = [driver for driver in known_drivers if driver not in installed_drivers]
            
            if not_installed_drivers:
                output = subprocess.check_output(['wmic', 'path', 'win32_pnpentity', 'get', 'caption']).decode('utf-8')
                device_names = [line.strip() for line in output.split('\n') if line.strip()]
                return [name for name in device_names if any(driver in name for driver in not_installed_drivers)]
            else:
                return "All drivers are installed."
        except subprocess.CalledProcessError as e:
            return f"Error: {e}"
    elif system == "Linux":
        try:
            installed_drivers_output = subprocess.check_output(['lsmod']).decode('utf-8')
            installed_drivers = [line.split()[0] for line in installed_drivers_output.split('\n')[1:] if line.strip()]
            known_drivers = ["Driver1", "Driver2", "Driver3"]  # Add your list of known drivers here
            not_installed_drivers = [driver for driver in known_drivers if driver not in installed_drivers]
            
            if not_installed_drivers:
                output = subprocess.check_output(['lsusb']).decode('utf-8')
                device_names = [line.split(':')[1].strip() for line in output.split('\n') if line.strip()]
                return [name for name in device_names if any(driver in name for driver in not_installed_drivers)]
            else:
                return "All drivers are installed."
        except subprocess.CalledProcessError as e:
            return f"Error: {e}"
    else:
        return "Unsupported operating system."

def run_app_on_remote_pc(remote_pc_ip, app_path):
    system = platform.system()
    if system == "Windows":
        try:
            subprocess.run(['powershell', '-Command', f'Invoke-Command -ComputerName {remote_pc_ip} -ScriptBlock {{ Start-Process -FilePath "{app_path}" }}'], check=True)
            return "Application started successfully on the remote PC."
        except subprocess.CalledProcessError as e:
            return f"Error: {e}"
    elif system == "Linux":
        try:
            subprocess.run(['ssh', f'user@{remote_pc_ip}', f'nohup {app_path} &'], check=True)
            return "Application started successfully on the remote PC."
        except subprocess.CalledProcessError as e:
            return f"Error: {e}"
    else:
        return "Unsupported operating system."

##################################### MONITOR TOOLS #####################################




def monitor_tools():
         clear_screen()
         print(Fore.RED+"\nMonitoring Tools Menu:")
         print(Fore.YELLOW +"1. Show Task Manager")
         print("2. Show Hardware Usage")
         print("3. Show System info")
         print("0. Back")
         choice=input("Enter Your Choice:")
         if choice=='1':
             display_processes()
         elif choice=='2':
             display_hardware_usage()
         elif choice=='3':
             display_system_info()
         elif choice=='0':
             main()
         else:
             print(Fore.RED+"Invalid choice...")
             
def display_processes():
    clear_screen()
    if platform.system() == 'Windows':
        subprocess.call('tasklist', shell=True)
    elif platform.system() == 'Linux':
        subprocess.call('ps aux', shell=True)
    else:
        print("Unsupported operating system")
    close_task_list()
        
def display_hardware_usage():
    clear_screen()
    print("CPU Usage: {}%".format(psutil.cpu_percent(interval=1)))
    print("Memory Usage: {}%".format(psutil.virtual_memory().percent))

    if platform.system() == 'Windows':
        print("Disk Usage:")
        for disk in psutil.disk_partitions():
            try:
                usage = psutil.disk_usage(disk.mountpoint)
                print(f"{disk.device} - Total: {usage.total / (1024 ** 3):.2f} GB, "
                      f"Used: {usage.used / (1024 ** 3):.2f} GB, "
                      f"Free: {usage.free / (1024 ** 3):.2f} GB")
            except PermissionError:
                continue
    elif platform.system() == 'Linux':
        print("Disk Usage:")
        disk_usage = psutil.disk_usage('/')
        print(f"Total: {disk_usage.total / (1024 ** 3):.2f} GB, "
              f"Used: {disk_usage.used / (1024 ** 3):.2f} GB, "
              f"Free: {disk_usage.free / (1024 ** 3):.2f} GB")
        
def display_system_info():
    clear_screen()
    print("System Information:")
    print(f"Operating System: {platform.system()} {platform.release()} {platform.version()}")
    print(f"Machine: {platform.machine()}")
    print(f"Processor: {platform.processor()}")
    print("\nCPU Usage:")
    print(f"  Cores: {psutil.cpu_count(logical=False)} (Physical)")
    print(f"  Threads: {psutil.cpu_count(logical=True)} (Logical)")
    print(f"  Usage: {psutil.cpu_percent(interval=1)}%")
    print("\nMemory Usage:")
    memory = psutil.virtual_memory()
    print(f"  Total: {memory.total / (1024 ** 3):.2f} GB")
    print(f"  Available: {memory.available / (1024 ** 3):.2f} GB")
    print(f"  Used: {memory.used / (1024 ** 3):.2f} GB ({memory.percent}%)")
    print(f"  Free: {memory.free / (1024 ** 3):.2f} GB")
    print("\nDisk Usage:")
    for partition in psutil.disk_partitions():
        try:
            partition_usage = psutil.disk_usage(partition.mountpoint)
            print(f"  Device: {partition.device}")
            print(f"    Mountpoint: {partition.mountpoint}")
            print(f"    Total: {partition_usage.total / (1024 ** 3):.2f} GB")
            print(f"    Used: {partition_usage.used / (1024 ** 3):.2f} GB ({partition_usage.percent}%)")
            print(f"    Free: {partition_usage.free / (1024 ** 3):.2f} GB")
        except PermissionError:
            continue
    print("\nNetwork Information:")
    print("  Network Interfaces:")
    for interface, addrs in psutil.net_if_addrs().items():
        print(f"    Interface: {interface}")
        for addr in addrs:
            print(f"      {addr.family.name}: {addr.address}")
            

               
def close_task_list():
    print(Fore.BLUE+"Did You want to Clear Process?")
    choice=input("Enter (Y) to Clear All Or (N) to Cancell: ")
    if choice=="y"or"Y":
        end_all_tasks()
    elif choice=="N"or"n":
        monitor_tools()
    else:
        print("incorrect!")           
        close_task_list()
        
def end_all_tasks():
    system = platform.system()
    if system == "Windows":
        try:
            subprocess.run(["taskkill", "/F", "/FI", "USERNAME ne SYSTEM"])
            print("All tasks terminated except system tasks.")
        except subprocess.CalledProcessError:
            print("Error: Failed to terminate tasks.")
    elif system == "Linux":
        try:
            subprocess.run(["sudo", "pkill", "-u", "$(whoami)"])
            print("All tasks terminated except system tasks.")
        except subprocess.CalledProcessError:
            print("Error: Failed to terminate tasks.")
    else:
        print("Unsupported platform.")
##################################### NETWORK TOOLS #####################################



def network_tools():
    clear_screen()
    print(Fore.RED+"\nNetwork Tools Menu:")
    print(Fore.YELLOW +"1. Show Network Connection")
    print("2.  Scan Open Ports")
    print("3.  Network Scaner")
    print("4.  Send Magic Packet")
    print("5.  Test Client With UDP Packet")
    print("6.  Test Client With TCP Packet ")
    print("7.  FireWall Status")
    print("8.  Speed Test")
    print("9.  Find Computer and User info")
    print("10. Routing")
    print("0.  Back")
    choice=input("Enter Your Choice:")
    if choice=='1':
        Network_connections()
    elif choice=='2':
        scan_open_ports()
    elif choice=='3':
        subnet, ip_range = get_user_input_network_scaner()
        scan_network(ip_range, subnet)
        print("\nScanning Complete!")
    elif choice=='5':
            target_ip = input("Enter target IP address: ")
            target_port = int(input("Enter target port number: "))
            message = input("Enter message to send: ")
            num_packets = int(input("Enter number of packets to send: "))
            num_threads = int(input("Enter number of threads: "))
            send_udp_packets(target_ip, target_port, message, num_packets, num_threads)
    elif choice=='4':
        mac_address, broadcast_address = get_user_input_magic_packet()
        send_magic_packet(mac_address, broadcast_address)
        print("Magic packet sent successfully!")
    elif choice=='6':
        ping_with_progress()
    elif choice=='7':
        fire_walls()
    elif choice=='8':
        run_speed_test_menu()
    elif choice=='9':
        ip_address = input("Enter IP Address: ")
        computer_name = get_hostname_from_ip(ip_address)
        if computer_name:
            print(f"Computer name: {computer_name}")
            usernames = get_user_by_computer_name(computer_name)
            if usernames:
                print(f"User(s) associated with computer {computer_name}: {', '.join(usernames)}")
            else:
                print(f"No user found for computer {computer_name}")
        else:
            print(f"Unable to retrieve computer name for IP {ip_address}")
    elif choice=='10':
        route_options()
        
    elif choice=='0':
        main()
    else:
        print(Fore.RED+"Invalid choice...")


def route_options():
    print(Fore.RED+"\nRoute Tools Menu:")
    print(Fore.YELLOW +"1. Show Route Table")
    print("2.  Add Route")      
    print("3.  Delete Route")    
    choice=input("Enter Your Choice:")
    if choice=='1':
        route_table = get_route_table()
        display_route_table(route_table)
    elif choice=='2':
        destination = input("Enter Destination IP: ")
        gateway = input("Enter Gateway IP: ")
        add_route(destination, gateway)  
    elif choice=='3':
        route_table = get_route_table()
        display_route_table(route_table)
        row_number = int(input("Enter the row number of the route to delete: "))
        delete_route(route_table, row_number)
    
    
def scan_open_ports():
    clear_screen()
    print(Fore.RED+"\nScan Port Tools Menu:")
    print(Fore.YELLOW +"1. Scan On Current Machine")
    print("2. Scan On Special IP")
    print("0. Back")
    choice=input("Enter Your Choice:")
    if choice=='1':
        display_open_ports_with_app()
    elif choice=='2':
        ip_address, port_range = get_user_input_port_scan()
        open_ports = get_open_ports(ip_address, port_range)
        print("Open ports:", open_ports)
    elif choice=='0':
        main()
    else:
        print(Fore.RED+"Invalid choice...")
        
def fire_walls():
    clear_screen()
    print(Fore.RED+"\nFireWall Menu:") 
    print(Fore.WHITE +"1. Firewall Status")
    print("2. Disable Firewall")
    print("3. Enable Firewall")
    print("0. Back")  
    choice=input("Enter Your Choice: ")
    if choice=='1':
        print(status_firewall())
    elif choice=='2':
        print(disable_firewall())
    elif choice=='3':
        print(enable_firewall())
    else:
        print(Fore.RED+"Invalid choice...")

def run_speed_test_menu():
    clear_screen()
    print(Fore.RED+"\nSpeed Test Menu:") 
    print(Fore.WHITE +"1. Internet Speed")
    print("2. Special Distanation Speed")
    print("3. Local Server Connection")
    print("0. Back")  
    choice=input("Enter Your Choice: ")
    if choice=='1':
        run_speed_test()
    elif choice=='2':
        server_ip = input("Enter Your Destination IP: ")
        run_network_speed_test(server_ip)
    elif choice=='3':
        run_traceroute("172.16.20.34")
    elif choice=='0':
        network_tools()
    else:
        print(Fore.RED+"Invalid choice...")
        
        
def Network_connections():
    print("\n  Network Connections:")
    for conn in psutil.net_connections(kind='inet'):
        laddr = f"{conn.laddr.ip}:{conn.laddr.port}" if conn.laddr else "N/A"
        raddr = f"{conn.raddr.ip}:{conn.raddr.port}" if conn.raddr else "N/A"
        print(f"    {laddr} --> {raddr} [{conn.status}]")





def display_progress_bar(percent):
    bar_length = 40
    progress = int(percent * bar_length)
    remaining = bar_length - progress
    bar = f"\033[32m{'█' * progress}\033[0m\033[31m{'-' * remaining}\033[0m"
    print(f"Scanning : [{bar}] {int(percent * 100)}%", end='\r')

def get_open_ports_with_app():
    open_ports_with_app = {}
    total_ports = 65535  # Total number of ports to scan
    for i, port in enumerate(range(1, total_ports + 1), 1):
        percent = i / total_ports
        display_progress_bar(percent)
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(0.1)  # Adjust timeout as needed
                s.connect(("127.0.0.1", port))
            if platform.system() == "Windows":
                connections = psutil.net_connections(kind='inet')
                for conn in connections:
                    if conn.laddr.port == port:
                        process = psutil.Process(conn.pid)
                        open_ports_with_app[port] = process.name()
            else:  # Assume Unix-like system
                process = psutil.Process(psutil.net_connections()[0].pid)
                open_ports_with_app[port] = process.name()
        except Exception as e:
            pass
    print()  # Move to the next line after progress bar
    return open_ports_with_app

# Display open ports and the corresponding applications
def display_open_ports_with_app():
    open_ports_with_app = get_open_ports_with_app()
    print("Open Ports:")
    for port, app in open_ports_with_app.items():
        print(f"Port {port} is being used by {app}")





def get_open_ports(ip_address, port_range):
    open_ports = []
    total_ports = port_range[1] - port_range[0] + 1
    progress = 0
    for port in range(port_range[0], port_range[1] + 1):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(0.1)  # Adjust timeout as needed
                s.connect((ip_address, port))
            open_ports.append(port)
        except:
            pass
        progress += 1
        percent = progress / total_ports
        display_progress_bar(percent)
    sys.stdout.write("\n")
    return open_ports

def get_user_input_port_scan():
    ip_address = input("Enter the IP address to scan: ")
    start_port = int(input("Enter the starting port: "))
    end_port = int(input("Enter the ending port: "))
    port_range = (start_port, end_port)
    return ip_address, port_range

RED = "\033[91m"
GREEN = "\033[92m"
RESET = "\033[0m"

def check_host_status(ip):
    result = subprocess.run(['ping', '-c', '1', ip], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    if result.returncode == 0:
        return True  # Host is online
    else:
        return False  # Host is offline

# Scan network function
def scan_network(ip_range, subnet):
    total_ips = ip_range[1] - ip_range[0] + 1
    progress = 0
    online_hosts = []
    offline_hosts = []

    for i in range(ip_range[0], ip_range[1] + 1):
        ip = f"{subnet}.{i}"
        online = check_host_status(ip)
        if online:
            status = f"{GREEN}Online{RESET}"
            try:
                hostname = socket.gethostbyaddr(ip)[0]
            except (socket.herror, socket.gaierror):
                hostname = "N/A"
            online_hosts.append((ip, hostname))
        else:
            status = f"{RED}Offline{RESET}"
            hostname = "N/A"
            offline_hosts.append(ip)

        os_info = platform.system()
        progress += 1
        percent = (progress / total_ips)
        display_progress_bar(percent)

    print("\n\nOnline hosts:")
    for host in online_hosts:
        print(f"IP: {host[0]}, Hostname: {host[1]}")

    print("\nOffline hosts:")
    for host in offline_hosts:
        print(f"IP: {host}, Status: Offline")


def get_user_input_network_scaner():
    subnet = input("Enter the subnet (e.g., 192.168.1): ")
    start_ip = int(input("Enter the starting IP address (e.g., 1): "))
    end_ip = int(input("Enter the ending IP address (e.g., 254): "))
    ip_range = (start_ip, end_ip)
    return subnet, ip_range



def send_magic_packet(mac_address, broadcast_address, port=9):
    # Clean up MAC address string
    mac_address = mac_address.replace('-', ':')

    # Construct magic packet
    mac_bytes = bytearray.fromhex(mac_address.replace(':', ''))
    magic_packet = b'\xff' * 6 + mac_bytes * 16

    # Create UDP socket
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        # Enable broadcast mode
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        # Send magic packet
        sock.sendto(magic_packet, (broadcast_address, port))

def get_user_input_magic_packet():
    mac_address = input("Enter the MAC address of the target device (format: XX:XX:XX:XX:XX:XX): ")
    broadcast_address = input("Enter the broadcast address of the target network (e.g., 192.168.1.255): ")
    return mac_address, broadcast_address


def send_udp_packets(target_ip, target_port, message, num_packets, num_threads):
    # Create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Function for each thread to send UDP packets
    def send_packets(thread_num, progress_bar):
        for _ in range(num_packets):
            packet = message.encode('utf-8')
            sock.sendto(packet, (target_ip, target_port))
            progress_bar.update(1)

    progress_bars = [tqdm(total=num_packets, desc=f"Thread {i+1}") for i in range(num_threads)]

    threads = []
    for i in range(num_threads):
        progress_bar = progress_bars[i]
        thread = threading.Thread(target=send_packets, args=(i+1, progress_bar))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
    sock.close()
    for bar in progress_bars:
        bar.close()


def ping_target(ip, num_pings, ttl, progress_bar):
    if platform.system() == "Windows":
        command = ["ping", "-n", str(num_pings), "-i", str(ttl), ip]
    else:
        command = ["ping", "-c", str(num_pings), "-i", str(ttl), ip]

    print(f"Running command: {' '.join(command)}")  

    for _ in range(num_pings):
        result = subprocess.run(command)
        print("Ping result:", result)  
        progress_bar.update(1)

def get_user_input_down_tcp():
    ip_address = input("Enter the target IP address: ")
    num_pings = int(input("Enter the number of pings: "))
    num_threads = int(input("Enter the number of threads: "))
    ttl = int(input("Enter the Time To Live (TTL) value: "))
    return ip_address, num_pings, num_threads, ttl

def ping_with_progress():
    ip_address, num_pings, num_threads, ttl = get_user_input_down_tcp()
    progress_bars = [tqdm(total=num_pings, desc=f"Thread {i+1}") for i in range(num_threads)]

    threads = []
    for i in range(num_threads):
        progress_bar = progress_bars[i]
        thread = threading.Thread(target=ping_target, args=(ip_address, num_pings, ttl, progress_bar))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    for bar in progress_bars:
        bar.close()

    print("Ping operation completed")
    


def status_firewall():
        system = platform.system()
        if system == "Windows":
            try:
                output = subprocess.check_output(['netsh', 'advfirewall', 'show', 'allprofiles', 'state'])
                output = output.decode('utf-8')
                return output
            except subprocess.CalledProcessError as e:
                return f"Error: {e}"
        elif system == "Linux":
            try:
                output = subprocess.check_output(['ufw', 'status'])
                output = output.decode('utf-8')
                return output
            except subprocess.CalledProcessError as e:
                return f"Error: {e}"
        else:
            return "Unsupported operating system"


def enable_firewall():
    system = platform.system()
    if system == "Windows":
        try:
            subprocess.run(['netsh', 'advfirewall', 'set', 'allprofiles', 'state', 'on'], check=True)
            return "Firewall enabled successfully on Windows."
        except subprocess.CalledProcessError as e:
            return f"Error: {e}"
    elif system == "Linux":
        try:
            subprocess.run(['ufw', 'enable'], check=True)
            return "Firewall enabled successfully on Linux."
        except subprocess.CalledProcessError as e:
            return f"Error: {e}"
    else:
        return "Unsupported operating system."


def disable_firewall():
    system = platform.system()
    if system == "Windows":
        try:
            subprocess.run(['netsh', 'advfirewall', 'set', 'allprofiles', 'state', 'off'], check=True)
            return "Firewall disabled successfully on Windows."
        except subprocess.CalledProcessError as e:
            return f"Error: {e}"
    elif system == "Linux":
        try:
            subprocess.run(['ufw', 'disable'], check=True)
            return "Firewall disabled successfully on Linux."
        except subprocess.CalledProcessError as e:
            return f"Error: {e}"
    else:
        return "Unsupported operating system."
    
           
def run_speed_test():
    st = speedtest.Speedtest()
    
    print("Running download speed test...")
    download_speed = st.download() / 1_000_000  # Convert to Mbps
    print("Download speed: {:.2f} Mbps".format(download_speed))
    
    print("Running upload speed test...")
    upload_speed = st.upload() / 1_000_000  # Convert to Mbps
    print("Upload speed: {:.2f} Mbps".format(upload_speed))  
        
        
        
def run_network_speed_test(server_ip):
    client = iperf3.Client()
    client.duration = 10  # Duration of the test in seconds
    client.server_hostname = server_ip
    
    print("Running network speed test to", server_ip)
    result = client.run()
    
    if result.error:
        print("Error:", result.error)
    else:
        print("Download speed: {:.2f} Mbps".format(result.sent_Mbps))
        print("Upload speed: {:.2f} Mbps".format(result.received_Mbps))


def run_traceroute(destination):
    if platform.system() == 'Windows':
        # Use tracert on Windows
        command = ['tracert', '-d', destination]
    else:
        # Use traceroute on Unix-based systems
        command = ['traceroute', '-n', destination]
    
    result = subprocess.run(command, capture_output=True, text=True)
    
    if result.returncode == 0:
        print(result.stdout)
    else:
        print("Error:", result.stderr)  
        
        
        
def get_hostname_from_ip(ip_address):
    try:
        if platform.system() == "Windows":
            result = subprocess.run(['nslookup', ip_address], capture_output=True, text=True)
            if result.returncode == 0:
                lines = result.stdout.split('\n')
                for line in lines:
                    if 'Name:' in line:
                        return line.split(':')[1].strip()
        else:
            result = subprocess.run(['host', ip_address], capture_output=True, text=True)
            if result.returncode == 0:
                lines = result.stdout.split('\n')
                return lines[0].split(' ')[-1].strip('.')
        return None
    except Exception as e:
        print(f"Error retrieving hostname: {e}")
        return None

def get_user_by_computer_name(computer_name):
    server = Server('ldap://ldap:port')
    with Connection(server, user='X', password='X') as conn: # Update with your domain information
        try:
            if not conn.bind():
                print("LDAP bind failed. Check username and password.")
                return []

            conn.search(
                search_base='OU=X.local,DC=X,DC=local',  # Update with your domain information
                search_filter=f'(&(objectCategory=computer)(sAMAccountName={computer_name}$))',
                attributes=['memberOf'],
                search_scope=SUBTREE
            )
            response = conn.response
            if response:
                computer_dn = response[0]['dn']
                conn.search(
                    search_base='OU=X.local,DC=X,DC=local',  # Update with your domain information
                    search_filter=f'(&(objectCategory=person)(objectClass=user)(memberOf={computer_dn}))',
                    attributes=['sAMAccountName'],
                    search_scope=SUBTREE
                )
                if conn.entries:
                    usernames = [entry.sAMAccountName.value for entry in conn.entries]
                    return usernames
                else:
                    return []
            else:
                return []
        except Exception as e:
            print(f"LDAP connection error: {e}")
            return []


    
def add_route(destination, gateway):
    try:
        # Determine the appropriate command based on the operating system
        if platform.system() == "Windows":
            command = f"route add {destination} mask 255.255.255.255 {gateway}"
        elif platform.system() == "Linux":
            command = f"route add -host {destination} gw {gateway}"
        else:
            print("Unsupported platform.")
            return

        # Execute the command
        subprocess.run(command, shell=True, check=True)
        print("Route added successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error adding route: {e}")
   

def get_route_table():
    route_table = []
    system = platform.system()
    if system == "Linux":
        try:
            # Run ip route command to get the route table information
            output = subprocess.check_output(["ip", "route"]).decode("utf-8")
            # Parse the output to extract route table information
            lines = output.split("\n")
            for line in lines:
                parts = line.split()
                if len(parts) >= 3:
                    destination = parts[0]
                    gateway = parts[2]
                    interface = parts[3] if len(parts) > 3 else ""
                    route_table.append((destination, gateway, interface))
        except subprocess.CalledProcessError:
            print("Error: Failed to retrieve route table information on Linux.")
    elif system == "Windows":
        try:
            # Run route print command to get the route table information
            output = subprocess.check_output(["route", "print"]).decode("utf-8")
            # Parse the output to extract route table information
            lines = output.split("\n")
            for line in lines[4:-2]:  # Skip the header and footer lines
                parts = line.split()
                if len(parts) >= 4:
                    destination = parts[0]
                    gateway = parts[2]
                    interface = parts[3]
                    route_table.append((destination, gateway, interface))
        except subprocess.CalledProcessError:
            print("Error: Failed to retrieve route table information on Windows.")
    else:
        print("Unsupported platform.")
    return route_table

def display_route_table(route_table):
    if route_table:
        print("Route Table:")
        for i, (destination, gateway, interface) in enumerate(route_table, start=1):
            print(f"{i}. Destination: {destination}, Gateway: {gateway}, Interface: {interface}")
    else:
        print("No route table information available.")

def delete_route(route_table, row_number):
    if row_number < 1 or row_number > len(route_table):
        print("Error: Invalid row number.")
        return False
    entry = route_table[row_number - 1]
    destination = entry[0]
    system = platform.system()
    if system == "Linux":
        try:
            subprocess.run(["sudo", "ip", "route", "del", destination])
            print(f"Route with destination {destination} deleted successfully.")
            return True
        except subprocess.CalledProcessError:
            print(f"Error: Failed to delete route with destination {destination}.")
            return False
    elif system == "Windows":
        try:
            subprocess.run(["route", "delete", destination])
            print(f"Route with destination {destination} deleted successfully.")
            return True
        except subprocess.CalledProcessError:
            print(f"Error: Failed to delete route with destination {destination}.")
            return False
    else:
        print("Unsupported platform.")
        return False



 ##################################### MAIN  #####################################
   

def clear_screen():
    if platform.system() == "Windows":
        import os
        os.system("cls")
    else:
        subprocess.call("clear", shell=True)
        
        
def main():
    clear_screen()
    while True:
        print(Fore.GREEN+"db   db  .d8b.  d8b   db d8888b. db    db      d888888b  .d88b.   .d88b.  db      .d8888. ")
        print(Fore.GREEN+"88   88 d8' `8b 888o  88 88  `8D `8b  d8'      `~~88~~' .8P  Y8. .8P  Y8. 88      88'  YP ")
        print(Fore.GREEN+"88ooo88 88ooo88 88V8o 88 88   88  `8bd8'          88    88    88 88    88 88      `8bo.   ")
        print(Fore.GREEN+"88~~~88 88~~~88 88 V8o88 88   88    88            88    88    88 88    88 88        `Y8b. ")
        print(Fore.GREEN+"88   88 88   88 88  V888 88  .8D    88            88    `8b  d8' `8b  d8' 88booo. db   8D ")
        print(Fore.GREEN+"YP   YP YP   YP VP   V8P Y8888D'    YP            YP     `Y88P'   `Y88P'  Y88888P `8888Y' ")
        print(Fore.RED+"By HamidReza")
        print(Style.RESET_ALL + Fore.RED + "\nMain Menu:")
        print(Fore.WHITE + "1. Folder Tools")
        print("2. File Tools")
        print("3. Admin Tools")
        print("4. Monitor Tools")
        print("5. Network Tools")
        print("0. Exit")
        choice = input(Fore.CYAN + "Enter your choice: ")

        if choice == '1':
            folder_tools()
        elif choice == '2':
            file_tools()
        elif choice == '3':
            admin_tools()
        elif choice == '4':
            monitor_tools()
        elif choice == '5':
            network_tools()
        elif choice == '0':
            print(Fore.GREEN + "Exiting the program. Goodbye!")
            print(Style.RESET_ALL)
            break
        else:
            print("Invalid choice!")




def ldap_login(username, password):
    # Modify the LDAP server details accordingly
    ldap_server = Server('ldap://ldap:port', get_info=ALL)
    # Replace the base_dn with your LDAP base DN
    base_dn = 'OU=X,,DC=X'
    # Replace the search_filter with your LDAP search filter
    search_filter = '(sAMAccountName={})'.format(username)

    try:
        # Attempt to bind to the LDAP server
        conn = Connection(ldap_server, user='{}@X.local'.format(username), password=password, authentication=SIMPLE)
        if not conn.bind():
            print(Fore.RED + "LDAP login failed: Invalid credentials")
            return False

        # Search for the user in LDAP
        conn.search(search_base=base_dn, search_filter=search_filter, attributes=['cn'])
        if not conn.entries:
            print(Fore.RED + "LDAP login failed: User not found")
            return False

        print(Fore.GREEN + "LDAP login successful!")
        return True

    except Exception as e:
        print(Fore.RED + "An error occurred during LDAP authentication:", e)
        return False

def clear_screen():
    if platform.system() == "Windows":
        import os
        os.system("cls")
    else:
        import subprocess
        subprocess.call("clear", shell=True)

def get_password(prompt='Enter your password: '):
    if platform.system() == 'Windows':
        password = ''
        print(prompt, end='', flush=True)
        while True:
            char = msvcrt.getch()
            if char == b'\r':
                print()
                break
            elif char == b'\x08':  # Backspace
                if password:
                    password = password[:-1]
                    print('\b \b', end='', flush=True)
            else:
                password += char.decode('utf-8')
                print('*', end='', flush=True)
    else:
        password = getpass.getpass(prompt)
    return password



if __name__ == "__main__":
    clear_screen()
    init(autoreset=True)  # Initialize colorama

    master_username = 'a'
    master_password = 'a'
    
    input_username = input("Enter your username: ")
    input_password = get_password()

    if input_username == master_username and input_password == master_password:
        main()
    elif ldap_login(input_username, input_password):
        main()