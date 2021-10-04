import os
from gevent.pywsgi import WSGIServer
from src import create_app

if __name__ == '__main__':
    app = create_app()

    SERVER_PORT = int(os.environ.get("PORT", "10101"))
    SERVER_IP = os.environ.get("HOST_IP", "0.0.0.0")

    server = WSGIServer((SERVER_IP, SERVER_PORT), app)

    print(f'Starting server on {SERVER_IP} with port {SERVER_PORT}')

    server.serve_forever()
