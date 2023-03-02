import urllib3
import json
url = "https://ptx.transportdata.tw/MOTC/v2/Tourism/ScenicSpot?$top=10&$format=JSON"
http = urllib3.PoolManager()
response = http.request('GET',url)
if(response.status == 200):
    data = json.loads(response.data.decode('utf-8'))
    print(data)
else:
    print(response.status)
