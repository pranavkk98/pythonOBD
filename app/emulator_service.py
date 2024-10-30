from elm import Elm

# Initialize the ELM emulator
def initialize_elm():
    emulator = Elm(
        batch_mode=False,
        newline=False,
        serial_port="",  # Specify if needed for Windows
        serial_baudrate="",
        net_port=8080,  # Example port for TCP/IP connection
        forward_net_host=None,
        forward_net_port=None,
        forward_serial_port=None,
        forward_serial_baudrate=None,
        forward_timeout=5.0
    )
    return emulator

def get_engine_voltage(emulator):
    # Query the engine voltage (replace with appropriate command)
    command = "01 0C"  # Example command to get RPM; replace with correct for voltage
    response = emulator.query(command)
    
    if response:
        return response  # Return the response or extract the voltage value
    else:
        return "No data"
