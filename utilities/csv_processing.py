import csv
import os
from typing import Any

from utilities.helper_functions import (string_to_date, convert_to_cents,
                                        date_to_string)


def read_from_csv(filename: str) -> Any:
    """Read the csv file

    Parameters
    ----------
    filename : string
        Path and name of the file

    Returns
    -------
    dict
        Read data
    """
    if os.path.isfile(filename):
        with open(filename, mode='r') as csvfile:
            product_data = csv.DictReader(csvfile, delimiter=',')
            rows = list(product_data)
    return rows


def clean_csv_data(product_data: dict) -> dict:
    """Clean the read csv data and convert to proper format

    Parameters
    ----------
    product_data : Dict
        Product data information

    Returns
    -------
    dict
        cleaned and converted product data
    """
    for row in product_data:
        row['product_quantity'] = int(row['product_quantity'])
        row['product_price'] = convert_to_cents(row['product_price'])
        row['date_updated'] = string_to_date(row['date_updated'])
    return product_data


def write_to_csv(filename: str, products: dict) -> None:
    """Write product data to a csv file including the headers

    Parameters
    ----------
    filename : str
        Filename to which to write the data
    products : dict
        data from the database that needs to be written to the file

    Returns
    -------
    None
    """
    fieldnames = ['product_name',
                  'product_quantity',
                  'product_price',
                  'date_updated']

    with open(filename, mode='w') as csvfile:
        csv_writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        csv_writer.writeheader()
        for product in products:
            price = f"${product.product_price / 100}"
            date_string = date_to_string(product.date_updated)
            csv_writer.writerow({
                'product_name': product.product_name,
                'product_quantity': product.product_quantity,
                'product_price': price,
                'date_updated': date_string
            })
