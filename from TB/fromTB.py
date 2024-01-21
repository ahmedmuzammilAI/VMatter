from TbApi import TbApi
# Create yourself a demo account: https://demo.thingsboard.io/signup
mothership_url = "http://demo.thingsboard.io:8080"
thingsboard_username = "teamexentia@gmail.com"
thingsboard_password = "teamsmc123"

tbapi = TbApi(mothership_url, thingsboard_username, thingsboard_password)   # root object

device = tbapi.get_device_by_name("ESP8266")        # In the default demo dataset
telemetry = device.get_telemetry()
print(telemetry)

