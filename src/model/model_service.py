"""
This module provides functionality for managing a ML model

It contains the ModelService class, which handles loading and using
a pretrained-ML model. The class offers methods to load a model
from a file, building it if it doesn't exist, and to make predictions from the
loaded model.

"""

from pathlib import Path
import pickle as pk

from loguru import logger

from config import model_settings
from model.pipeline.model import build_model


class ModelService(object):
    """
    A service class for managing the ML model

    This class provides functionalities to load a ML model from
    a specified path, built it if it doesn't exist, and make
    predictions using the loaded model.

    Attributes:
        model: ML model managed by this service. Initially set to None.

    Methods:
        __init__: Constructor that initializes the ModelService
        load_model: loads the model from file or builds it if it doesn't exist.
        predict: Makes a prediction using the loaded model
    """

    def __init__(self) -> None:
        """Initialize the ModelService with no model loaded"""
        self.model = None

    def load_model(self) -> None:
        """Load the model from a specified path,
        or builds it if it doesn't exist."""
        logger.info(f'Checking the existence of the model config file at '
                    f'{model_settings.model_path}/{model_settings.model_name}')
        model_path = Path(f'{model_settings.model_path}/'
                          f'{model_settings.model_name}')

        if not model_path.exists():
            logger.warning(f'model at'
                           f'{model_settings.model_path}/'
                           f'{model_settings.model_name} void'
                           f'building {model_settings.model_name}')
            build_model()

        logger.info(f'Model {model_settings.model_name} Exists! ->'
                    f'loading Model Configuration File')

        with open(model_path, 'rb') as model_file:
            self.model = pk.load(model_file)

            # self.model = pk.load(open(f'{settings.model_path}
            # /{settings.model_name}', 'rb'))

    def predict(self, input_parameters: list) -> list:
        """
        Make prediction using the loaded model

        Take input parameters and passes it to the model,
        which was loaded using a pickle file

        Args:
            input_parameters (list): The input data for making a prediction

        Returns:
            list: The prediction result from the model.
        """
        logger.info('Making Prediction!')
        return self.model.predict([input_parameters])
