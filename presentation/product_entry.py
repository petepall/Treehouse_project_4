from datetime import date

from presentation.menu import StoreMenu
from utilities.helper_functions import (clear_screen, convert_to_cents,
                                        wait_for_enter)


def enter_product_data() -> dict:
    product = {}

    while True:
        clear_screen()
        StoreMenu.print_header("Product sheet")
        try:
            name = input("Product name >>>  ")

            try:
                price = convert_to_cents(
                    input("Product price in USD (0.00) >>>  "))
            except ValueError:
                wait_for_enter("\nPlease enter a numeric value")
                continue

            try:
                quantity = int(input("Product quantity >>>  "))
            except ValueError:
                wait_for_enter("\nPlease enter a numeric value")
                continue
        except KeyboardInterrupt:
            wait_for_enter("Exit via CTRL-C not possible")
            continue
        break

    product['product_name'] = name
    product['product_price'] = price
    product['product_quantity'] = quantity
    product['date_updated'] = date.today()

    return product
