import os
import shutil
from Module.SortFolder import sort_list
from Module.ExtensionFilter import extract_file_extensions
import pyautogui as pag
from tqdm import tqdm

def input_and_change_directory():
    input_path = pag.prompt(title = "Path to sort files", text = "Enter the main folder you want to sort files", default ='')
    """
    Prompts the user for an input path, creates a "# Sorted Files" directory within it,
    and changes the current working directory to the newly created directory.

    Returns:
        str: The input path provided by the user.
    """
    sorted_files_dir = os.path.join(input_path, "# Sorted Files")
    os.makedirs(sorted_files_dir, exist_ok=True)  # Create "# Sorted Files" directory if it doesn't exist
    os.chdir(sorted_files_dir)
    return input_path

def write_sorted_folder_list(subfolder_names):
    """
    Creates a text file named "Sorted Folder.txt" and writes a list of sorted subfolders to it.

    Args:
        subfolder_names (list): A list of subfolder names.
    """
    with open("Sorted Folder.txt", 'w') as f:
        f.write('List of the sorted folders:\n')
        for index, folder in enumerate(subfolder_names, start=1):
            f.write(f"{index}. {folder}\n")

def create_sorted_folders(subfolder_names):
    """
    Creates sorted folders based on subfolder names.

    Args:
        subfolder_names (list): A list of subfolder names.
    """
    for folder in subfolder_names:
        os.makedirs(f"Sorted of - {folder.replace('.', '')}", exist_ok=True)

def read_files_from_subfolders(input_path, subfolder_names):
    """
    Writes a list of files in each subfolder to a text file named "Sorted files.txt".

    Args:
        input_path (str): The input path to the directory.
        subfolder_names (list): A list of subfolder names.
    """
    with open("Sorted files.txt", "w", encoding="utf-8") as f:
        for index, folder in enumerate(subfolder_names, start=1):
            files_list = os.listdir(os.path.join(input_path, folder))
            files_list = sort_list(files_list)
            f.write(f"{index}\n")
            f.write(str(files_list) + "\n\n")

def read_files_extension(input_path, subfolder_names):
    with open("File extension.txt", "w", encoding="utf-8") as f:
        for index, folder in enumerate(subfolder_names, start=1):
            files_extension = extract_file_extensions(os.listdir(os.path.join(input_path, folder)))
            files_extension = sort_list(files_extension)
            file_extensions = list(set(files_extension))
            f.write(f"{index}\n")
            f.write(str(file_extensions) + "\n\n")

def read_extension_list_and_create_subfolders_then_copy(input_path, subfolder_names):
    """
    Extracts file extensions from files in each subfolder and creates subfolders based on extensions.
    Moves files to corresponding extension subfolders.

    Args:
        input_path (str): The input path to the directory.
        subfolder_names (list): A list of subfolder names.
    """
    for folder in subfolder_names:
        folder_path = os.path.join(input_path, folder)
        file_extension = extract_file_extensions(os.listdir(folder_path))
        file_extensions = list(set(file_extension))
        target_dir = f"Sorted of - {folder.replace('.', '')}"


        for ext in file_extensions:
            ext_dir = os.path.join(target_dir, ext)
            os.makedirs(ext_dir, exist_ok=True)

            files_to_copy = [os.path.join(folder_path, file) for file in os.listdir(folder_path) if file.endswith(ext)]
            with tqdm(total=len(files_to_copy), desc=f"Copying files to {ext_dir}") as pbar:
                for file in files_to_copy:
                    try:
                        shutil.copy(file, ext_dir)
                        pbar.update(1)
                    except PermissionError as e:
                        print(f"Error copying {file}: {e}")
            
def main():
    """
    Main function to orchestrate the sorting process.
    """
    input_path = input_and_change_directory()
    all_folders = os.listdir(input_path)
    all_folders = sort_list(all_folders)
    subfolders = all_folders[1:]  # Exclude the first element

    write_sorted_folder_list(subfolders)
    create_sorted_folders(subfolders)
    read_files_from_subfolders(input_path, subfolders)
    read_files_extension(input_path, subfolders)
    read_extension_list_and_create_subfolders_then_copy(input_path, subfolders)

if __name__ == "__main__":
    main()
