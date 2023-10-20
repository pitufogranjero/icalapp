import requests
from datetime import timedelta, datetime
import datetime
from icalendar import Calendar, Event

#modules
import getApiKey
import getDay
import insertStage
import insertEvent

def getTennisMatches(file_name,days_difference):

    cal = Calendar()

    dateToCheck = getDay.getDay(days_difference)
    offset = 2.00
    params = '?countryCode=SP&MD=1&locale=en'

    baseurl = 'https://sports-api20.p.rapidapi.com/app/date/tennis/'
    # tennis/20231019/2.00?countryCode=SP&MD=1&locale=en
    url = baseurl + str(dateToCheck) + '/' + str(offset) + '/' + params

    headers = {
        "X-RapidAPI-Key": getApiKey.getApiKey('./api_key_rapid.txt'),  
        "X-RapidAPI-Host": "sports-api20.p.rapidapi.com"
    }

    print(url)

    # print('\n\n\n\n\n')
    # response = ''
    response = requests.get(url, headers=headers)
    # print(response.text)

    if response.status_code == 200:  

        data = response.json()  
        stages = data['stages']
        # print(stages)

        for stage in stages:
            print(stage['category_code'])
            if stage['category_code'] == 'atp-challenger':
                continue

            insertStage.insertStage(stage)

            for event in stage['events']:
                insertEvent.insertEvent(event, stage['stage_id'])



    #         game = match['teams']['home']['name'] + ' - ' + match['teams']['away']['name']
    #         # print(match['fixture']['timestamp'])

    #         event = Event()
    #         event.add('summary', game)
    #         dt = datetime.datetime.fromtimestamp(timestamp)
    #         # print(dt)
    #         event.add('dtstart', datetime.datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second))
    #         event.add('dtend', datetime.datetime(dt.year, dt.month, dt.day, dt.hour+2, dt.minute, dt.second))
    #         cal.add_component(event)
        
    #     with open('./calendars/' + file_name, 'wb') as f:
    #         f.write(cal.to_ical())
    else:
        print("Error al realizar la solicitud a la API")



getTennisMatches('file_name',1)