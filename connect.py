import pexpect
import time

DEVICES = ["D9:04:7D:17:F7:80", "EF:DD:9C:D6:FB:6B", "F3:C9:F9:A0:E9:6E"]

class Device:
    def __init__(self, address):
        self.MACaddress = address
	self.numDevice = 0

	try:
            self.deviceHandle = connect(DEVICES[0])
	    self.numDevices += 1
	    break
	try:
	    self.deviceHandle2 = connect(DEVICES[1])
	    self.numDevices += 1
            break
	try:
	    self.deviceHandle3 = connect(DEVICES[2])
	    self.numDevices += 1
    	    break

        except NoConnection:
 	    print("No Devices Found")

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



def connect(MACaddress):
  print("Connecting to device"),
  print(MACaddress)

  command = "sudo gatttool -i hci0 -t random -b " + MACaddress + " -I"
  child = pexpect.spawn(command)
  child.sendline("connect")
  child.expect("Connection successful", timeout=5)
  print(" Connected to "),
  print(MACaddress),
  print("!")
  return child

def scan():
  print("Scanning for devices...")
  child = pexpect.spawn("sudo hcitool lescan")
  print(child)


