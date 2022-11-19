# bot.py
import os
import random
import mouse
import keyboard
import discord
import time
from dotenv import load_dotenv
#from textblob import TextBlob
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')



client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, I am a bot who controls my hosts PC mouse'
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return


    if message.content:
        try:
            wiadomosc = str(message.content).lower()
            if wiadomosc == 'killbot':
                quit()
            if (wiadomosc == 'click') or (wiadomosc == 'lclick'):
                mouse.click(button='left')
            elif (wiadomosc == 'clickspace') or (wiadomosc == 'space') or (wiadomosc == 'show objects') or (wiadomosc == 'showobjects'):
                keyboard.press('space')
                time.sleep(5)
                keyboard.release('space')
            elif wiadomosc == 'rclick':
                mouse.click(button='right')
            elif wiadomosc[0:2] == 'mu':
                mouse.move(0, int(wiadomosc[2:])*-1, absolute=False, duration=1)
            elif wiadomosc[0:2] == 'md':
                mouse.move(0, int(wiadomosc[2:]), absolute=False, duration=1)
            elif wiadomosc[0:2] == 'mr':
                mouse.move(int(wiadomosc[2:]), 0, absolute=False, duration=1)
            elif wiadomosc[0:2] == 'ml':
                mouse.move(int(wiadomosc[2:])*-1, 0, absolute=False, duration=1)
        except:
            print("error")

client.run(TOKEN)
