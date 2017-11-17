import pexpect
import time

DEVICES = ["D9:04:7D:17:F7:80", "EF:DD:9C:D6:FB:6B", "F3:C9:F9:A0:E9:6E", "E6:3B:21:18:45:51"]

class Devices:
  def __init__(self):
    self.connectedDevs = []
    self.numDevices = 0
    return

  def connectDevices(self):  
    for i in range(len(DEVICES)):
        connected = self.connectSingle(DEVICES[i], i)

    	if connected:
          self.numDevices += 1

    if (self.numDevices == 0):
        print("No Devices Found")

    else:
        print("Connect to "),
        print(self.numDevices),
        print(" device(s)")

    return self.connectedDevs

  def connectSingle(self, MACaddress, index):
    command = "sudo gatttool -i hci0 -t random  -b " + MACaddress + " -I"
    self.connectedDevs.append(pexpect.spawn(command))
    self.connectedDevs[-1].sendline("connect")
    
    try:
        self.connectedDevs[-1].expect("Connection successful", timeout=2)
        connected = True
   
    except:
        print("Could not find "),
	print(MACaddress)
        self.connectedDevs = self.connectedDevs[:-1]  # pop
        connected = False
    return connected

 	    
def readFrom(devHandle):
    devHandle.sendline("char-write-req 0x0011 0100 -listen")
    
    while True:
        devHandle.expect("Notification handle = 0x0010 value: ", timeout=10)
        devHandle.expect("\r\n", timeout=10)
        print("Value: "),
        print(devHandle.before),
        print("\n")

def writeTo(devHandle, data):
    command = "char-write-req 0x0019 " + data
    devHandle.sendline(command)
    print("Write Successful")



