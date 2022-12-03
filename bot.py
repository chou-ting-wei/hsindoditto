import discord
import responses
import json

with open('setting.json', mode='r', encoding='utf8') as jfile:
    jdata = json.load(jfile)
        
def run_discord_bot():
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents = intents)
    
    @client.event
    async def on_ready():
        print('Bot is online!')
        print('Logged in as', client.user)
        game = discord.Game('>_<')
        await client.change_presence(status = discord.Status.idle, activity = game)
        
    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)
        
        print(f"{username} said: '{user_message}' ({channel})")
        
        if user_message[0] == '%':
            user_message = user_message[1:]
            response = responses.handle_response(user_message)
            await message.channel.send(response)
        
        if client.user.mentioned_in(message):
            await message.channel.send('You can type `%help` for more info.')
        
    client.run(jdata['TOKEN'])