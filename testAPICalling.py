import requests
url='http://medhub-server.herokuapp.com/api/v1.0/add_data'
data = {
	"packets": [
		{
			"user": 2,
			"type": 2,
			"time": 100,
			"data": [1, 2, 6, 8]
		},
		{
			"user": 2,
			"type": 3,
			"time": 20,
			"data": [1, 2, 6, 8]
		},
		{
			"user": 2,
			"type": 1,
			"time": 1,
			"data": [1, 30, 6, 8]
		}
	]
}

response = requests.post(url, json=data)
print(response)