"""
Prediction API module.

This module contains endpoints to trigger a machine learning model
for predicting apartment price.

Endpoints:
    - GET /pred/:
    Returns a prediction for apartment price based on the query
    parameters provided in the request. Query parameters should
    match the schema defined in the Apartment class.

    - POST /pred/:
    Returns a prediction for apartment price based on the JSON
    data provided in the request body. The request body should
    contain JSON data that matches the schema defined in the
    Apartment class.
    Returns HTTP status 400 if input parameters are invalid.
"""

from flask import Blueprint, abort, request
from pydantic import ValidationError

from schema.apartments import Apartment
from services import model_inference_service


bp = Blueprint('prediction', __name__, url_prefix='/pred')


@bp.get('/')
def get_prediction() -> dict:
    """
    Returns a prediction based on the query parameters

    Returns:
        dict: A dictionary containing the prediction result.
    """

    # getting and checking input parameters (feature values)
    try:
        apartment_features = Apartment(**request.args)
    except ValidationError:
        abort(code=400, description='Bad input params')  # noqa: WPS432

    # feed input parameters to the loaded ml model to get a prediction
    # converts the validated input data into a format that the ML model
    # can process
    prediction = model_inference_service.predict(
        list(apartment_features.model_dump().values()),
    )
    # return a prediction value
    return {'prediction': prediction}


@bp.post('/')
def get_prediction_post() -> dict:
    """
    Returns a prediction based on the JSON data.

    Returns:
        dict: A dictionary contraining the prediction result.
    """

    # getting and checking input parameters (feature values)
    # requests are embedded as json when sending a post request
    try:
        apartment_features = Apartment(**request.json)
    except ValidationError:
        abort(code=400, description='Bad input params')  # noqa: WPS432

    # feed input parameters to the loaded ml model to get a prediction
    # converts the validated input data into a format that the ML model
    # can process
    prediction = model_inference_service.predict(
        list(apartment_features.model_dump().values()),
    )
    # return a prediction value
    # prediction.item() to ensure Flask
    # can serialize the result properly and
    # Postman will get back clean JSON
    return {'prediction': prediction.item()}
