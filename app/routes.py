from flask import Blueprint, jsonify
#from .obd_service import get_engine_voltage, get_speed
from .emulator_service import initialize_elm, get_engine_voltage

main = Blueprint('main', __name__)


# Initialize the ELM emulator once
@main.route('/engine_voltage', methods=['GET'])
def engine_voltage():
    voltage = get_engine_voltage()
    return jsonify({"engine_voltage": voltage})


#@main.route('/get_speed')
#def fetch_speed():
     #speed = get_speed()
     #return jsonify(speed)
 
