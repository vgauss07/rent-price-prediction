import pandas as pd

from loguru import logger
from sqlalchemy import select

from config import engine
from db.db_model import RentApartments


def load_data(FILEPATH):      # data_file_name
    """Loads data from a specified file path."""
    logger.info(f"loading csv file at path {FILEPATH}")
    return pd.read_csv(FILEPATH)


def load_data_from_db():
    """Loads data from a database"""
    logger.info("Extracting Data from the Database")
    query = select(RentApartments)
    return pd.read_sql(query, engine)
