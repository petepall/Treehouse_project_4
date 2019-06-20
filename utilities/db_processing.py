from peewee import IntegrityError, InternalError

from models.product import Product
from utilities.csv_processing import clean_csv_data, read_from_csv


def create_database() -> None:
    """Create the database
    """
    try:
        Product.create_table(safe=True)
    except InternalError as err:
        print(str(err))


def load_csv_data_in_database(csvfile: str) -> None:
    """Load the data from the CSV file into the database

    Parameters
    ----------
    csvfile : str
        CSV file path and filename

    Returns
    -------
    None

    """
    loaded_csv = read_from_csv(csvfile)
    csv_data = clean_csv_data(loaded_csv)
    write_csv_to_db(csv_data)


def write_csv_to_db(csv_data) -> None:
    """Read the data from the csv file and write it to the db

    Returns
    -------
    None
    """
    for row in csv_data:
        add_product_to_db(row)


def add_product_to_db(product: dict) -> None:
    """Takes a dictionary and inserts the product into the db.
    If a product with duplicate name is found, existing data will be updated if
    the 'date_updated' is higher than the existing record.

    Parameters
    ----------
    product : dict
        Row of Product data

    Returns
    -------
    None
    """
    try:
        Product.insert(product_name=product['product_name'],
                       product_price=product['product_price'],
                       product_quantity=product['product_quantity'],
                       date_updated=product['date_updated']).execute()
    except IntegrityError:
        result = Product.get(product_name=product['product_name'])
        if product['date_updated'] > result.date_updated:
            result.product_quantity = product['product_quantity']
            result.product_price = product['product_price']
            result.date_updated = product['date_updated']
            result.save()


def view_product():
    # TODO: build out the view_product method
    pass


def backup_data():
    # TODO: build out the backup_data method
    pass


def create_product():
    # TODO: build out the create_product method
    pass
