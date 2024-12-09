

# Swagger generated server

## Overview
This server was generated by the [swagger-codegen](https://github.com/swagger-api/swagger-codegen) project. By using the
[OpenAPI-Spec](https://github.com/swagger-api/swagger-core/wiki) from a remote server, you can easily generate a server stub.  This
is an example of building a swagger-enabled Flask server.

This example uses the [Connexion](https://github.com/zalando/connexion) library on top of Flask.

## Requirements
Python 3.5.2+

## Usage
To run the server, please execute the following from the root directory:

```
python3 -m venv .venv

source .venv/bin/activate

pip install -r requirements.txt

pip install 'connexion[swagger-ui]<3.0'

python3 -m swagger_server
```

and open your browser to here:

```
http://localhost:8080/ui/
```

Loki:
```
./loki-linux-amd64 -config.file=loki-local-config.yaml
```

Prometheus:

```
./promtail-linux-amd64 -config.file=promtail-local-config.yaml
```

Grafana:
```
docker run -d -p 3000:3000 --network host --name=grafana grafana/grafana
```

```bash
# building the image
docker build -t swagger_server .

# starting up a container
docker run -p 8080:8080 swagger_server
```

![Screenshot 2024-10-15 171752](https://github.com/user-attachments/assets/4cef5779-a9c2-4656-91c1-48d9b4daad20)
