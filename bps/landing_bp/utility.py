import requests
from dateutil import parser
from datetime import datetime
from flask import url_for

def weatherUtility():
    """
        This function is created to 
            parse the date in string form,
            return the temperature and condition according to time 
    """
    res = requests.get( url_for('api_bp.weather', _external = True))
    res = res.json()
    # time write now
    timestamp = datetime.now()
    hrs = int(datetime.strftime(timestamp,r'%H'))
    # print(res)

    arr = []
    for i in range(min(4,len(res))):
        data = res[i]
        # Date Parsing from api
        date_str = data['date']['$date']
        date = parser.isoparse(date_str)
        day = date.strftime(r"%a")
        forcast = data['forcast'][hrs]
        mintemp = min(data['forcast'], key=lambda x : x['temp'])['temp']
        maxtemp = max(data['forcast'], key=lambda x : x['temp'])['temp']
        # night checking
        # forcast['time']['hrs'] -= 10
        # forcast['condition'] = 'thunder'
        # print(forcast['condition'])
        arr.append(
            { 
                "location": data['location'],
                "day": day,
                "temp": forcast['temp'],
                "condition": forcast['condition'],
                "time": forcast['time'],
                "maxtemp": maxtemp,
                "mintemp": mintemp
            }
        )

    return arr