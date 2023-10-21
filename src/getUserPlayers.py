from supabase import create_client, Client

#modules
from src import getApiKey

def getUserPlayers(user):

    supabase_url = 'https://juyljyipfkmaqnhijnsp.supabase.co'
    supabase_key = getApiKey.getApiKey('./src/api_key.txt')

    supabase: Client = create_client(supabase_url, supabase_key)

    response, error = supabase.table('rel_profile_player').select('player_id, players(player_name)').eq('profile_id',user).execute()

    players_list = response[1]
    # print(teams_list)
    players_list = [{'player_id': item['player_id'], 'name': item['players']['player_name']} for item in players_list]

    return players_list