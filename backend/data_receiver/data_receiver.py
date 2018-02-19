from flask import Flask, request, jsonify
from multiprocessing import Process, Manager
import os

app = Flask(__name__)
manager = Manager()
storage = manager.dict()

class DataReceiver(Process):
    """
    A class that handles the reception of SigFox backend HTTP POST messages. It extracts the data contained in the JSON
    payload of the HTTP POST and appends it to a queue.
    """

    def __init__(self):
        super().__init__()
        storage["content"] = {"None": "0"}

    def run(self):
        port = int(os.environ.get('PORT', 5000))
        app.run(host='0.0.0.0', port=port, debug=True)

    @app.route('/api/callback_handler/<device_id>', methods=['POST'])
    def callback_handler(device_id):
        """
        Receives the json formatted callback message from a given sigfox device.
        It stores the information into the database.
        Returns: the device_id as a response with HTTP event 200 to notify everything is ok.
        """
        storage["content"] = request.json
        print("temp: {}".format(storage["content"]['temp']))
        print("bitfield[0]: {}".format(storage["content"]['0']))
        print("bitfield[1]: {}".format(storage["content"]['1']))
        print("bitfield[2]: {}".format(storage["content"]['2']))
        return jsonify({"device_id":device_id})
