import os
from underground import metadata, SubwayFeed
from datetime import datetime, timezone
from pytz import timezone
tz = timezone('EST')
now = datetime.now(tz)

def getmtadata(line,station="L16N"):
	os.environ['MTA_API_KEY'] = "HoYzecGBd54ZYC8bHLOgq2aBX6lZTu1n5NIX1ETm"
	API_KEY = os.getenv('MTA_API_KEY')

	ROUTE = line
	feed = SubwayFeed.get(ROUTE, api_key=API_KEY)

	URL = metadata.resolve_url(ROUTE)
	feed = SubwayFeed.get(URL)
	stop_dict = feed.extract_stop_dict()
	#result = stop_dict[line][station]
	result = [(item-now).seconds//60 for item in stop_dict[line][station]]
	return str(result)




#now = datetime.now() # current date and time



#time = now.strftime("%H:%M:%S")
#print("time:", time)