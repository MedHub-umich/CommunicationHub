from unpackager import Unpackager, States
import unittest

class TestIngest(unittest.TestCase):

    def test_correct_checksum(self):
        testString = "f00412345678BA3C"
        unpack = Unpackager()
        self.assertEqual(unpack.ingest(testString), States.PACKEGE_COMPLETE)

    def test_incorrect_checksum(self):
        testString = "f00412345678BA3D"
        unpack = Unpackager()
        self.assertEqual(unpack.ingest(testString), States.PACKAGE_FAILED)

    #TODO: Write test for multiple strings
    def test_broken_up_over_data_messages(self):
        testString1 = "f0041234"
        testString2 = "5678BA3C"
        unpack = Unpackager()
        self.assertEqual(unpack.ingest(testString1), States.WAITING_FOR_END)
        self.assertEqual(unpack.ingest(testString2), States.PACKEGE_COMPLETE)
    
    def test_broken_up_over_size(self):
        testString1 = "f0"
        testString2 = "0412345678BA3C"
        unpack = Unpackager()
        self.assertEqual(unpack.ingest(testString1), States.WAITING_FOR_SIZE)
        self.assertEqual(unpack.ingest(testString2), States.PACKEGE_COMPLETE)

    def test_broken_up_over_checksum1(self):
        testString1 = "f00412345678"
        testString2 = "BA3C"
        unpack = Unpackager()
        self.assertEqual(unpack.ingest(testString1), States.WAITING_FOR_CHECKSUMBYTE1)
        self.assertEqual(unpack.ingest(testString2), States.PACKEGE_COMPLETE)

    def test_broken_up_over_checksum2(self):
        testString1 = "f00412345678BA"
        testString2 = "3C"
        unpack = Unpackager()
        self.assertEqual(unpack.ingest(testString1), States.WAITING_FOR_CHECKSUMBYTE2)
        self.assertEqual(unpack.ingest(testString2), States.PACKEGE_COMPLETE)

if __name__ == '__main__':
    unittest.main()