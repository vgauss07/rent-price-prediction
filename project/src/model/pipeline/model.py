import pandas as pd
import pickle as pk
from loguru import logger

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import GridSearchCV

from config import model_settings
from model.pipeline.preparation import prepare_data


def build_model() -> None:
    """
    Build, evaluate and save a RandomForestRegressor model.

    This function orchestrates the model building pipeline.
    It starts by preparing the data, followed by defining the
    feature names, then splitting the data into training and
    testing sets. The model's performance is evaluated on the
    test set, and finally, the model is saved for future use

    Returns:
        None

    """
    # train and save the model we need:
    logger.info("Starting up Model Building Pipeline")
    # 1. load processed dataset
    df = prepare_data()
    feature_names = ['area',
                     'bedrooms',
                     'garden',
                     'constraction_year',
                     'balcony_yes',
                     'storage_yes',
                     'parking_yes',
                     'garage_yes',
                     'furnished_yes']
    logger.info("Building Model")
    # 2. identify X and y
    X, y = _get_X_Y(df, col_X=feature_names)
    # 3. split dataset
    X_train, X_test, y_train, y_test = _split_train_test(X, y)
    # 4. train the model
    rf = _train_model(X_train, y_train)
    # 5. model evaluation
    _evaluate_model(rf, X_test, y_test)
    # 6. Tune Hyperparameter
    # 7. Save Model
    _save_model(rf)


def _get_X_Y(dataframe: pd.DataFrame,
             col_X: list[str],
             col_y: str = 'rent'
             ) -> tuple[pd.DataFrame, pd.Series]:
    """
    Split the dataset into features and target variable.

    Args:
        dataframe (pd.DataFrame): Dataset to be split
        col_X (list[str]): list of feature names
        col_y (str): Name of the target variable column
    """
    logger.info(f'Defining X and Y variables.'
                f' \nX vars: {col_X}\ny var: {col_y}')
    return dataframe[col_X], dataframe[col_y]


def _split_train_test(X: pd.DataFrame, y: pd.Series
                      ) -> tuple[pd.DataFrame, pd.Series]:
    """
    Split the dataset into train and test sets

    Args:
        X (pd.DataFrame): features dataset
        y (pd.series): Target variable

    Returns:
        tuple: Training and testing sets for features & target.
    """
    X_train, X_test, y_train, y_test = train_test_split(X,
                                                        y,
                                                        test_size=0.2,
                                                        random_state=32
                                                        )
    return X_train, X_test, y_train, y_test


def _train_model(X_train: pd.DataFrame, y_train: pd.Series
                 ) -> RandomForestRegressor:
    """
    Train the RandomForestRegressor model with hyperparameter tuning

    Args:
        X_train (pd.DataFrame): Training set features
        y_train (pd.Series): Testing set Target

    Returns:
        RandomForestRegressor: The best estimator with Gridsearch
    """

    grid_space = {'n_estimators': [100, 200, 300],
                  'max_depth': [3, 6, 9, 12]}

    grid = GridSearchCV(RandomForestRegressor(),
                        param_grid=grid_space,
                        cv=5,
                        scoring='r2')
    logger.debug(f'grid_space = {grid_space}')

    model_grid = grid.fit(X_train, y_train)
    return model_grid.best_estimator_


def _evaluate_model(model: RandomForestRegressor,
                    X_test: pd.DataFrame,
                    y_test: pd.Series) -> float:
    """
    Evaluate the trained model's performance
    """
    logger.info(f'Evaluating Model Performance SCORE = '
                f'{model.score(X_test, y_test)}')
    return model.score(X_test, y_test)


def _save_model(model: RandomForestRegressor):
    """
    Save the trained model to a specified directory

    Args:
        model (RandomForestRegressor): The model to save

    Returns:
        None.
    """
    logger.info(f'Saving the Model:'
                f'{model_settings.model_path}/{model_settings.model_name}')
    pk.dump(model,
            open(f'{model_settings.model_path}/'
                 f'{model_settings.model_name}', 'wb'))


# test
build_model()
