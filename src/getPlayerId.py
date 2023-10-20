from supabase import create_client, Client

#modules
import getApiKey

def insertStage(stage_data):
    print('stage:')
    print(stage_data['stage_id'])

    supabase_url = 'https://juyljyipfkmaqnhijnsp.supabase.co'
    supabase_key = getApiKey.getApiKey('./api_key.txt')

    supabase: Client = create_client(supabase_url, supabase_key)

    data, count = supabase.table('stages').upsert(
        {
            "stage_id": stage_data['stage_id'],
            "stage_name": stage_data['stage_name'],
            "stage_code": stage_data['stage_code'],
            "category_name": stage_data['category_name'],
            "csnm": stage_data['Csnm'],
            "category_code": stage_data['category_code']
        }).execute()

    # print(data)

    return True