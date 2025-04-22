"""
This module provides functionality for managing a ML model

It contains the ModelInferenceService class, which handles loading and using
a pretrained-ML model. The class offers methods to load a model
from a file, and to make predictions from the
loaded model.

"""

from pathlib import Path
import pickle as pk

from loguru import logger

from config import model_settings


class ModelInferenceService(object):
    """
    A service class for making predictions.

    This class provides functionalities to load a ML model from
    a specified path, built it if it doesn't exist, and make
    predictions using the loaded model.

    Attributes:
        model: ML model managed by this service. Initially set to None.

    Methods:
        __init__: Constructor that initializes the ModelService
        load_model: loads the model from file.
        predict: Makes a prediction using the loaded model
    """

    def __init__(self) -> None:
        """Initialize the ModelService with no model loaded"""
        self.model = None
        self.model_path = model_settings.model_path
        self.model_name = model_settings.model_name

    def load_model(self) -> None:
        """
        Load the model from a specified path

        raises FileNotFoundError


        """
        logger.info(f'Checking the existence of the model config file at '
                    f'{self.model_path}/{self.model_name}')

        model_path = Path(f'{self.model_path}/'
                          f'{self.model_name}')

        if not model_path.exists():
            raise FileNotFoundError('Model file does not exist!')

        logger.info(f'Model {self.model_name} Exists! ->'
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
