#!/usr/bin/env python3

import time
import connexion

from swagger_server import encoder
from prometheus_client import start_http_server
from swagger_server.metrics import *

def main():
    start_http_server(8001)
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'Motorcycle Store API'}, pythonic_params=True)
    app.run(port=8080)


if __name__ == '__main__':
    main()
