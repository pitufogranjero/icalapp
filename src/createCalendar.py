import requests
from datetime import timedelta
import datetime
from icalendar import Calendar, Event
from supabase import create_client, Client


import getApiKey

def createCalendar(teams,players,file_name):

    cal = Calendar()

    actual_date = datetime.datetime.today()
    actual_date_before = actual_date - timedelta(days=5)
    actual_date_str = actual_date_before.strftime('%Y-%m-%d')
    year = str(actual_date.year)

    baseurl = 'https://api-football-v1.p.rapidapi.com/v3/'

    
    for team in teams:
        # print(team['team_id'])
        # print(team)

        querys = 'team=' + str(team['name'])
        querys += '&from=' + actual_date_str
        querys += '&season=' + year
        querys += '&to=' + year + '-12-31'
        
        
        url = baseurl + "fixtures?" + querys
        headers = {
            "X-RapidAPI-Key": getApiKey.getApiKey('./api_key_rapid.txt'),  
            "X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
        }
        print('Query: ' + querys)
        # print('\n\n\n\n\n')
        # response = ''
        response = requests.get(url, headers=headers)

        if response.status_code == 200:  

            data = response.json()  
            # data_object = json.loads(data['response'])
            data_object = data['response']

            print('data_object:')
            print(data_object)
            for match in data_object:
                timestamp = match['fixture']['timestamp']
                game = match['teams']['home']['name'] + ' - ' + match['teams']['away']['name']
                # print(match['fixture']['timestamp'])

                event = Event()
                event.add('summary', game)
                dt = datetime.datetime.fromtimestamp(timestamp)
                # print(dt)
                event.add('dtstart', datetime.datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second))
                event.add('dtend', datetime.datetime(dt.year, dt.month, dt.day, dt.hour+2, dt.minute, dt.second))
                cal.add_component(event)

        else:
            print("Error al realizar la solicitud a la API")
    

    supabase_url = 'https://juyljyipfkmaqnhijnsp.supabase.co'
    supabase_key = getApiKey.getApiKey('./api_key.txt')

    supabase: Client = create_client(supabase_url, supabase_key)

    for player in players:

        response, error = supabase.table('events').select('event_id,stage:stages(stage_name), start_date, player_1:player1(player_name), player_2:player2(player_name)').eq('player1',player['player_id']).execute()

        games = response[1]
        # print(events)

        for game in games:
            print(game)

            timestamp = game['start_date']
            formatted_timestamp_str = datetime.datetime.strptime(timestamp, "%Y%m%d%H%M%S")
            print(timestamp)
            game = game['player_1']['player_name'] + ' - ' + game['player_2']['player_name'] + ':\n' + game['stage']['stage_name'] + '\niCalSports'

            event = Event()
            event.add('summary', game)
            dt = datetime.datetime.fromtimestamp(int(formatted_timestamp_str.timestamp()))
            print(dt)
            event.add('dtstart', datetime.datetime(dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second))
            event.add('dtend', datetime.datetime(dt.year, dt.month, dt.day, dt.hour+2, dt.minute, dt.second))
            cal.add_component(event)


    with open('../' + file_name, 'wb') as f:
        f.write(cal.to_ical())