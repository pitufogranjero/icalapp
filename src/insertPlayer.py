from supabase import create_client, Client

#modules
from src import getApiKey

def insertPlayer(id,name):
    print('player:')
    print(name)

    supabase_url = 'https://juyljyipfkmaqnhijnsp.supabase.co'
    supabase_key = getApiKey.getApiKey('./src/api_key.txt')

    supabase: Client = create_client(supabase_url, supabase_key)

    data, count = supabase.table('players').upsert(
        {
        "player_id": id,
        "player_name": name
        }).execute()

    # print(data)

    return True