import pandas as pd
import regex as re
from loguru import logger

from model.pipeline.collection import load_data_from_db


def prepare_data():
    """Prepares the data; integrating different data cleaning functions."""
    logger.info("Starting up Preprocessing Pipeline")
    # to prepare dataset:
    # load dataset
    data = load_data_from_db()  # noqa: WPS110
    logger.info('Preprocessing Data')
    # transform categorical columns
    # encode columns like balcony, parking etc
    data_encoded = _encode_cat_col(data)
    # parse the garden column
    df = _parse_garden_col(data_encoded)
    final_df = _encode_bool(df)
    return final_df


def _encode_bool(dataframe: pd.DataFrame) -> pd.DataFrame:
    """Encodes true-false columns into 1's and 0's"""
    logger.info("Encoding Boolean Column")
    true_false_columns = dataframe.select_dtypes(include=['bool']).columns
    dataframe[true_false_columns] = dataframe[true_false_columns].astype(int)
    return dataframe


def _encode_cat_col(dataframe: pd.DataFrame) -> pd.DataFrame:
    """Encodes categorical columns"""
    cols = ['balcony', 'parking', 'furnished', 'garage', 'storage']
    logger.info(f'Encoding Categorical Columns: {cols}')
    return pd.get_dummies(dataframe,
                          columns=cols,
                          drop_first=True)


def _parse_garden_col(dataframe: pd.DataFrame) -> pd.DataFrame:
    """
    Parses the garden column to get the integer value.

    Args:
        dataframe (pd.DataFrame): The dataset with a 'garden' column

    Returns:
        pd.DataFrame: The dataset with the 'garden' column parsed.
    """
    logger.info('Parsing Garden Column')
    dataframe['garden'] = dataframe['garden'].apply(
        lambda x: 0 if x == 'Not present' else int(re.findall(r'\d+', x)[0])
    )
    return dataframe


df = prepare_data()
