from flask import jsonify

from database.database import LatestSigFoxMessages, Session
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
