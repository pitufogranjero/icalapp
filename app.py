from supabase import create_client, Client
import requests
from datetime import timedelta
import datetime
from icalendar import Calendar, Event
import json

#modules
from src import getUsers
from src import getUserTeams
from src import getUserPlayers
from src import getUserUrl
from src import createCalendar
from src import getTennisMatches


import os

os.system('clear')

# consultamos los id de los usuarios
usersList = getUsers.getUsers()
# print(usersList)

getTennisMatches.getTennisMatches(1)
# getTennisMatches.getTennisMatches(2)

# consultamos los equipos de cada usuario
for user in usersList:
    print('\nUser id -> ' + user['id'])
    
    # print('\nUser teams:')
    user_teams = getUserTeams.getUserTeams(user['id'])
    # print(user_teams)

    # print('\nUser players:')
    user_players = getUserPlayers.getUserPlayers(user['id'])
    # print(user_players)

    # creamos un archivo por cada usuario
    if(len(user_teams) > 0 or len(user_players) > 0):
        # print('entro')

        # leo la url del usuario
        user_url = getUserUrl.getUserUrl(user['id'])
        user_url = user_url[0]
        if(user_url['calendar_url'] != None):
            file_name = user_url['calendar_url'] + '.ics'

            try:
                createCalendar.createCalendar(user_teams,user_players,file_name)
            except Exception as e:
                print('Exception:',e)

        # complete_user_url = 'https://www.czr.es/calendars/' + user_url['calendar_url'] + '.ics'
        # print(complete_user_url)

