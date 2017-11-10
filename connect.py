import pexpect
import time

DEVICES = ["D9:04:7D:17:F7:80", "EF:DD:9C:D6:FB:6B"]

class Device:
    def __init__(self, address):
        self.MACaddress = address
        self.deviceHandle = connect(address)

    def readFrom(self.deviceHandle):
      print("reading from"),
      print(MACaddress)
      deviceHandle.sendline("char-write-req 0x0011 0100 -listen")
      
      while True:
       child.expect("Notification handle = 0x0010 value: ", timeout=10)
       child.expect("\r\n", timeout=10)
       print("Value: "),
       print(child.before),
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


