import os
import sys

def count_source_files(source_directories):
    source_count = 0
    for directory in source_directories:
        for root, dirs, files in os.walk(directory):
            source_count += len(files)
    return source_count

source_directories = [
    "C:\\Users\\djhra\\Documents",
    "D:\\Downloads",
    "D:\\My Music",
    "D:\\Pictures",
    "C:\\Program Files (x86)\\Steam\\steamapps\\common"
]

def count_destination_files(destination_directory):
    destination_count = 0
    for root, dirs, files in os.walk(destination_directory):
        destination_count += len(files)
    return destination_count

destination_directory = "E:\\Backup"


def count_remaining_files(source_directories, destination_directory):
    source_count = count_source_files(source_directories)
    destination_count = count_destination_files(destination_directory)
    remaining_count = source_count - destination_count
    return remaining_count

def main() -> int:
    remaining_count = count_remaining_files(source_directories, destination_directory)
    print("Remaining files to be synced:", remaining_count)
    return 0

if __name__ == "__main__":
    sys.exit(main())