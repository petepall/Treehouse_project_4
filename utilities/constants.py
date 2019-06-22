from pathlib import Path
from collections import OrderedDict


DB_FOLDER = str(Path('db/').resolve())
DB_FILE = "inventory.db"
CSV_FILE_IMPORT = str(Path('import_data/inventory.csv').resolve())
CSV_FOLDER_EXPORT = str(Path('archive').resolve())
CSV_FILE_EXPORT = "/backup.csv"
MENU = OrderedDict([
    ('a', 'Add product'),
    ('v', 'View selected product'),
    ('b', 'Export data in csv format'),
    ('q', 'QUIT the App')
])
