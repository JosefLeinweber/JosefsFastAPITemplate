"""
This file is necessary for the initialization of the database tables.
All database tables should be imported here, else they will not be initialized.
"""

from src.models.db_tables.account_table import Account
from src.utility.database.base_table import DBBaseTable
