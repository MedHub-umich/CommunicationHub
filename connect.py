import pexpect
import time
import threading
from unpackager import Unpackager
#, "FA:9A:A3:54:EE:DA" is PCB 2
# "EC:B1:FE:A2:84:01", "D9:04:7D:17:F7:80", "EF:DD:9C:D6:FB:6B", "F3:C9:F9:A0:E9:6E", "E6:3B:21:18:45:51"
DEVICES = ["FA:9A:A3:54:EE:DA"]

class Device:
    def __init__(self, MACaddress, index):
        self.MACaddress = MACaddress
        self.parser = Unpackager(MACaddress)
        self.isConnected = False
        self.index = index

    def connect(self):
        command = "sudo gatttool -i hci0 -t random  -b " + self.MACaddress + " -I"
        self.devHandle = pexpect.spawn(command)
        self.devHandle.sendline("connect")
    
        try:
            self.devHandle.expect("Connection successful", timeout=2)
            self.isConnected = True
   
        except:
            print("Could not find "),
            print(self.MACaddress)
            self.isConnected = False


class DeviceContainer:
  def __init__(self):
    self.connectedDevs = []
    self.numDevices = 0
    self.readThreads = []
    return

  def connectDevices(self):  
    i = 0
    for i in range(len(DEVICES)):
        temp = Device(DEVICES[i], self.numDevices)
        temp.connect()

    	if temp.isConnected:
            print("device registered as connected")
            self.numDevices += 1
            self.connectedDevs.append(temp)
            self.readThreads.append(threading.Thread(target=readFromThread, args=(self, temp.index)))
            self.readThreads[temp.index].setDaemon(True)
            self.readThreads[temp.index].start()

    if (self.numDevices == 0):
        print("No Devices Found")

    else:
        print("Connect to "),
        print(self.numDevices),
        print(" device(s)")

    return self.connectedDevs

  def reconnect(self, index):
    # delete old readFrom thread and pexpect spawn
        self.connectedDevs[index].devHandle.terminate()
        print(self.readThreads[index].isAlive()) # TODO: slightly concerning that the thread is still alive...
        self.connectedDevs[index].connect()
        print("connected? "),
        print(self.connectedDevs[index].isConnected)

        # add new read thread
        while (self.connectedDevs[index].isConnected == False):
            self.connectedDevs[index].connect()

        self.readThreads[index] = threading.Thread(target=readFromThread, args=(self, index))
        self.readThreads[index].setDaemon(True)
        self.readThreads[index].start()
 	    
  def readFrom(self, index):
        self.connectedDevs[index].devHandle.sendline("char-write-req 0x0011 0100 -listen")
        print("Reading...")

        while True:
            if self.connectedDevs[index].parser.handle == False:
                quit()
            #TODO: Test the timeout thing
            i = self.connectedDevs[index].devHandle.expect([pexpect.TIMEOUT, pexpect.EOF, "Notification handle = 0x0010 value: "], timeout=3)
            if i == 0:
                print('Device disconnected')
                self.connectedDevs[index].isConnected = False
                self.reconnect(index)
                exit(1)
            elif i == 1:
                pass
            else:
                self.connectedDevs[index].devHandle.expect("\r\n")
                self.connectedDevs[index].parser.unpackage(self.connectedDevs[index].devHandle.before)

def readFromThread(connectedDevs, index):
    connectedDevs.readFrom(index)



def writeTo(device, data):
    command = "char-write-req 0x0019 " + data
    
    while device.isConnected == False:
        print("waiting to send..")
        time.sleep(2)

    device.devHandle.sendline(command)
    print("Write Successful")

def connect():
    BLEdevs = DeviceContainer()

    connectedDevs = BLEdevs.connectDevices()
    while(len(connectedDevs) == 0):
        connectedDevs = BLEdevs.connectDevices()

    return connectedDevs




