from flask import Blueprint, jsonify, request
from .obd_service import connect_to_obd, disconnect_obd, get_engine_voltage

main = Blueprint('main', __name__)

@main.route('/connect', methods=['POST'])
def connect():
    data = request.json
    bt_device = data.get('port')
    
    connection = connect_to_obd(bt_device)
    
    if connection:
        return jsonify({"status": "connected", "port": bt_device})
    else:
        return jsonify({"status": "failed", "message": "Could not connect to OBD-II device"}), 500

@main.route('/disconnect', methods=['POST'])
def disconnect():
    success = disconnect_obd()
    
    if success:
        return jsonify({"status": "disconnected"})
    else:
        return jsonify({"status": "error", "message": "No active connection to disconnect"}), 400

@main.route('/engine_voltage', methods=['GET'])
def engine_voltage():
    voltage = get_engine_voltage()
    
    if voltage != "No data":
        return jsonify({"engine_voltage": voltage})
    else:
        return jsonify({"status": "failed", "message": "Could not retrieve engine voltage"}), 500



#@main.route('/get_speed')
#def fetch_speed():
     #speed = get_speed()
     #return jsonify(speed)
 
