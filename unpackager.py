from bitstring import BitArray, BitStream
import crcmod

# Basically enum for stats
class States:
    WAITING_FOR_START = 0
    WAITING_FOR_SIZE = 1
    WAITING_FOR_END = 2
    WAITING_FOR_CHECKSUMBYTE1 = 3
    WAITING_FOR_CHECKSUMBYTE2 = 4

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
        return self.ingest(message)
        # React to shit
        pass
    
    
    def ingest(self, message):
        bitMessage = BitArray(hex=message)
        for byte in bitMessage.bytes:
            print("In state ", self.state)
            byteHex = '0x' + byte.encode("hex")
            if (self.state == States.WAITING_FOR_START):
                if byte == Unpackager.START_BYTE:
                    # loop through bits and check for start
                    print("Found start byte")
                    self.buffer.append(byteHex)
                    self.state = States.WAITING_FOR_SIZE
                else:
                    print("found byte, but is not start so discarding")

            elif (self.state == States.WAITING_FOR_SIZE):
                print("Byte interpreted as size of ", ord(byte))
                self.buffer.append(byteHex)
                self.size = ord(byte)
                self.packetsIngested = 0
                self.state = States.WAITING_FOR_END

            elif (self.state == States.WAITING_FOR_END):
                print("Ingesting new packet for things")
                self.buffer.append(byteHex)
                self.data.append(byteHex)
                self.packetsIngested += 1
            elif (self.state == States.WAITING_FOR_CHECKSUMBYTE1):
                print("Handling MSB of checksum")
                self.checksum = ord(byte) << 8
                self.buffer.append(byteHex)
                self.state = States.WAITING_FOR_CHECKSUMBYTE2
            elif (self.state == States.WAITING_FOR_CHECKSUMBYTE2):
                print("Handling LSB of checksum")
                self.checksum += ord(byte)
                self.buffer.append(byteHex)
                return self.handleFullPacket()
            else:
                print ("improper or unhandled state of: ", self.state)
            
            # check if we've reached the "end" of a packet
            if (self.packetDone()):
                print("Packet was completed")
                self.state = States.WAITING_FOR_CHECKSUMBYTE1
        # if we are here, return 1 for not done yet
        return 1

    def packetDone(self):
        return self.packetsIngested == self.size and self.state == States.WAITING_FOR_END

    def handleFullPacket(self):
        if(self.calculateCRC()):
            print("Checksum passed")
            return 2
        else :
            print ("Checksum failed")
            return 0

    def calculateCRC(self):
        # print("Data is: ")
        # for byte in self.data.bytes:
        #     print(byte.encode("hex")),
        # print("Checksum is:"),
        return self.crcfunc(self.data.bytes) == self.checksum


