from unpackager import Unpackager
import unittest

class TestUnpackager(unittest.TestCase):

    def test_correct_checksum(self):
        testString = "f00412345678BA3C"
        unpack = Unpackager()
        self.assertEqual(unpack.ingest(testString), 2)

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