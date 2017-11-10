# Using Hexiwear with Python
import pexpect
import time
 
DEVICE = "D9:04:7D:17:F7:80"
DEVICE2 = "EF:DD:9C:D6:FB:6B"

print(DEVICE)
 
# Run gatttool interactively.
print("Run gatttool...")
child = pexpect.spawn("sudo gatttool -i hci0 -t random -b D9:04:7D:17:F7:80 -I")
child2 = pexpect.spawn("sudo gatttool -i hci0 -t random -b EF:DD:9C:D6:FB:6B -I")
 
# Connect to the device.
print("Connecting to "),
print(DEVICE),
child.sendline("connect")
child.expect("Connection successful", timeout=5)
print(" Connected!")

print("Attempting to connect to second device")
child2.sendline("connect")
child2.expect("Connection successful", timeout=5)
print("Also connected!")
 
# function to transform hex string into signed integer
def hexStrToInt(hexstr):
    val = int(hexstr[0:2],16) + (int(hexstr[3:5],16)<<8)
    if ((val&0x8000)==0x8000): # treat signed 16-bits
        val = -((val^0xffff)+1)
    return val
 
#while True:
# Accelerometer
child.sendline("char-write-req 0x0011 0100 -listen")
child2.sendline("char-write-req 0x0011 0100 -listen")
while True:
   child.expect("Notification handle = 0x0010 value: ", timeout=10)
   child.expect("\r\n", timeout=10)
   print("Value: "),
   print(child.before),
   #print(hexStrToInt(child.before[0:5]))
   print("\n")

   child2.expect("Notification handle = 0x0010 value: ", timeout=10)
   child2.expect("\r\n", timeout=10)
   print("Second Value: "),
   print(child2.before),
   #print(hexStrToInt(child.before[0:5]))
   print("\n")




