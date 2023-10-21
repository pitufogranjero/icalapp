from supabase import create_client, Client

#modules
from src import getApiKey

def getUsers():
    
    supabase_url = 'https://juyljyipfkmaqnhijnsp.supabase.co'
    supabase_key = getApiKey.getApiKey('./src/api_key.txt')

    supabase: Client = create_client(supabase_url, supabase_key)

    response, error = supabase.table('profiles').select('id').execute()

    user_list = response[1]

    return user_list