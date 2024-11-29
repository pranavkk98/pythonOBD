from urllib import request
from flask import Blueprint, jsonify

from OBDApp.app import obd_service
#from .obd_service import get_engine_voltage, get_speed

main = Blueprint('main', __name__)


@main.route('/connect', methods=['POST'])
def connect():
    data = request.json
    bt_device = data.get('port')
    
    connection = obd_service.connect_to_obd(bt_device)

    if connection:
        return jsonify({"status": "connected", "port": bt_device})
    else:
        return jsonify({"status": "failed", "message": "Could not connect to OBD-II device"}), 500

# @main.route('/engine_voltage', methods=['GET'])
# def engine_voltage():
#     voltage = get_engine_voltage()
#     return jsonify({"engine_voltage": voltage})

@main.route('/disconnect', methods=['POST'])
def disconnect():
    success = obd_service.disconnect_obd()
    if success:
        return jsonify({"status": "disconnected"})
    else:
        return jsonify({"status": "error", "message": "No active connection to disconnect"}), 400

    


#@main.route('/get_speed')
#def fetch_speed():
     #speed = get_speed()
     #return jsonify(speed)
 
