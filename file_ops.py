"""
file_ops.py
Custom module providing simple file-handling utility functions
for the Multi-Utility Toolkit.
"""

import os


def create_file(filename):
    """Create a new (empty) file. Returns True on success."""
    try:
        with open(filename, "x"):
            pass
        return True
    except FileExistsError:
        # If it already exists, just "touch" it so the flow doesn't break
        with open(filename, "a"):
            pass
        return True
    except OSError:
        return False


def write_file(filename, data):
    """Overwrite the file with the given data."""
    with open(filename, "w") as f:
        f.write(data)


def read_file(filename):
    """Return the contents of the file, or None if it doesn't exist."""
    if not os.path.exists(filename):
        return None
    with open(filename, "r") as f:
        return f.read()


def append_file(filename, data):
    """Append data to the end of the file."""
    with open(filename, "a") as f:
        f.write(data)
