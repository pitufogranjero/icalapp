from supabase import create_client, Client

#modules
from src import getApiKey

def getUserTeams(user):

    supabase_url = 'https://juyljyipfkmaqnhijnsp.supabase.co'
    supabase_key = getApiKey.getApiKey('./src/api_key.txt')

    supabase: Client = create_client(supabase_url, supabase_key)

    response, error = supabase.table('rel_profile_team').select('team_id, teams(name)').eq('profile_id',user).execute()

    teams_list = response[1]
    # print(teams_list)
    team_ids = [item['team_id'] for item in teams_list]
    team_names = [item['teams']['name'] for item in teams_list]
    teams_list = [{'team_id': item['team_id'], 'name': item['teams']['name']} for item in teams_list]

    return teams_list