import os
import platform

# Check if colorama package is installed
try:
        import pkg_resources
        pkg_resources.require("pywin32")
except ImportError:
        print("pywin32 not found. Installing...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pywin32"])

try:
    import colorama
except ImportError:
    # Install colorama package
    os.system("pip install colorama")
    import colorama

try:
    from PIL import Image
except ImportError:
    # Install Pillow package
    os.system("pip install Pillow")
    from PIL import Image
try:
    import psutil
except ImportError:
    # Install Pillow package
    os.system("pip install psutil")
    import psutil
    
try:
    import curses
except ImportError:
    # Install Pillow package
    os.system("pip install windows-curses")
    import curses
    
try:
    from moviepy.editor import VideoFileClip
except ImportError:
    # Install Pillow moviepy package
    os.system("pip install Pillow moviepy")
    from moviepy.editor import VideoFileClip


# Check if cryptography package is installed
try:
    from cryptography.fernet import Fernet
except ImportError:
    # Install cryptography package
    os.system("pip install cryptography")
    from cryptography.fernet import Fernet

# Import other necessary modules
import shutil
import hashlib
import traceback
import hashlib
import uuid
import string
import random
import datetime
import getpass
import zipfile
from colorama import Fore, Style
import moviepy.editor as mp
import psutil
import curses
import time
import socket
import sys
import threading
import subprocess
import ctypes
import win32api
import winreg





def folder_tools():
    Clear_Screen()
    print(Fore.RED + "\nFolder Tools Menu:")
    print(Fore.YELLOW + "1. List contents of a folder")
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
    print("13. Create symbolic links")
    print("0. Back")
    choice = input(Fore.CYAN +"Enter your choice: ")

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
    Clear_Screen()
    print(Fore.RED + "\nDelete Folder(s) Menu:")
    print(Fore.YELLOW + "1. Delete all folders in the current path")
    print("2. Delete all folders in a directory")
    print("3. Delete folder(s) by name")
    print("0. Back")
    choice = input(Fore.CYAN +"Enter your choice: ")

    if choice == '1':
        delete_all_folders_in_current_path()
    elif choice == '2':
        folder_path = input("Enter the path of the directory: ")
        delete_all_folders(folder_path)
    elif choice == '3':
        folder_names = input("Enter the name(s) of the folder(s) to delete (separated by commas): ")
        delete_folders_by_name(folder_names)
    elif choice == '0':
         folder_tools()
    else:
        print("Invalid choice!")


def file_tools():
    Clear_Screen()
    print(Fore.RED + "\nFile Tools Menu:")
    print(Fore.YELLOW + "1. File Information")
    print("2. File Operations")
    print("3. File Comparison")
    print("4. File Search")
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
    Clear_Screen()
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
            os.mkdir(name.strip()) 
            print(f"{Fore.GREEN}Folder '{name.strip()}' created successfully.")
        except FileExistsError:
            print(f"{Fore.YELLOW}Folder '{name.strip()}' already exists!")
        except Exception as e:
            print(f"{Fore.RED}An error occurred while creating folder '{name.strip()}': {e}")


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
            shutil.rmtree(name.strip())  
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

def conversion_tools():
    Clear_Screen()
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

def admin_tools():
    Clear_Screen()
    print(Fore.RED+"\nAdministrator Tools Menu:")
    print(Fore.YELLOW +"1. Show System Users")
    print("2. Add user(s)")
    print("3. Remove user(s)")
    print("4. Remove Keyboard(s)")
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
         usernumber = input('Set Number of users need to Create: ')
         if usernumber == '1':
            add_single_user()
         else:
            add_multiple_users(usernumber)
    elif choice == '3':
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
    elif choice == '4':
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
    elif choice == '0':
        main()
    else:
        print(Fore.RED+"Invalid choice...")
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


def Monitor_tools():
         Clear_Screen()
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
             
def Network_Tools():
    Clear_Screen()
    print(Fore.RED+"\nNetwork Tools Menu:")
    print(Fore.YELLOW +"1. Show Network Connection")
    print("2. Scan Open Ports")
    print("3. Network Scaner")
    print("4. Send Magic Packet")
    print("5. Down Client With UDP Packet")
    print("6. Down Client With TCP Packet ")
    print("0. Back")
    choice=input("Enter Your Choice:")
    if choice=='1':
        Network_connections()
    elif choice=='2':
        scan_open_ports()
    elif choice=='3':
        subnet, ip_range = get_user_input()
        scan_network(ip_range, subnet)
        print("\nScanning Complete!")
    elif choice=='5':
            host = input("Enter the target IP address: ")
            port = int(input("Enter the target port: "))
            total_packets = int(input("Enter Number Of Packets:"))
            num_threads = int(input("Enter Number Of Thread:"))
            send_udp_packets_multithread(host, port, total_packets, num_threads)
    elif choice=='4':
        mac_address, broadcast_address = get_user_input_magic_packet()
        send_magic_packet(mac_address, broadcast_address)
        print("Magic packet sent successfully!")
    elif choice=='6':
         ip_address, num_pings,num_thread = get_user_input_ping()

         # Start ping processes in separate threads
         threads = []
         for _ in range(num_thread):  # You can change 100 to any desired number of threads
             thread = threading.Thread(target=ping_target, args=(ip_address, num_pings))
             thread.start()
             threads.append(thread)

         # Wait for user input to stop ping processes
         input("Press Enter to stop pinging...")
         stop_ping_threads()

         # Join all threads to wait for them to complete
         for thread in threads:
             thread.join()
    elif choice=='0':
        main()
    else:
        print(Fore.RED+"Invalid choice...")

def scan_open_ports():
    Clear_Screen()
    print(Fore.RED+"\nScan Port Tools Menu:")
    print(Fore.YELLOW +"1. Scan On Current Machine")
    print("2. Scan On Special IP")
    print("0. Back")
    choice=input("Enter Your Choice:")
    if choice=='1':
        display_open_ports()
    elif choice=='2':
        ip_address, port_range = get_user_input_port_scan()
        open_ports = get_open_ports(ip_address, port_range)
        print("Open ports:", open_ports)
    elif choice=='0':
        main()
    else:
        print(Fore.RED+"Invalid choice...")
        
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
    Clear_Screen()
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

def show_system_users_windows():
    os.system("net user")

def show_system_users_linux():
    with open("/etc/passwd", "r") as passwd_file:
        for line in passwd_file:
            username = line.split(":")[0]
            print(username)

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

def display_processes():
    Clear_Screen()
    if platform.system() == 'Windows':
        subprocess.call('tasklist', shell=True)
    elif platform.system() == 'Linux':
        subprocess.call('ps aux', shell=True)
    else:
        print("Unsupported operating system")
        
def display_hardware_usage():
    Clear_Screen()
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
    Clear_Screen()
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

def display_open_ports():
    Clear_Screen()
    print(Fore.RED+"Open Ports:")
    for port in get_open_ports():
        print(f"    Port {port}")

def get_open_ports():
    open_ports = []
    total_ports = 1024  # Total number of ports to scan
    for i, port in enumerate(range(1, total_ports + 1), 1):
        percent = i / total_ports
        display_progress_bar(percent)
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(0.1)  # Adjust timeout as needed
                s.connect(("127.0.0.1", port))
            open_ports.append(port)
        except:
            pass
    print()  # Move to the next line after progress bar
    return open_ports

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

def scan_network(ip_range, subnet):
    total_ips = ip_range[1] - ip_range[0] + 1
    progress = 0
    for i in range(ip_range[0], ip_range[1] + 1):
        ip = f"{subnet}.{i}"
        try:
            hostname = socket.gethostbyaddr(ip)[0]
        except (socket.herror, socket.gaierror):
            hostname = "N/A"
        os_info = platform.system()
        print(f"IP: {ip}, Hostname: {hostname}, OS: {os_info}")
        progress += 1
        percent = (progress / total_ips)
        display_progress_bar(percent)

def get_user_input():
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

def send_udp_packet(host, port, num_packets_per_thread):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        for _ in range(num_packets_per_thread):
            sock.sendto(b'ping', (host, port))
        print(f"UDP packets sent to {host}:{port}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        sock.close()

def send_udp_packets_multithread(host, port, total_packets, num_threads):
    num_packets_per_thread = total_packets // num_threads
    threads = []
    for _ in range(num_threads):
        thread = threading.Thread(target=send_udp_packet, args=(host, port, num_packets_per_thread))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
        
stop_threads = False

def ping_target(ip, num_pings):
    global stop_threads
    if platform.system() == "Windows":
        command = ["ping", "-n", str(num_pings), ip]
    else:
        command = ["ping", "-c", str(num_pings), ip]

    while not stop_threads:
        subprocess.run(command)

def stop_ping_threads():
    global stop_threads
    stop_threads = True

def get_user_input_ping():
    ip_address = input("Enter the target IP address: ")
    num_pings = int(input("Enter the number of pings: "))
    num_thread = int(input("Enter the number of thread: "))
    return ip_address, num_pings, num_thread


def main():
    Clear_Screen()
    while True:
        print(Style.RESET_ALL + Fore.RED+ "\nMain Menu:")
        print(Fore.WHITE + "1. Folder Tools")
        print("2. File Tools")
        print("3. Admin Tools")
        print("4. Monitor Tools")
        print("5. Network Tools")
        print("0. Exit")
        choice = input(Fore.CYAN +"Enter your choice: ")

        if choice == '1':
            folder_tools()
        elif choice == '2':
            file_tools()
        elif choice == '3':
            admin_tools()
        elif choice == '4':
            Monitor_tools()
        elif choice == '5':
            Network_Tools()
        elif choice == '0':
            print(Fore.GREEN+"Exiting the program. Goodbye!")
            print(Style.RESET_ALL)
            break
        else:
            print("Invalid choice!")




def Clear_Screen():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

if __name__ == "__main__":
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")
        
    main()
