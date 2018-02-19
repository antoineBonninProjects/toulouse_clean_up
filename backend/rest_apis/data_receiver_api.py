from flask import request, jsonify

from database.database import SigFoxMessages, LatestSigFoxMessages, Session
from . import FlaskApp


class DataReceiver():
    """
    A class that handles the reception of SigFox backend HTTP POST messages. It extracts the data contained in the JSON
    payload of the HTTP POST and appends it to the database table 'sigfox_messages'.
    """
    def __init__(self):
        self.app = FlaskApp

    @FlaskApp.route('/api/callback_handler/<device_id>', methods=['POST'])
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

        # Append message to 'sigfox_messages' table
        db_msg = SigFoxMessages()
        db_msg.device_id = json_msg["device"]
        db_msg.seq_num = json_msg["seq_num"]
        db_msg.weight = json_msg["weight"]
        db_session.add(db_msg)

        # Create 'latest_sigfox_messages' table entry or update it if existing for the current device_id
        if db_session.query(LatestSigFoxMessages).filter(LatestSigFoxMessages.device_id == device_id).count() == 0:
            latest_db_msg = LatestSigFoxMessages()
            latest_db_msg.device_id = json_msg["device"]
            latest_db_msg.seq_num = json_msg["seq_num"]
            latest_db_msg.weight = json_msg["weight"]
            db_session.add(latest_db_msg)
        else:
            entry_to_update = db_session.query(LatestSigFoxMessages).filter(LatestSigFoxMessages.device_id ==
                                                                            device_id).one()
            entry_to_update.seq_num = json_msg["seq_num"]
            entry_to_update.weight = json_msg["weight"]

        db_session.commit()
        db_session.close()

        return jsonify({"device_id": device_id})

    @FlaskApp.route('/api/get_sigfox_messages', methods=['GET'])
    def get_sigfox_messages():
        """
        Returns a 200 OK with the 'sigfox_messages' table content (JSON formatted)

        Returns:
            json: A json representation of the content of table sigfox_messages with HTTP 200 OK.
        """
        db_session = Session()
        qryresult = db_session.query(SigFoxMessages).all()

        resp_json = jsonify(json_list=[i.serialize for i in qryresult])
        db_session.close()

        return resp_json

    @FlaskApp.route('/api/get_latetst_sigfox_messages', methods=['GET'])
    def get_latest_sigfox_messages():
        """
        Returns a 200 OK with the 'latest_sigfox_messages' table content (JSON formatted)

        Returns:
            json: A json representation of the content of table sigfox_messages with HTTP 200 OK.
        """
        db_session = Session()
        qryresult = db_session.query(LatestSigFoxMessages).all()

        resp_json = jsonify(json_list=[i.serialize for i in qryresult])
        db_session.close()

        return resp_json
