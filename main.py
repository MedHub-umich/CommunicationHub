from threads import read, write, connect

connectedDevs = connect()
read(connectedDevs[0])
write(connectedDevs[0],  "00020101")

