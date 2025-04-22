"""
This module provides functionality for managing a ML model

It contains the ModelBuilderService class, which handles model training
and saving to a directory. The class offers methods to train a model
and save the model.

"""

from loguru import logger

from config import model_settings
from model.pipeline.model import build_model


class ModelBuilderService(object):
    """
    A service class for managing the ML model

    This class provides functionalities to train the ML model from
    a specified path and save it.

    Attributes:
        model_path: Dir ML model is saved to.
        model_name: Name of the saved model

    Methods:
        __init__: Constructor that initializes the ModelBuilderService
        train_model: Trains the model and saves it.
    """

    def __init__(self) -> None:
        """Initialize the ModelBuilderService."""
        self.model_path = model_settings.model_path
        self.model_name = model_settings.model_name

    def train_model(self) -> None:
        """Train the model from a specified path,
        and save to model's directory."""
        logger.info(f'Building model config file at '
                    f'{self.model_path}/{self.model_name}')
        build_model()
