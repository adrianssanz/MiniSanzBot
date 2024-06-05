import discord
import datetime
import os
from dotenv import load_dotenv
load_dotenv()
import random

token = os.getenv('DISCORD_TOKEN')
fecha_actual = f'{datetime.datetime.now().strftime("%H:%M:%S %d-%m-%Y")}'
intents = discord.Intents.all()
intents.members = True

archivo = open("logs/logLogin.txt","a")

lobby_id = None

log_editados = None

log_eliminados = None

dado = random.randint(1,6)
moneda = random.random()