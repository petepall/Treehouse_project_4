from colorama import Fore

from presentation.menu import StoreMenu
from utilities.helper_functions import (clear_screen, date_to_string,
                                        to_currency)


def print_product_sheet(product: dict):
    clear_screen()
    StoreMenu.print_header("Product sheet")
    for value in product:
        print("The data for the selected product is:\n")
        print(f"{Fore.YELLOW}Product ID   :{Fore.RESET} {value.product_id}")
        print(f"{Fore.YELLOW}Product name :{Fore.RESET} {value.product_name}")
        print(
            f"{Fore.YELLOW}Product price:{Fore.RESET}"
            f" {to_currency(value.product_price)}")
        print(f"{Fore.YELLOW}Current stock:{Fore.RESET}"
              f" {value.product_quantity}")
        print()
        print(f"This product was last updated on:"
              f"{Fore.RED} {date_to_string(value.date_updated)}{Fore.RESET}")


def unknown_product_id(product_id: str):
    clear_screen()
    StoreMenu.print_header("Product sheet")
    print(f"\nThe product ID {Fore.RED}{product_id}{Fore.RESET}"
          f" does not exist.")
    print("Please try again")
