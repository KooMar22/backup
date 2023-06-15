import sys
from backup import execute
from log import log_info


def main() -> int:
    log_info("Starting backup")
    execute()
    return 0

if __name__ == "__main__":
    sys.exit(main())