from supabase import create_client, Client

#modules
from src import getApiKey


def getMatchesByPlayer(playerId):

    supabase_url = 'https://juyljyipfkmaqnhijnsp.supabase.co'
    supabase_key = getApiKey.getApiKey('./api_key.txt')

    supabase: Client = create_client(supabase_url, supabase_key)

    data, count = supabase.table('events').select('stage_name, stages(stage_name)','player_1, players(player_id)','player_2, players(player_id)').eq('player1', playerId).eq('player2', playerId).execute()

    print(data)

getMatchesByPlayer(616)