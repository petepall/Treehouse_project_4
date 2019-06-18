import csv
from pathlib import Path
from datetime import datetime


def read_csv_data():
    """Read the csv data and return the header and product data.
    """
    with open(f"{Path().absolute()}\\data_import\\inventory.csv") as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=',')
        rows = list(csv_reader)
        csv_header = csv_reader.fieldnames
        product_data = rows[1:]

    return csv_header, product_data


def clean_data():
    """Clean the loaded csv data so that it's ready for the database
    processing
    """
    inventory = []
    header, product_data = read_csv_data()

    for row in product_data:
        print(row)
        # remove the $ from the price and covert to cents
        row['product_price'] = int(
            float(row['product_price'].lstrip('$')) * 100)
        row['product_quantity'] = int(row['product_quantity'])
        # create the date time field.
        last_updated = row['date_updated'].split('/')
        row['date_updated'] = datetime(int(last_updated[2]),
                                       int(last_updated[0]),
                                       int(last_updated[1]),
                                       0, 0, 0, 0)

        inventory.append({header[0]: row['product_name'],
                          header[1]: row['product_price'],
                          header[2]: row['product_quantity'],
                          header[3]: row['date_updated']})

    return inventory


clean_data()
