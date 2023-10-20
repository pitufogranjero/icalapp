from supabase import create_client, Client

#modules
import getApiKey

def getUserUrl(user):
    
    supabase_url = 'https://juyljyipfkmaqnhijnsp.supabase.co'
    supabase_key = getApiKey.getApiKey('./api_key.txt')

    supabase: Client = create_client(supabase_url, supabase_key)

    response, error = supabase.table('profiles').select('calendar_url').eq('id',user).execute()
    calendar_url = response[1]
    
    return calendar_url
