from supabase import create_client, Client
from datetime import timedelta, datetime
import datetime

#modules
from src import getApiKey
from src import insertPlayer
from src import getPlayerId

def insertEvent(event_data,stage_id):
    # print('event:')    
    # print(event_data['event_id'])

    supabase_url = 'https://juyljyipfkmaqnhijnsp.supabase.co'
    supabase_key = getApiKey.getApiKey('./src/api_key.txt')

    supabase: Client = create_client(supabase_url, supabase_key)

    insertPlayer.insertPlayer(event_data['t1'][0]['id'],event_data['t1'][0]['name'])

    #check if I have player 1 information
    data, count = supabase.table('players').select('allsports_id').eq('player_id',event_data['t1'][0]['id']).execute()

    data = data[1]

    if data[0]['allsports_id'] is not None:
        try:
            getPlayerId.getPlayerId(event_data['t1'][0]['id'],event_data['t1'][0]['name'])
            print('upsert player ' + event_data['t1'][0]['id'])
        except Exception as e:
            print("Exception:", e)

    insertPlayer.insertPlayer(event_data['t2'][0]['id'],event_data['t2'][0]['name'])

    #check if I have player 2 information
    data, count = supabase.table('players').select('allsports_id').eq('player_id',event_data['t2'][0]['id']).execute()

    data = data[1]

    if data[0]['allsports_id'] is not None:
        try:
            getPlayerId.getPlayerId(event_data['t2'][0]['id'],event_data['t1'][0]['name'])
            print('upsert player ' + event_data['t2'][0]['id'])
        except Exception as e:
            print("Exception:", e)


    """
    CONVERSION OF DATE TIME

    date_time = datetime.datetime.strptime(str(event_data['start_date']), "%Y%m%d%H%M%S")
    print(date_time)
    date_str = date_time.date()
    time_str = date_time.time()
    print(type(date_str))
    print(time_str)
    timestamp = date_time.timestamp()
    timestamp = datetime.datetime.utcfromtimestamp(timestamp)
    print(type(timestamp))
    """

    data, count = supabase.table('events').upsert(
        {
            "event_id": event_data['event_id'],
            "stage_id": stage_id,
            "start_date": event_data['start_date'],
            "player1": event_data['t1'][0]['id'],
            "player2": event_data['t2'][0]['id']
        }).execute()

    # print(data)

    return True