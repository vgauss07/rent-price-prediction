"""
Main application script for runnning the ML Model Service

This script initializes the ModelBuilderService, trains the model,
and logs the output.

"""

from loguru import logger

from model.model_builder import ModelBuilderService


@logger.catch   # this makes sure that logger catches any exception
def main():
    """
    Run the application.

    Train the model, and save it to
    a directory.
    """
    logger.info("Running the Application")
    ml_svc = ModelBuilderService()
    ml_svc.train_model()


if __name__ == '__main__':
    main()
