import pexpect
import time

DEVICES = ["D9:04:7D:17:F7:80", "EF:DD:9C:D6:FB:6B", "F3:C9:F9:A0:E9:6E"]

class Device:
  def __init__(self, address):
    self.MACaddress = address
    self.numDevice = 0

    for i in DEVICES:
      connected = connect(i)

      if connected:
        self.numDevices += 1

    if self.numDevices == 0:
      print("No Devices Found")

    else:
      print("Connect to "),
      print(self.numDevices),
      print(" devices")

  def connect(self, MACaddress):
    command = "sudo gatttool -i hci0 -t random  -b " + MACaddress + " -I"
    self.deviceHandle = pexpect.spawn(command)
    self.deviceHandle.sendline("connect")
    self.deviceHandle.expect("Connection successful", timeout=5)
 	    
  def readFrom(self):

    print("reading from"),
    print(self.MACaddress)
    self.deviceHandle.sendline("char-write-req 0x0011 0100 -listen")
    
    while True:
     self.deviceHandle.expect("Notification handle = 0x0010 value: ", timeout=10)
     self.deviceHandle.expect("\r\n", timeout=10)
     print("Value: "),
     print(self.deviceHandle.before),
     print("\n")




