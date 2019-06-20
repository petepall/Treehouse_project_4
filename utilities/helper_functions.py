import os
from datetime import date, datetime
from presentation.menu import StoreMenu


def clear_screen() -> None:
    """Clear the console screen

    Returns
    -------
    None
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def convert_to_cents(price: str) -> int:
    """Convert the price to cents, stripping the currency sign

    Parameters
    ----------
    price : str
        Price provided in string format

    Returns
    -------
    int
        Price converted to cents
    """
    return int(price.replace('$', '').replace('.', '').replace(',', ''))


def string_to_date(given_date: str) -> date:
    """Clean and convert a string date into a datetime data

    Parameters
    ----------
    given_date : str
        Date in string format

    Returns
    -------
    date
        Date in datetime,date format
    """
    return datetime.strptime(given_date, '%m/%d/%Y').date()


def date_to_string(date_to_convert: date) -> str:
    """Provided with a date in date format, convert this to a string format

    Parameters
    ----------
    date_to_convert : date
        date in date format

    Returns
    -------
    str
        date in formated string format
    """
    return date.strftime(date_to_convert, '%m/%d/%Y')


def to_currency(cents: int) -> str:
    """Convert a given number of cent into a string formated dollar format

    Parameters
    ----------
    cents : int
        Number of cents that needs to be converted

    Returns
    -------
    str
        Formated dollar amount
    """
    return f"${cents / 100:.2f}"


def create_folder(location: str):
    """Receive a folder location and name and create the folder

    Parameters
    ----------
    location : str
        folder location and name
    """
    try:
        os.mkdir(location)
    except FileExistsError:
        pass


def check_folder_exists(location: str) -> bool:
    """Receive a folder path and name and validate if it exists

    Parameters
    ----------
    location : str
        string representing the folder path and name

    Returns
    -------
    bool
        True if folder is found else False is returned
    """
    if os.path.isdir(location):
        return True
    else:
        return False


def wait_for_enter(field_data=""):
    """Wait for the user entry to continue

    Parameters
    ----------
    field_data : str, optional
        Data to show in the message, by default ""
    """
    try:
        input(f"{field_data}\n"
              f"Press the 'ENTER' key to continue")
    except KeyboardInterrupt:
        pass


def product_search_input() -> str:
    """handle the user input for search on product ID

    Returns
    -------
    str
        entered product ID
    """
    while True:
        clear_screen()
        StoreMenu.print_header("Product sheet")
        try:
            product_id = input("Enter the product ID to display >>>  ")
            if product_id.isnumeric():
                return product_id
            else:
                wait_for_enter("You must enter a number")
                continue
        except KeyboardInterrupt:
            wait_for_enter("Exit via CTRL-C not possible")
