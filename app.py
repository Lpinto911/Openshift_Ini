from flask import Flask
import requests

from flask import Flask
import requests

app = Flask(__name__)

# URL del otro servicio en OpenShift
OTHER_SERVICE_URL = "http://mi-servicio-2.lpintofsgrp-dev.svc.cluster.local:4000/"

@app.route('/', methods=['GET'])
def hello_world():
    try:
        # Llama al otro servicio
        response = requests.get(OTHER_SERVICE_URL, timeout=5)
        return response.text, response.status_code
    except requests.exceptions.RequestException as e:
        return f"Error llamando al servicio remoto: {e}", 500

# 👇 Agrega estas rutas para las probes
@app.route('/startup')
def startup():
    return "OK", 200

@app.route('/readiness')
def readiness():
    return "READY", 200

@app.route('/health')
def health():
    return "HEALTHY", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
