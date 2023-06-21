import os
import sys
from dirsync import sync
from log import log_info, log_error, log_warning
from sync_status import count_remaining_files

# Modify your sources and destination folders here:
sources_destinations = {
    r"C:\\Users\\djhra\\Documents": r"E:\\Backup\\Documents",
    r"D:\\Downloads": r"E:\\Backup\\Downloads",
    r"D:\\My Music": r"E:\\Backup\\My Music",
    r"D:\\Pictures": r"E:\\Backup\\Pictures",
    r"C:\\Program Files (x86)\\Steam\\steamapps\\common": r"E:\\Backup\\Steam Games Backup"
}

# Modify the root folder within which you would like to perform backup:
root_backup = r"E:\\Backup"


def create_destination_folders():
    destination_errors = {}
    for destination in sources_destinations.values():
        try:
            if not os.path.exists(root_backup):
                os.makedirs(root_backup)
            if not os.path.exists(destination):
                os.makedirs(destination)
            destination_errors[destination] = None
        except (FileNotFoundError, OSError) as error:
            destination_errors[destination] = error
            if error:
                raise Exception(f"Could not access the destination folder: {error}")
        return destination_errors


def perform_backup():
    backup_warnings = {}
    for source, destination in sources_destinations.items():
        try:
            print(f"INFO: Performing the backup of {os.path.basename(source)}...")
            initial_remaining_count = count_remaining_files([source], destination)
            sync(source, destination, "sync", purge=True, create=True, verbose=0)
            remaining_count = count_remaining_files([source], destination)
            print(f"Remaining files to be synced: {remaining_count}/{initial_remaining_count}")
            print(f"INFO: Backup of {os.path.basename(source)} had completed successfully.\n\n")
        except OSError as error:
            log_error(f"ERROR: {error}")
            raise Exception(f"Backup of {os.path.basename(source)} failed with {error}")
        except Exception as warning:
            log_warning(f"WARNING: {warning}")
            backup_warnings[source] = warning
    return backup_warnings


def catch_errors():
    try:
        destination_errors = create_destination_folders()
        backup_warnings = perform_backup()
        if not any(destination_errors.values()) and not any(backup_warnings.values()):
            print(f"INFO: All backups have completed successfully.")
            log_info(f"INFO: All backups have completed successfully.")
    except Exception as error:
        print(f"ERROR: {error}")
        log_error(f"ERROR: {error}")



def execute():
    catch_errors()


def main() -> int:
    execute()
    return 0


if __name__ == "__main__":
    sys.exit(main())
