from unpackager import Unpackager, States
import unittest

class TestIngest(unittest.TestCase):

    def test_correct_checksum(self):
        testString = "f00412345678BA3C"
        unpack = Unpackager()
        self.assertEqual(unpack.ingest(testString), States.WAITING_FOR_START)

    def test_incorrect_checksum(self):
        testString = "f00412345678BA3D"
        unpack = Unpackager()
        self.assertEqual(unpack.ingest(testString), States.WAITING_FOR_START)

    #TODO: Write test for multiple strings
    def test_broken_up_over_data_messages(self):
        testString1 = "f0041234"
        testString2 = "5678BA3C"
        unpack = Unpackager()
        self.assertEqual(unpack.ingest(testString1), States.WAITING_FOR_END)
        self.assertEqual(unpack.ingest(testString2), States.WAITING_FOR_START)
    
    def test_broken_up_over_size(self):
        testString1 = "f0"
        testString2 = "0412345678BA3C"
        unpack = Unpackager()
        self.assertEqual(unpack.ingest(testString1), States.WAITING_FOR_SIZE)
        self.assertEqual(unpack.ingest(testString2), States.WAITING_FOR_START)

    def test_broken_up_over_checksum1(self):
        testString1 = "f00412345678"
        testString2 = "BA3C"
        unpack = Unpackager()
        self.assertEqual(unpack.ingest(testString1), States.WAITING_FOR_CHECKSUMBYTE1)
        self.assertEqual(unpack.ingest(testString2), States.WAITING_FOR_START)

    def test_broken_up_over_checksum2(self):
        testString1 = "f00412345678BA"
        testString2 = "3C"
        unpack = Unpackager()
        self.assertEqual(unpack.ingest(testString1), States.WAITING_FOR_CHECKSUMBYTE2)
        self.assertEqual(unpack.ingest(testString2), States.WAITING_FOR_START)

class TestContexualizer(unittest.TestCase):

    def test_empty_packet_heart(self):
        print("HERE!")
        testString = "f0061111050000007C54"
        unpack = Unpackager()
        unpack.ingest(testString)

    def test_empty_packet_ecg(self):
        print("HERE!")
        testString = "f0061111050000016C75"
        unpack = Unpackager()
        unpack.ingest(testString)

    def test_empty_packet_breathing_rate(self):
        print("HERE!")
        testString = "f0061111050000025C16"
        unpack = Unpackager()
        unpack.ingest(testString)

    def test_empty_packet_tempearture(self):
        print("HERE!")
        testString = "f0061111050000043CD0"
        unpack = Unpackager()
        unpack.ingest(testString)

if __name__ == '__main__':
    unittest.main()