import pexpect
import time

DEVICES = ["D9:04:7D:17:F7:80", "EF:DD:9C:D6:FB:6B"]


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
