# CommunicationHub
## Connecting the Pi to the Dev board using bluetoothctl
Run the the bash script to automatically connect to the dev board with the yellow tape on it. To change the device, follow the steps below to get the devices UUID and change the UUID in file.txt

## Working with bluetoothctl manually
  - Type 'bluetoothctl' in terminal 
  - Then 'agent-on'
  - Then 'scan on' and it will start displaying all devices and their UUIDs
  - Turn 'scan off' and then 'pair UUID' to pair with the device of your choosing
  - To connect type 'connect UUID' 
  - To make sure you are connected you can check the connection with 'info UUID>'
  
## Setting Up BluetoothLib
  - Install bluez via sudo apt-get install bluez
  - sudo gatttool -i hci0 -b <BLE_Address> -I  (example Yellow Taped Device has address D9:04:7D:17:F7:80) 
  - cha-write-req 0x0011 0100 -listen

## Setting up the CRC tool
  - Untar the crcmod tar file
  - Navigate into the folder from the untarring
  - run `python setup.py install`
  Reference this: https://pypi.python.org/pypi/crcmod

## Setting up bitstring (needed for unpack)
  - run `pip install bistring`
  
## Connecting the Pi to Internet in Lab
  - In terminal type: 
     - sudo route del default
     - sudo route add default gw 10.160 26.81
  - Open up chome
