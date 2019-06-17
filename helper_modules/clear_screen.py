import os


def clear_screen():
    """clear the data on the screen. for windows and unix/linux systems
    """
    os.system("cls" if os.name == "nt" else "clear")
