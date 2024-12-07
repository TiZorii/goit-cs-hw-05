import shutil
import asyncio
from pathlib import Path
import logging
from colorama import Fore, Style
import textwrap

# Logging setup
logging.basicConfig(level=logging.ERROR, format="%(asctime)s - %(message)s")

# Asynchronous function for copying files
async def copy_file(file_path, dest_folder):
    try:
        # Get file extension
        file_extension = file_path.suffix.lstrip(".").lower()
        if not file_extension:
            file_extension = "unknown"

        # Create folder for the extension
        dest_path = dest_folder / file_extension
        dest_path.mkdir(parents=True, exist_ok=True)

        # Copy the file
        await asyncio.to_thread(shutil.copy, file_path, dest_path)
        # Format long lines
        formatted_message = textwrap.fill(
            f"File {file_path.name} copied to {dest_path}",
            width=120
        )
        print(Fore.GREEN + formatted_message + Style.RESET_ALL)
    except Exception as e:
        logging.error(f"Error copying file {file_path}: {e}")
        print(
            Fore.RED + f"Error copying file {file_path}: {e}" + Style.RESET_ALL)

# Asynchronous function for reading the folder
async def read_folder(source_folder, dest_folder):
    try:
        tasks = []
        # Iterate over all files and subfolders
        for item in source_folder.iterdir():
            if item.is_file():
                tasks.append(copy_file(item, dest_folder))
            elif item.is_dir():
                tasks.append(read_folder(item, dest_folder))
        # Execute tasks asynchronously
        await asyncio.gather(*tasks)
    except Exception as e:
        logging.error(f"Error reading folder {source_folder}: {e}")
        print(
            Fore.RED + f"Error reading folder {source_folder}: {e}" + Style.RESET_ALL)

# Main function
def main():
    print(Fore.BLUE + "Specify the path to the folder for sorting" + Style.RESET_ALL)

    # Request the source folder path
    source_folder_path = input(
        Fore.YELLOW + "Enter the path to the source folder: " + Style.RESET_ALL).strip()

    # Request the target folder path
    sorted_folder_path = input(
        Fore.YELLOW + "Enter the path to the target folder: " + Style.RESET_ALL).strip()

    # Convert paths to Path objects
    source_folder = Path(source_folder_path)
    sorted_folder = Path(sorted_folder_path)

    # Check if the source folder exists
    if not source_folder.is_dir():
        print(
            Fore.RED + "Error: Source folder does not exist or is not a folder." + Style.RESET_ALL)
        return

    print(Fore.BLUE + "File sorting is starting..." + Style.RESET_ALL)
    asyncio.run(read_folder(source_folder, sorted_folder))
    print(Fore.BLUE + "File sorting completed." + Style.RESET_ALL)


if __name__ == "__main__":
    main()
