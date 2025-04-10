"""
Main application script for runnning the ML model Service

This script initializes the ModelService, loads the model,
makes a prediction based on predefined input parameters
and logs the output.

"""

from loguru import logger

from model.model_service import ModelService


@logger.catch   # this makes sure that logger catches any exception
def main():
    """
    Run the application.

    Load the model, make a prediction on provided data,
    and log the prediction.
    """
    logger.info("Running the Application")
    ml_svc = ModelService()
    ml_svc.load_model()

    feature_values = {
        'area': 85,
        'bedrooms': 2,
        'garden': 1,
        'constraction_year': 2015,
        'balcony_yes': 1,
        'storage_yes': 0,
        'parking_yes': 1,
        'garage_yes': 1,
        'furnished_yes': 1,
    }

    pred = ml_svc.predict(list(feature_values.values()))
    logger.info(f'Prediction: {pred}')


if __name__ == '__main__':
    main()
