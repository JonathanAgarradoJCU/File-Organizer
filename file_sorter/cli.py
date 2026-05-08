import argparse
from pathlib import Path

from .core import sort_files_by_extension


def get_default_downloads_folder():
    return str(Path.home() / "Downloads")


def parse_args():
    parser = argparse.ArgumentParser(
        description="Sort files into subfolders by extension."
    )
    parser.add_argument(
        "directory",
        nargs="?",
        default=get_default_downloads_folder(),
        help="Directory to sort (defaults to the current user's Downloads folder).",
    )
    parser.add_argument(
        "--log-file",
        default="file_sort_log.txt",
        help="Name of the log file written to the target directory.",
    )
    return parser.parse_args()


def main():
    args = parse_args()
    sort_files_by_extension(args.directory, args.log_file)


if __name__ == "__main__":
    main()
