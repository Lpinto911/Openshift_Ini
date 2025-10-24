#from flask import Flask

#app = Flask(__name__)

#@app.route('/', methods=['GET'])
#def hello_world():
#    return 'Hola Mundo', 200

#if __name__ == '__main__':
#    app.run(host='0.0.0.0', port=3000)
from flask import Flask, jsonify
import requests

app = Flask(__name__)

# URL del otro servicio en OpenShift
OTHER_SERVICE_URL = "http://mi-servicio-2.lpintofsgrp-dev.svc.cluster.local:4000/"

@app.route('/', methods=['GET'])
def hello_world():
    try:
        # Hace la petición GET al otro servicio
        response = requests.get(OTHER_SERVICE_URL, timeout=5)
        # Retorna el contenido de la otra app
        return response.text, response.status_code
    except requests.exceptions.RequestException as e:
        # Si hay un error al llamar al otro servicio
        return f"Error llamando al servicio remoto: {e}", 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
