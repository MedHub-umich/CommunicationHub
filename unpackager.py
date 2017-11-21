from bitstring import BitArray, BitStream
import crcmod

# Basically enum for stats
class States:
    WAITING_FOR_START = 0
    WAITING_FOR_SIZE = 1
    WAITING_FOR_END = 2
    WAITING_FOR_CHECKSUMBYTE1 = 3
    WAITING_FOR_CHECKSUMBYTE2 = 4
    PACKEGE_COMPLETE = 5
    PACKAGE_FAILED = -1

class Unpackager:
    START_BYTE = '\xf0'
    def __init__(self):
        self.buffer = BitArray()
        self.state = States.WAITING_FOR_START
        self.size = 0
        self.data = BitArray()
        self.packetsIngested = 0
        self.checksum = 0
        BitArray.bytealigned = True
        self.crcfunc = crcmod.mkCrcFun(0x11021, initCrc=0x1d0f, rev=False, xorOut=0x0000)
    
    def unpackage(self, message):
        # Ingest with context
        if (self.ingest(message) == PACKAGE_FAILED):
            print "Discarding packet for whatever reason, SALT THE EARTH"
        elif(self.ingest(message) < PACKAGE_COMPLETE):
            print "Still waiting for EOP"
        elif(self.ingest(message) == PACKAGE_COMPLETE):
            print "Package was completed, please handle"
        # React to shit
        pass
    
    
    def ingest(self, message):
        bitMessage = BitArray(hex=message)
        for byte in bitMessage.bytes:
            byteHex = '0x' + byte.encode("hex")
            if (self.state == States.WAITING_FOR_START):
                if byte == Unpackager.START_BYTE:
                    # loop through bits and check for start
                    self.buffer.append(byteHex)
                    self.state = States.WAITING_FOR_SIZE
                else:
                    print("found byte, but is not start so discarding")                    

            elif (self.state == States.WAITING_FOR_SIZE):
                self.buffer.append(byteHex)
                self.size = ord(byte)
                self.packetsIngested = 0
                self.state = States.WAITING_FOR_END

            elif (self.state == States.WAITING_FOR_END):
                self.buffer.append(byteHex)
                self.data.append(byteHex)
                self.packetsIngested += 1
                self.state
            elif (self.state == States.WAITING_FOR_CHECKSUMBYTE1):
                self.checksum = ord(byte) << 8
                self.buffer.append(byteHex)
                self.state = States.WAITING_FOR_CHECKSUMBYTE2
            elif (self.state == States.WAITING_FOR_CHECKSUMBYTE2):
                self.checksum += ord(byte)
                self.buffer.append(byteHex)
                self.state = self.handleFullPacket()
            else:
                print ("improper or unhandled state of: ", self.state)
            
            # check if we've reached the "end" of a packet
            if (self.allDataRecieved()):
                self.state = States.WAITING_FOR_CHECKSUMBYTE1
        # if we are here, return 1 for not done yet
        return self.state

    def allDataRecieved(self):
        return self.packetsIngested == self.size and self.state == States.WAITING_FOR_END

    def handleFullPacket(self):
        #TODO: Call actual typing and handling here
        if(self.calculateCRC()):
            return States.PACKEGE_COMPLETE
        else :
            return States.PACKAGE_FAILED

    def calculateCRC(self):
        return self.crcfunc(self.data.bytes) == self.checksum


