import discord
import twitter #pip install twitter

#TwitterAPIKey
Consumer_Key="*******"
Consumer_Secret="*******"
AccessToken="*******"
AccessTokenSecret="*******"

TOKEN = "TOKEN"

client = discord.Client()

@client.event
async def on_ready():
    print('ログインしました')
    print('Call56TwitterBotを起動中です。')

@client.event
async def on_message(message):
    CommandTrigger="!ctl"
    Twitter=140
    if message.author.bot:
        return
    if message.content.startswith(CommandTrigger):
        Oauth = twitter.OAuth(AccessToken,AccessTokenSecret,Consumer_Key,Consumer_Secret)
        twi = twitter.Twitter(auth=Oauth)
        message.content=message.content.replace(CommandTrigger,message.author.name+":")
　　#140文字以下か判定する
        if len(message.content) <= Twitter:
            #Twitterに投稿
            twi.statuses.update(status=message.content)
        else:
            mes="Twitterへの投稿に失敗しました、文字数を減らしてください。"
            await message.channel.send(mes)
client.run(TOKEN)
