from unpackager import Unpackager
import unittest

class TestUnpackager(unittest.TestCase):

    def test_correct_checksum(self):
        testString = "f00412345678BA3C"
        unpack = Unpackager()
        self.assertEqual(unpack.ingest(testString), 2)

    def test_incorrect_checksum(self):
        testString = "f00412345678BA3D"
        unpack = Unpackager()
        self.assertEqual(unpack.ingest(testString), 0)

    #TODO: Write test for multiple strings
    def test_broken_up_over_data_messages(self):
        testString1 = "f0041234"
        testString2 = "5678BA3C"
        unpack = Unpackager()
        self.assertEqual(unpack.ingest(testString1), 1)
        self.assertEqual(unpack.ingest(testString2), 2)
    
    def test_broken_up_over_size(self):
        testString1 = "f0"
        testString2 = "0412345678BA3C"
        unpack = Unpackager()
        self.assertEqual(unpack.ingest(testString1), 1)
        self.assertEqual(unpack.ingest(testString2), 2)

    def test_broken_up_over_checksum1(self):
        testString1 = "f00412345678"
        testString2 = "BA3C"
        unpack = Unpackager()
        self.assertEqual(unpack.ingest(testString1), 1)
        self.assertEqual(unpack.ingest(testString2), 2)

    def test_broken_up_over_checksum2(self):
        testString1 = "f00412345678BA"
        testString2 = "3C"
        unpack = Unpackager()
        self.assertEqual(unpack.ingest(testString1), 1)
        self.assertEqual(unpack.ingest(testString2), 2)
        
testStrings = [
    # "f000", #no size
    # "f00100", #size 1
    # "f034", #size52
    # "94f0029811", #not initial packet
    "f00412345678BA3C", #correct checksum
    "f00412345678BA3D", #incorrect checksum
]

if __name__ == '__main__':
    unittest.main()