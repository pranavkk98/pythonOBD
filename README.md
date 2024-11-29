# pythonOBD


Guide for running it
1)Clone this repo
2) do pip install -r requirements.txt
3) RUn the app using python3 run.py

4) dmesg | grep tty --> after pairing run this command
5) ls /dev/tty*  ---> command to check all available devices
6) You should see something like /dev/rfcomm0 (or another rfcomm number) which corresponds to the Bluetooth serial connection.

==========
curl -X POST http://localhost:5000/connect \
     -H "Content-Type: application/json" \
     -d '{"port": "/dev/cu.Bluetooth-Serial-Port"}'

The client side has to send the port no. which they get froom the bluetooth in ther request

How to get the port no. ?
1. Pair the Bluetooth Device
On macOS:

Go to System Preferences > Bluetooth and pair your OBD-II Bluetooth device.
After pairing, the device should be available as a serial port.

On Windows:

You can pair the device via the Bluetooth settings, and then Windows typically assigns a COM port (e.g., COM3).

2. Identify the Bluetooth Serial Port
Once the device is paired, you'll need to determine the exact serial port that the Bluetooth adapter is using for communication. This varies based on the operating system.

On macOS:

After pairing the OBD-II device, you can use the ls /dev/cu.* command in the terminal to find the Bluetooth serial port.
For example, it might show up as something like /dev/cu.Bluetooth-Serial-Port

On Windows:

In the Device Manager, you can find the Bluetooth device under Ports (COM & LPT), and it will display something like COM3 or another COM port.

^^^The above one is for testing

The js code to get the port no.

The navigator.bluetoot.requestDevice would promt the user to select a device, once the device has been selected, the user will be able to extract the useful info

  const device = await navigator.bluetooth.requestDevice({
                filters: [{ services: ['0000fee7-0000-1000-8000-00805f9b34fb'] }] 
            });
            console.log('Device selected:', device.name);

const btPort = device.gatt.connected ? device.gatt.server.device.gatt.connected : null;



