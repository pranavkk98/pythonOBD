from urllib import response
import obd
import serial

def connect_to_obd(port):
    global connection
    if connection is not None:
        return connection
    try:
        connection = obd.OBD(port=port)  
        return connection
    except serial.SerialException:
        return None

def disconnect_obd():
    global connection
    if connection:
        connection.close()
        connection = None
        return True
    return False

def get_engine_voltage():
  connection = obd.OBD() 
  voltage_cmd = obd.commands.GET_DTC
  response = connection.query(voltage_cmd)

  if response.value:
    return response.value.magnitude
  else:
    return "No data"  


