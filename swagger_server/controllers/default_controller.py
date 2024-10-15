import connexion
import six

from swagger_server.models.motorcycle import Motorcycle  # noqa: E501
from swagger_server import util
from flask import request

motorcycles = [
    {"id": 1, "brand": "Harley-Davidson", "model": "Iron 883"},
    {"id": 2, "brand": "Yamaha", "model": "YZF-R3"},
    {"id": 3, "brand": "Honda", "model": "CB500F"}
]


def motorcycles_get():  # noqa: E501
    """Get a list of all motorcycles

     # noqa: E501

      

    :rtype: List[Motorcycle]
    """
   
    return motorcycles, 200


def motorcycles_id_delete(id_):  # noqa: E501
    """Delete a motorcycle by ID
    """
    for motorcycle in motorcycles:
        if motorcycle['id'] == id_:
            motorcycles.remove(motorcycle)
            return 'Motorcycle removed', 200
        
    return {'message': 'Motorcycle not found'}, 404 


def motorcycles_id_get(id_):  # noqa: E501
    

    for motorcycle in motorcycles:
        if motorcycle['id'] == id_:
            return motorcycle, 200  # Return the motorcycle details and status 200

    return {'message': 'Motorcycle not found'}, 404  # Return 404 if not found


def motorcycles_id_put( id_):  # noqa: E501
    updated_data = request.json
    for motorcycle in motorcycles:
        if motorcycle['id'] == id_:
        # Update  motorcycle 
            motorcycle.update(updated_data)
            return motorcycle, 200  

    return {'message': 'Motorcycle not found'}, 404


def motorcycles_post(body):  # noqa: E501
    """Add a new motorcycle to the store

     # noqa: E501

    :param body: Motorcycle object to be added
    :type body: dict | bytes

    :rtype: None
    """
    new_motorcycle = request.json
    new_motorcycle['id'] = len(motorcycles) + 1
    motorcycles.append(new_motorcycle)


    if connexion.request.is_json:
        body = Motorcycle.from_dict(connexion.request.get_json())  # noqa: E501
    return new_motorcycle, 200
