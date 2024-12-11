import connexion
import six
import time
from swagger_server.models.motorcycle import Motorcycle  # noqa: E501
from swagger_server import util
from swagger_server.metrics import *
from swagger_server.logger import logger


def record_metrics(method, endpoint):
    REQUEST_COUNT.labels(method=method, endpoint=endpoint).inc()
    start_time = time.time()

    def observe_latency(status_code=None):
        duration = time.time() - start_time
        REQUEST_LATENCY.labels(method=method, endpoint=endpoint).observe(duration)
        if status_code:
            REQUEST_STATUS_CODES.labels(method=method, endpoint=endpoint, status_code=status_code).inc()

    return observe_latency

# Predefined list of motorcycles
motorcycles = [
    {"id": 1, "brand": "Harley-Davidson", "model": "Iron 883"},
    {"id": 2, "brand": "Yamaha", "model": "YZF-R3"},
    {"id": 3, "brand": "Honda", "model": "CB500F"}
]

def motorcycles_get():  # noqa: E501
    logger.info("Try GET /motorcycles")
    observer = record_metrics("GET", "/motorcycles")
    try:
        logger.info("GET /motorcycles endpoint accessed")
        observer(status_code="200")
        return "GET query success!"
    except Exception as e:
        observer(status_code="500")
        ERROR_COUNT.labels(method="GET", endpoint="/motorcycles").inc()
        logger.error(f"Error in GET /motorcycles: {str(e)}")
        return {"error": "Something went wrong"}, 500
   
    return motorcycles, 200


def motorcycles_id_delete(id_):  # noqa: E501
    """Delete a motorcycle by ID."""
    for motorcycle in motorcycles:
        if motorcycle['id'] == id_:
            motorcycles.remove(motorcycle)
            return 'Motorcycle removed', 200
    return {'message': 'Motorcycle not found'}, 404 

def motorcycles_id_get(id_):  # noqa: E501
    """Get a motorcycle by ID."""
    for motorcycle in motorcycles:
        if motorcycle['id'] == id_:
            return motorcycle, 200
    return {'message': 'Motorcycle not found'}, 404

def motorcycles_id_put(id_):  # noqa: E501
    """Update a motorcycle by ID."""
    updated_data = request.json
    for motorcycle in motorcycles:
        if motorcycle['id'] == id_:
            motorcycle.update(updated_data)
            return motorcycle, 200
    return {'message': 'Motorcycle not found'}, 404

def motorcycles_post(body):  # noqa: E501
    """Add a new motorcycle to the store."""
    new_motorcycle = request.json
    new_motorcycle['id'] = len(motorcycles) + 1
    motorcycles.append(new_motorcycle)
    return new_motorcycle, 200

