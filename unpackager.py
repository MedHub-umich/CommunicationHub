from bitstring import BitArray
from enum import enum

# Basically enum for stats
class States:
    WAITING_FOR_START = 0
    WAITING_FOR_END = 1

class Unpackager:
    def __init__(self):
        self.buffer = BitArray()
        self.state = States.WAITING_FOR_START
    
    def unpackage(self, message):
        # translate to bits
        self.ingest(message)
        # feed into reader
        # update python state and react
        pass
    
    
    def ingest(self, message):
        bitMessage = BitArray(hex=message)
        print(bitMessage.hex)
        if (state == States.WAITING_FOR_START):
            # loop through bits and check for start
            pass