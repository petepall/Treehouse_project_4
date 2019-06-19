from peewee import IntegrityError

from models.product import Product


def write_rows_to_db(csv_data) -> None:
    """Read the data from the csv file and write it to the db

    Returns
    -------
    None
    """
    for row in csv_data:
        create_product(row)


def create_product(product: dict) -> None:
    """Takes a dictionary and inserts the product into the db

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
