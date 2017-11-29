class PacketTypes:
    HEART_RATE = 3
    ECG = 2
    BREATHING_RATE = 4
    TEMPERATURE = 5
    BLOOD_PRESSURE = 1


class Contextualizer:
    MIN_PACKET_SIZE = 6

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
            return

        typeNum = ord(packBytes[Contextualizer.TYPE_INDEX])

        #router
        if (typeNum == PacketTypes.HEART_RATE):
            Contextualizer.handle_heart_rate(unpacker)
        elif (typeNum == PacketTypes.ECG):
            Contextualizer.handle_ecg(unpacker)
        elif (typeNum == PacketTypes.BREATHING_RATE):
            Contextualizer.handle_breathing_rate(unpacker)
        elif (typeNum == PacketTypes.TEMPERATURE):
            Contextualizer.handle_temperature(unpacker)
        elif (typeNum == PacketTypes.BLOOD_PRESSURE):
            Contextualizer.handle_blood_pressure(unpacker)


    @staticmethod
    def handle_heart_rate(unpacker):
        print("In heart rate!")
    
    @staticmethod
    def handle_ecg(unpacker):
        print("In ecg!")
    
    @staticmethod
    def handle_breathing_rate(unpacker):
        print("In breathinG rate!")
    
    @staticmethod
    def handle_temperature(unpacker):
        print("In temperature!")

    @staticmethod
    def handle_blood_pressure(unpacker):
        print("In blood pressure!")
