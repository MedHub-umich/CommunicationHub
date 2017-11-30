from bitstring import BitArray, BitStream
from contextualizer import Contextualizer
import crcmod

# Basically enum for stats
class States:
    WAITING_FOR_START = 0
    WAITING_FOR_SIZE = 1
    WAITING_FOR_END = 2
    WAITING_FOR_CHECKSUMBYTE1 = 3
    WAITING_FOR_CHECKSUMBYTE2 = 4
    PACKAGE_COMPLETE = 5
    PACKAGE_FAILED = -1

class Unpackager:
    START_BYTE = '\xf0'
    def __init__(self, MAC_ADDRESS):
        self.resetPackager()
        self.MAC_ADDRESS = MAC_ADDRESS
        BitArray.bytealigned = True
        self.crcfunc = crcmod.mkCrcFun(0x11021, initCrc=0x1d0f, rev=False, xorOut=0x0000)
    
    def unpackage(self, message):
        # Ingest with context
        response = self.ingest(message)
        #if (response == States.PACKAGE_FAILED):
         #   print "Discarding packet for whatever reason, SALT THE EARTH"
        #elif(response < States.PACKAGE_COMPLETE):
         #   print "Still waiting for EOP"
        #elif(response  == States.PACKAGE_COMPLETE):
          #  print "Package was completed, please handle"
    
    def resetPackager(self):
        self.buffer = BitArray()
        self.state = States.WAITING_FOR_START
        self.size = 0
        self.data = BitArray()
        self.packetsIngested = 0
        self.checksum = 0

    def ingest(self, message):
        bitMessage = BitArray(hex=message)
        for byte in bitMessage.bytes:
            byteHex = '0x' + byte.encode("hex")
            if (self.state == States.WAITING_FOR_START):
                if byte == Unpackager.START_BYTE:
                    # loop through bits and check for start
                    self.buffer.append(byteHex)
                    # print("Found start byte")
                    self.state = States.WAITING_FOR_SIZE
                else:
                    print(byteHex)
                    print("found byte, but is not start so discarding")                

            elif (self.state == States.WAITING_FOR_SIZE):
                self.buffer.append(byteHex)
                self.size = ord(byte)
                # print(self.size)
                self.packetsIngested = 0
                self.state = States.WAITING_FOR_END
                #check that size is 0
                if (self.size == 0):
                    print("Invalid package (size invalid), discarding")
                    self.resetPackager()

            elif (self.state == States.WAITING_FOR_END):
                self.buffer.append(byteHex)
                self.data.append(byteHex)
                self.packetsIngested += 1
                # check if we've reached the "end" of a packet
                if (self.allDataRecieved()):
                    self.state = States.WAITING_FOR_CHECKSUMBYTE1
            elif (self.state == States.WAITING_FOR_CHECKSUMBYTE1):
                self.checksum = ord(byte) 
                self.buffer.append(byteHex)
                self.state = States.WAITING_FOR_CHECKSUMBYTE2
            elif (self.state == States.WAITING_FOR_CHECKSUMBYTE2):
                self.checksum += ord(byte) << 8
                self.buffer.append(byteHex)
                self.handleFullPacket(message)
            else:
                print ("improper or unhandled state of: ", self.state)
            
            
        # if we are here, return 1 for not done yet
        return self.state

    def allDataRecieved(self):
        return self.packetsIngested == self.size and self.state == States.WAITING_FOR_END

    def handleFullPacket(self, message):
        #TODO: Call actual typing and handling here
        # print(self.crcfunc(self.data.bytes))
        if(self.calculateCRC() and self.size != 0):
            self.state = States.PACKAGE_COMPLETE
            Contextualizer.contextualize(self)
        else:
            print("failed")
            print(message)
            print(self.buffer)
            
        
        self.resetPackager()

    def calculateCRC(self):
        return self.crcfunc(self.data.bytes) == self.checksum


