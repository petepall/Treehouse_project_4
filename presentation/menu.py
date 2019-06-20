from pyfiglet import Figlet
import colorama
from colorama import Fore
from collections import OrderedDict


class StoreMenu:

    colorama.init()

    @classmethod
    def _header(cls) -> None:
        text = Figlet(font='speed', width=100)
        print(text.renderText("Store Inventory"))
        print(f"{'~' * 96:96}")

    @classmethod
    def _menu_options(cls, options: OrderedDict) -> None:
        for key, value in options.items():
            print(f"   {Fore.YELLOW}{key}){Fore.RESET} {value.strip():90}",
                  end="\n")
        print()

    @classmethod
    def _process_menu_input(cls):
        pass

    @classmethod
    def menu(cls):
        pass
              
