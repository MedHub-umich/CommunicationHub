import pexpect
import time

DEVICES = ["D9:04:7D:17:F7:80", "EF:DD:9C:D6:FB:6B", "F3:C9:F9:A0:E9:6E"]

class Devices:
  def __init__(self):
    self.connectedDevs = []
    self.numDevices = 0

    for i in range(len(DEVICES)):
      connected = self.connect(DEVICES[i], i)

      if connected:
        self.numDevices += 1

    if self.numDevices == 0:
      print("No Devices Found")

    else:
      print("Connect to "),
      print(self.numDevices),
      print(" device(s)")

    return

  def connect(self, MACaddress, index):
    command = "sudo gatttool -i hci0 -t random  -b " + MACaddress + " -I"
    self.connectedDevs.append(pexpect.spawn(command))
    self.connectedDevs[-1].sendline("connect")
    
    try:
        self.connectedDevs[-1].expect("Connection successful", timeout=5)
        connected = True
   
    except:
        print("Could not find "),
	print(MACaddress)
        self.connectedDevs = self.connectedDevs[:-1]  # pop
        connected = False
    return connected

 	    
def readFrom(index):
    print("reading from"),
    print(self.MACaddress)
    self.connectedDevs[index].sendline("char-write-req 0x0011 0100 -listen")
    
    while True:
        self.connectedDevs[index].expect("Notification handle = 0x0010 value: ", timeout=10)
        self.connectedDevs[index].expect("\r\n", timeout=10)
        print("Value: "),
        print(self.connectedDevs[index].before),
        print("\n")




