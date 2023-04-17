import discord
from discord.ext import commands
import responses
import json
import datetime
import asyncio
# import keep_alive

with open('setting.json', mode='r', encoding='utf8') as jfile:
    jdata = json.load(jfile)
    
def run_discord_bot():    
    intents = discord.Intents.default()
    intents.message_content = True
    bot = commands.Bot(intents = intents, command_prefix = '%')
    
    async def schedule_daily_message():
        while True:
            now = datetime.datetime.now()
            midnight = (now + datetime.timedelta(days = 1)).replace(hour=0, minute=0, second=0, microsecond=0)
            wait_time = (midnight - now).total_seconds()
            if wait_time > 86400:
                wait_time -= 86400
            print('Next daily message:', wait_time, '(s)')
            await asyncio.sleep(wait_time)
            
            channel1 = bot.get_channel(1043935672207159316)
            channel2 = bot.get_channel(1050409753202929664)
            response = responses.handle_response('countdown')
            await channel1.send(response)
            await channel2.send(response)
    
    @bot.event
    async def on_ready():
        print('Bot is online!')
        print('Logged in as', bot.user)
        game = discord.Game('>_<')
        await bot.change_presence(status = discord.Status.idle, activity = game)
        await schedule_daily_message()
        
    @bot.event
    async def on_message(message):
        if message.author == bot.user:
            return
        
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)
        
        print(f"{username} said: '{user_message}' ({channel})")
        
        if user_message[0] == '%':
            user_message = user_message[1:]
            if str(message.author) == 'userwei#8366':
                response = responses.handle_response(user_message, True)
                await message.channel.send(response)
            # elif str(message.author) == '一豪#9288':
            #     response = responses.handle_response(user_message, True)
            #     await message.channel.send(response)
            else:
                response = responses.handle_response(user_message, False)
                await message.channel.send(response)
        
        if bot.user.mentioned_in(message):
            await message.channel.send('You can type `%help` for more info.')
        
    # keep_alive.keep_alive()
    bot.run(jdata['TOKEN'])