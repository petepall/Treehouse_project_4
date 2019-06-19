import os
from datetime import date, datetime


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
    return int(price.replace('$', '').replace('.', ''))


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
    return date.strftime(date_to_convert, '%m/%d/%Y')
