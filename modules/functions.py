# -----------------------------------------------------------------------------
# Module: Functions
#
# What: Miscellaneous functions. 
#
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
# 1 - Imports
# ------------------------------------------------------------------------------
import os, sys

# ------------------------------------------------------------------------------
# 2 - Functions
# ------------------------------------------------------------------------------
# Retrives base path (Important when creating executable)
def get_base_path():
    try:
    # PyInstaller creates a temp folder and stores path in _MEIPASS
        return sys._MEIPASS
    except Exception: # If not using pyinstaller
        return os.path.abspath(".")

# Absolute path
def resource_path(relative_path):
    base_path = get_base_path()

    return os.path.join(base_path, relative_path)