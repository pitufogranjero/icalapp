from supabase import create_client, Client
import requests
from datetime import timedelta
import datetime
from icalendar import Calendar, Event
import json

#modules
import getUsers
import getUserTeams
import getUserPlayers
import createCalendar
import getUserUrl

import os

os.system('clear')

# consultamos los id de los usuarios
usersList = getUsers.getUsers()
# print(usersList)

# consultamos los equipos de cada usuario
for user in usersList:
    print('User id: ' + user['id'])
    
    # print('\nUser teams:')
    user_teams = getUserTeams.getUserTeams(user['id'])
    # print(user_teams)

    # print('\nUser players:')
    user_players = getUserPlayers.getUserPlayers(user['id'])
    # print(user_players)

    # creamos un archivo por cada usuario
    if(len(user_teams) > 0):
        # print('entro')

        # leo la url del usuario
        user_url = getUserUrl.getUserUrl(user['id'])
        user_url = user_url[0]
        if(user_url['calendar_url'] != None):
            file_name = user_url['calendar_url'] + '.ics'

            createCalendar.createCalendar(user_teams,user_players,file_name)

        # complete_user_url = 'https://www.czr.es/calendars/' + user_url['calendar_url'] + '.ics'
        # print(complete_user_url)






# metemos en la bbdd la url de cada usuario
