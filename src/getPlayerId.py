from supabase import create_client, Client
import requests
import urllib.request
import sys

#modules
from src import getApiKey
from src import readWriteFiles
# from src import getApiKey

def getPlayerId(player_id,player_name):
    # print('player name:')
    # print(player_name + ' (' + str(player_id) + ')')

    remaining = readWriteFiles.readVariable('./src/allsports_remaining.txt','r')
    # print('Remaining allsports: ' + str(remaining))

    if remaining.strip() and int(remaining) < 3:
        raise Exception("There're are " + remaining + " more requests remaining in allsports")

    baseurl = 'https://allsportsapi2.p.rapidapi.com/api/tennis/search/'
    url = baseurl + player_name

    headers = {
        "X-RapidAPI-Key": getApiKey.getApiKey('./src/api_key_rapid.txt'),  
        "X-RapidAPI-Host": "allsportsapi2.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:

        readWriteFiles.writeVariable('./src/allsports_remaining.txt',response.headers['x-ratelimit-requests-remaining'], 'w')
        # print('Remaining allsports: ' + str(response.headers['x-ratelimit-requests-remaining']))

        data = response.json()
        data_object = data['results'][0]['entity']

        # print(data_object)
        country = data_object['country']['name']
        gender = data_object['gender']
        allsports_id = data_object['id']
        ranking = data_object['ranking']
    
    """
    baseurl = 'https://allsportsapi2.p.rapidapi.com/api/tennis/player/'
    url = baseurl + str(player_id) + '/image'

    response = requests.get(url, headers=headers)

    # Imprime los encabezados
    print("Headers:")
    for header, value in response.headers.items():
        print(f"{header}: {value}")

    # Imprime el contenido (como cadena)
    print("\nContent:")
    print(response.content.decode('utf-8'))

    if response.status_code == 200:
        readWriteFiles.writeVariable('./src/allsports_remaining.txt',response.headers['X-RateLimit-Requests-Remaining'], 'w')

        

        with open('./avatar/' + str(player_id) + '.png', 'wb') as file:
            file.write(response.content)
    else:
        print('La descarga falló. Código de estado:', response.status_code)
    
    print(response.content)

    # urllib.request.urlretrieve(url, './avatar/' + str(player_id) + '.png')

    """

    supabase_url = 'https://juyljyipfkmaqnhijnsp.supabase.co'
    supabase_key = getApiKey.getApiKey('./src/api_key.txt')

    supabase: Client = create_client(supabase_url, supabase_key)

    data, count = supabase.table('players').upsert(
        {
            "player_id": player_id,
            "player_name": player_name,
            "gender":gender,
            "country":country,
            "allsports_id": allsports_id,
            "ranking":ranking

        }).execute()

    # print(data)

    return True

# getPlayerId(180657,'Ben Shelton')