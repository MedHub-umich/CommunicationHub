from unpackager import Unpackager

testStrings = [
    "f000", #no size
    "f00100", #size 1
    "f034", #size52
]

for test in testStrings:
    unpack = Unpackager()
    print("Testing: ", test)
    unpack.ingest(test)