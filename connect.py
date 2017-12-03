import pexpect
import time
import threading
from unpackager import Unpackager

DEVICES = ["EC:B1:FE:A2:84:01", "D9:04:7D:17:F7:80", "EF:DD:9C:D6:FB:6B", "F3:C9:F9:A0:E9:6E", "E6:3B:21:18:45:51", "FA:9A:A3:54:EE:DA"]

class Device:
    def __init__(self, MACaddress, devHandle):
        self.MACaddress = MACaddress
        self.devHandle = devHandle
        self.parser = Unpackager(MACaddress)
        self.isConnected = True
        self.readThread = threading.Thread(target=readFrom, args=(self,))
        self.readThread.setDaemon(True)
        #self.writeThread

class DeviceContainer:
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
    self.connectedDevs.append(Device(MACaddress, pexpect.spawn(command)))
    self.connectedDevs[-1].devHandle.sendline("connect")
    
    try:
        self.connectedDevs[-1].devHandle.expect("Connection successful", timeout=2)
        connected = True
   
    except:
        print("Could not find "),
	print(MACaddress)
        self.connectedDevs = self.connectedDevs[:-1]  # pop
        connected = False
    return connected

 	    
def readFrom(device):
    device.devHandle.sendline("char-write-req 0x0011 0100 -listen")
    print("Reading...")
    
    while True:
        if device.parser.handle == False:
            quit()
        i = device.devHandle.expect([pexpect.TIMEOUT, pexpect.EOF, "Notification handle = 0x0010 value: "], timeout=10)
        if i == 0:
            print('Device disconnected')
        elif i == 1:
            pass
        else:
            device.devHandle.expect("\r\n")
            # print("Processing:"),
            # print(device.devHandle.before),
            # print("\n")
            device.parser.unpackage(device.devHandle.before)



def writeTo(devHandle, data):
    command = "char-write-req 0x0019 " + data
    devHandle.sendline(command)
    print("Write Successful")

def startRead(device):
    #device.readThread.setDaemon(True)
    device.readThread.start()



