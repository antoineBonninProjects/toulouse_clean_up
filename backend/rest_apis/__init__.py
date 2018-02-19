from flask import Flask
from multiprocessing import Process
import os

FlaskApp = Flask(__name__)
"""
The flask application.
"""


class FlaskAppLauncher(Process):
    """
    A class that starts a Flask HTTP server. The Flask server allows us to create GET/POST API services and bind them to
    URLs.
    """

    def __init__(self):
        self.app = FlaskApp
        super().__init__()

    def run(self):
        """
        Overrides the Process run method and starts a Flask server.
        """
        port = int(os.environ.get('PORT', 5000))
        self.app.run(host='0.0.0.0', port=port, debug=True)