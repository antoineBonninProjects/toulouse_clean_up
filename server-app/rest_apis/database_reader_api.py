from flask import jsonify

from database.database import LatestSigFoxMessages, SigFoxMessages, Session
from . import FlaskApp
from .crossdomain_decorator import crossdomain


class DatabaseReader():
    """
        A class to access data from our Database from a remote machine. It implement HTTP rest API services.
    """
    def __init__(self):
        self.app = FlaskApp

    @FlaskApp.route('/api/get_sigfox_messages/latest/weight/<device_id>', methods=['GET'])
    @crossdomain(origin='*')
    def get_latest_weight(device_id):
        """
        Returns a HTTP 200 OK with the latest weight for the given device (JSON formatted)

        Returns:
            json: A json representation of the latest device stored weight with HTTP 200 OK.
        """
        db_session = Session()
        qryresult = db_session.query(LatestSigFoxMessages).filter(LatestSigFoxMessages.device_id == device_id).one()
        weight = qryresult.weight;

        resp_json = jsonify({"weight": weight})
        db_session.close()

        return resp_json

    @FlaskApp.route('/api/get_sigfox_messages/latest', methods=['GET'])
    @crossdomain(origin='*')
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

    @FlaskApp.route('/api/get_sigfox_messages/all/<device_id>', methods=['GET'])
    @crossdomain(origin='*')
    def get_sigfox_messages_for_device(device_id):
        """
        Returns a 200 OK with the 'sigfox_messages' table content for a given device (JSON formatted)

        Args:
             device_id (str): the SigFox device id that has triggered the callback

        Returns:
            json: A json representation of the content of table sigfox_messages (for one device) with HTTP 200 OK.
        """
        db_session = Session()
        qryresult = db_session.query(SigFoxMessages).filter(SigFoxMessages.device_id == device_id)

        resp_json = jsonify(json_list=[i.serialize for i in qryresult])
        db_session.close()

        return resp_json
