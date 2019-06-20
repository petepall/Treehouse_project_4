from pyfiglet import Figlet
from utilities.helper_functions import clear_screen
import colorama
from colorama import Fore, Back, Style
from collections import OrderedDict


class StoreMenu:

    colorama.init()

    @classmethod
    def _header(cls) -> None:
        clear_screen()
        text = Figlet(font='speed', width=100)
        print(text.renderText("Store Inventory"))
        print(f"{'~' * 96:96}")

    @classmethod
    def _menu_options(cls, options: OrderedDict) -> None:
        for key, value in options.items():
            print(f"   {Fore.YELLOW}{key}){Fore.RESET} {value.strip():90}",
                  end="\n")
        print()
