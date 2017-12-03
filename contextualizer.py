from datetime import datetime
from config import *
import requests
import worker

class Contextualizer:
    MIN_PACKET_SIZE = 4

    START_INDEX = 0
    SIZE_INDEX = 1
    SEQUENCE_INDEX = 2
    RESERVED_START_INDEX = 3
    RESERVED_END_EXCLUSIVE = 5
    TYPE_INDEX = 5
    DATA_START_INDEX = 6

    @staticmethod
    def contextualize(unpacker):
        packBytes = unpacker.buffer.bytes
        if unpacker.size < Contextualizer.MIN_PACKET_SIZE:
            # invalid packet size, return
            print("MIN PACKET SIZE")
            return

        typeNum = ord(packBytes[Contextualizer.TYPE_INDEX])
        Contextualizer.handlePacket(unpacker, typeNum)


    @staticmethod
    def handlePacket(unpacker, packetType):
        dataPackets = unpacker.data[4:]
        json = {
            "user": MACtranslation[unpacker.MAC_ADDRESS],
            "type": packetType,
            "time": Contextualizer.getTime(),
            "data": dataPackets.hex,
        }
        Contextualizer.addToQueue(unpacker, packetType, json)
        printInfo(unpacker)
        print(dataPackets.hex)

    @staticmethod
    def getTime():
        return str(datetime.now())

    @staticmethod
    def addToQueue(unpacker, packetType, jsonData):
        unpacker.queueDict[packetType].append(jsonData)
        if (len(unpacker.queueDict[packetType]) > QueueLimits[packetType]):
            finalData = {
                "packets": unpacker.queueDict[packetType]
            }
            print("About to send the following type of data", packetType)
            # requests.post(add_data_url, json=finalData)
            worker.worker(add_data_url, finalData)
            print("unblocked")
            unpacker.queueDict[packetType] = []

            


def printInfo(unpacker):
    # print("For device: "),
    # print (unpacker.MAC_ADDRESS)
    # print("The time is: "),
    Contextualizer.getTime()
