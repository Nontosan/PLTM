import discord
from gtts import gTTS
from discord.ext import commands
from tempfile import TemporaryFile

client = commands.Bot(command_prefix = '*')
speaker = None
myLang = 'th'

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    global speaker
    if message.author == speaker:
        global myLang
        server = message.server
        voice_client = client.voice_client_in(server)
        tts = gTTS(text = message.content, lang = myLang)
        tts.save('tts.mp3')
        player = voice_client.create_ffmpeg_player('tts.mp3', after=lambda: print('done'))
        player.start()
    if message.content == '.ttsme':
        speaker = message.author

'''
@client.command(pass_context = True)
async def help(ctx)
'''

@client.command(pass_context = True)
async def join(ctx):
    channel = ctx.message.author.voice.voice_channel
    await client.join_voice_channel(channel)

@client.command(pass_context = True)
async def tts(context, myText):
    global myLang
    server = context.message.server
    voice_client = client.voice_client_in(server)
    tts = gTTS(text = myText, lang = myLang)
    tts.save('tts.mp3')
    player = voice_client.create_ffmpeg_player('tts.mp3', after=lambda: print('done'))
    player.start()

@client.command(pass_context = True)
async def ttslang(context, myText):
    global myLang
    myLang = myText
    await client.send_message(context.channel, str('Set default language to: ') + str(myText))


@client.command(pass_context = True)
async def leave(ctx):
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    await voice_client.disconnect()

client.run('NTYwNTI5ODExNDU4NzUyNTM4.D31Rlw.HUH1J7XnQr6WL-bhiuVMmKRsqSQ')
#client.run('NTYwODI4Njk0MTgxMDUyNDI3.D35n8g.D5d7u9M1Z-m4DD2_7Ee2eCKvqNY')