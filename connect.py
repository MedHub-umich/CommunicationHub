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
        self.connectedDevs[-1].expect("Connection successful", timeout=1)
        connected = True
   
    except:
        print("Could not find "),
	print(MACaddress)
        self.connectedDevs = self.connectedDevs[:-1]  # pop
        connected = False
    return connected

def print2ByteFrom20Byte(devHandle):
	num0 = int(devHandle.before[3:5]+devHandle.before[0:2],16)
	num1 = int(devHandle.before[9:11]+devHandle.before[6:8],16)
	num2 = int(devHandle.before[15:17]+devHandle.before[12:14],16)
	num3 = int(devHandle.before[21:23]+devHandle.before[18:20],16)	
	num4 = int(devHandle.before[27:29]+devHandle.before[24:26],16)
	num5 = int(devHandle.before[33:35]+devHandle.before[30:32],16)
	num6 = int(devHandle.before[39:41]+devHandle.before[36:38],16)
	num7 = int(devHandle.before[45:47]+devHandle.before[42:44],16)	
	num8 = int(devHandle.before[51:53]+devHandle.before[48:50],16)	
	num9 = int(devHandle.before[57:59]+devHandle.before[54:56],16)	
	print num0
	print num1
	print num2
	print num3
	print num4
	print num5
	print num6
	print num7
	print num8
	print num9 
	return

def readFrom(devHandle):
    devHandle.sendline("char-write-req 0x0011 0100 -listen")
    
    while True:
        devHandle.expect("Notification handle = 0x0010 value: ", timeout=10)
        devHandle.expect("\r\n", timeout=10)
        #print("Value: "),
        #print(devHandle.before[0:5])
        print2ByteFrom20Byte(devHandle)

def writeTo(devHandle):
	devHandle.sendline()


