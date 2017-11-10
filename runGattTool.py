# Using Hexiwear with Python
import pexpect
import time
 
DEVICE = "D9:04:7D:17:F7:80"
 
print("Hexiwear address:"),
print(DEVICE)
 
# Run gatttool interactively.
print("Run gatttool...")
child = pexpect.spawn("sudo gatttool -i hci0 -t random -b D9:04:7D:17:F7:80 -I")
 
# Connect to the device.
print("Connecting to "),
print(DEVICE),
child.sendline("connect")
child.expect("Connection successful", timeout=5)
print(" Connected!")
 
# function to transform hex string like "0a cd" into signed integer
def hexStrToInt(hexstr):
    val = int(hexstr[0:2],16) + (int(hexstr[3:5],16)<<8)
    if ((val&0x8000)==0x8000): # treat signed 16bits
        val = -((val^0xffff)+1)
    return val
 
#while True:
# Accelerometer
child.sendline("char-write-req 0x0011 0100 -listen")
while True:
    child.expect("Notification handle = 0x0010 value: ", timeout=10)
    child.expect("\r\n", timeout=10)
    print("Value: "),
    print(child.before),
    #print(hexStrToInt(child.before[0:5]))
