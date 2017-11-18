from bitstring import BitArray, BitStream

# Basically enum for stats
class States:
    WAITING_FOR_START = 0
    WAITING_FOR_SIZE = 1
    WAITING_FOR_END = 2

class Unpackager:
    START_BYTE = '\xf0'
    def __init__(self):
        self.buffer = BitArray()
        self.state = States.WAITING_FOR_START
        self.sizeLeft = 0
        BitArray.bytealigned = True
    
    def unpackage(self, message):
        # Ingest with context
        self.ingest(message)
        # React to shit
        pass
    
    
    def ingest(self, message):
        bitMessage = BitArray(hex=message)
        for byte in bitMessage.bytes:
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
                self.sizeLeft = ord(byte)
                self.state = States.WAITING_FOR_END
            elif (self.state == States.WAITING_FOR_END):
                print("Ingesting new packet for things")
            else:
                print ("improper or unhandled state of: ", self.state)

    def packetDone(self):
        return self.sizeLeft == 0
