from flask import Flask, request, jsonify
from multiprocessing import Process, Manager
import os

from database.database import SigFoxMessages, Session

app = Flask(__name__)
"""
The flask application.
"""

class DataReceiver(Process):
    """
    A class that handles the reception of SigFox backend HTTP POST messages. It extracts the data contained in the JSON
    payload of the HTTP POST and appends it to a queue.
    """
    def run(self):
        port = int(os.environ.get('PORT', 5000))
        app.run(host='0.0.0.0', port=port, debug=True)

    @app.route('/api/callback_handler/<device_id>', methods=['POST'])
    def callback_handler(device_id):
        """
        Receives the json formatted callback message from a given sigfox device.
        It stores the information into the database.

        Args:
             device_id (str): the SigFox device id that has triggered the callback

        Returns:
            json: The device_id as a response with HTTP 200 OK.
        """
        json_msg = request.json

        db_session = Session()
        db_msg = SigFoxMessages()
        db_msg.device_id = json_msg["device"]
        db_msg.seq_num = json_msg["seq_num"]
        db_msg.weight = json_msg["weight"]

        db_session.add(db_msg)
        db_session.commit()
        db_session.close()

        return jsonify({"device_id":device_id})

    @app.route('/api/get_sigfox_messages', methods=['GET'])
    def get_sigfox_messages():
        """
        Displays the sigfox messages that has been stored in database in the web browser (JSON formatted)


        Returns:
            json: A json representation of the content of table sigfox_messages with HTTP 200 OK.
        """
        db_session = Session()
        qryresult = db_session.query(SigFoxMessages).all()

        json_list = [i.serialize for i in qryresult]
        print(type(json_list[0]))

        resp_json = jsonify(json_list=[i.serialize for i in qryresult])
        db_session.close()

        return resp_json
