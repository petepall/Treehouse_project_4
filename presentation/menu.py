from pyfiglet import Figlet
import colorama
from colorama import Fore
from collections import OrderedDict


class StoreMenu:

    colorama.init()

    @classmethod
    def print_header(cls, header: str) -> None:
        """Print the header of the menu

        Parameters
        ----------
        header : str
            Text that will be used to print the header

        Returns
        -------
        None

        """
        text = Figlet(font='speed', width=100)
        print(text.renderText(header))
        print(f"{'~' * 96:96}")

    def _show_menu_options(self, options: OrderedDict) -> None:
        """Receive the menu options as an orderedDict and print these out

        Parameters
        ----------
        options : OrderedDict
            Menu options and text or method/function

        Returns
        -------
        None

        """
        for key, value in options.items():
            print(f"   {Fore.YELLOW}{key}){Fore.RESET} {value.strip():90}",
                  end="\n")
        print()

    def _process_menu_selection(self, options: OrderedDict) -> str:
        try:
            menu_entry = input("Enter your selection >>>  ")
        except KeyboardInterrupt:
            return f"{Fore.RED}The entry is not known. " \
                f"Please try again{Fore.RESET}"
        if menu_entry not in options.keys():
            return f"{Fore.RED}The entry is not known. " \
                f"Please try again{Fore.RESET}"
        else:
            return menu_entry

    def menu(self, options: OrderedDict, header: str) -> str:
        self.print_header(header)
        self._show_menu_options(options)
        return self._process_menu_selection(options)
