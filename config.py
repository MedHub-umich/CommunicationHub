MACtranslation = {
	"EC:B1:FE:A2:84:01" : 2,
	# "D9:04:7D:17:F7:80" : 1,
	# "EF:DD:9C:D6:FB:6B" : 1,
	"F3:C9:F9:A0:E9:6E" : 1,
	# "E6:3B:21:18:45:51" : 1,
	"FA:9A:A3:54:EE:DA" : 1,
}

userToMac = {
	1 : "FA:9A:A3:54:EE:DA",
	2 : "EC:B1:FE:A2:84:01"
}

class PacketTypes:
    HEART_RATE = 3
    ECG = 2
    BREATHING_RATE = 4
    TEMPERATURE = 5
    BLOOD_PRESSURE = 1

QueueLimits = {
	PacketTypes.HEART_RATE : 1,
	PacketTypes.ECG : 70,
	PacketTypes.BREATHING_RATE : 1,
	PacketTypes.TEMPERATURE : 1,
	PacketTypes.BLOOD_PRESSURE : 1,
}

add_data_url = "http://medhub-server.herokuapp.com/api/v1.0/add_data"