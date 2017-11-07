# CommunicationHub
## Connecting the Pi to the Dev board using bluetoothctl
Run the the bash script to automatically connect to the dev board with the yellow tape on it

## Working with bluetoothctl manually
  - Type 'bluetoothctl' in terminal 
  - Then 'agent-on'
  - Then 'scan on' and it will start displaying all devices and their UUIDs
  - Turn 'scan off' and then 'pair UUID' to pair with the device of your choosing
  - To connect type 'connect UUID' 
  - To make sure you are connected you can check the connection with 'info UUID>'
  
