from urllib import response
import obd
def get_engine_voltage():
  #connection = obd.OBD()
  connection = obd.OBD() 
  voltage_cmd = obd.commands.GET_DTC
  response = connection.query(voltage_cmd)

  if response.value:
    return response.value.magnitude
  else:
    return "No data"  


