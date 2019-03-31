import discord
from gtts import gTTS
from discord.ext import commands

client = commands.Bot(command_prefix = '.')
speaker = None
myLang = 'th'
superLang = 'th'
activate = False

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    await client.process_commands(message)
    global activate
    if activate:
        activate = False
        return
    global speaker
    if message.author == speaker:
        await supertts(message.content,message.server)

'''
@client.command(pass_context = True)
async def help(ctx):
    user = ctx.message.author
    await client.send_message(user,
        str('```available commands \n') +
        str("'af'     : 'Afrikaans'\n") +
        str("'sq'     : 'Albanian'\n") +
'''

@client.command(pass_context=True)
async def suplang(ctx):
    user = ctx.message.author
    await client.send_message(user, 
        str('```----------Supported Languages----------\n') +
        str("'af'     : 'Afrikaans'\n") +
        str("'sq'     : 'Albanian'\n") +
        str("'ar'     : 'Arabic'\n") +
        str("'hy'     : 'Armenian'\n") +
        str("'bn'     : 'Bengali'\n") +
        str("'ca'     : 'Catalan'\n") +
        str("'zh'     : 'Chinese'\n") +
        str("'zh-cn'  : 'Chinese (Mandarin/China)'\n") +
        str("'zh-tw'  : 'Chinese (Mandarin/Taiwan)'\n") +
        str("'zh-yue' : 'Chinese (Cantonese)'\n") +
        str("'hr'     : 'Croatian'\n") +
        str("'cs'     : 'Czech'\n") +
        str("'da'     : 'Danish'\n") +
        str("'nl'     : 'Dutch'\n") +
        str("'en'     : 'English'\n") +
        str("'en-au'  : 'English (Australia)'\n") +
        str("'en-uk'  : 'English (United Kingdom)'\n") +
        str("'en-us'  : 'English (United States)'\n") +
        str("'eo'     : 'Esperanto'\n") +
        str("'fi'     : 'Finnish'\n") +
        str("'fr'     : 'French'\n") +
        str("'de'     : 'German'\n") +
        str("'el'     : 'Greek'\n") +
        str("'hi'     : 'Hindi'\n") +
        str("'hu'     : 'Hungarian'\n") +
        str("'is'     : 'Icelandic'\n") +
        str("'id'     : 'Indonesian'\n") +
        str("'it'     : 'Italian'\n") +
        str("'ja'     : 'Japanese'\n") +
        str("'ko'     : 'Korean'\n") +
        str("'la'     : 'Latin'\n") +
        str("'lv'     : 'Latvian'\n") +
        str("'mk'     : 'Macedonian'\n") +
        str("'no'     : 'Norwegian'\n") +
        str("'pl'     : 'Polish'\n") +
        str("'pt'     : 'Portuguese'\n") +
        str("'pt-br'  : 'Portuguese (Brazil)'\n") +
        str("'ro'     : 'Romanian'\n") +
        str("'ru'     : 'Russian'\n") +
        str("'sr'     : 'Serbian'\n") +
        str("'sk'     : 'Slovak'\n") +
        str("'es'     : 'Spanish'\n") +
        str("'es-es'  : 'Spanish (Spain)'\n") +
        str("'es-us'  : 'Spanish (United States)'\n") +
        str("'sw'     : 'Swahili'\n") +
        str("'sv'     : 'Swedish'\n") +
        str("'ta'     : 'Tamil'\n") +
        str("'th'     : 'Thai'\n") +
        str("'tr'     : 'Turkish'\n") +
        str("'vi'     : 'Vietnamese'\n") +
        str("'cy'     : 'Welsh'\n```"))

@client.command(pass_context = True)
async def join(ctx):
    channel = ctx.message.author.voice.voice_channel
    await client.join_voice_channel(channel)
    global activate
    activate = True

@client.command(pass_context = True)
async def tts_status(ctx):
    channel = client.get_channel(ctx.message.channel.id)
    await client.send_message(channel, 
        str('Super tts user: ') + str(speaker.name) + str('\n') +
        str('Super tts language: ') + str(superLang) + str('\n') +
        str('tts language: ') + str(myLang) + str('\n'))
    global activate
    activate = True

@client.command(pass_context = True)
async def tts(ctx, myText):
    global myLang
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    tts = gTTS(text = myText, lang = myLang)
    tts.save('tts.mp3')
    player = voice_client.create_ffmpeg_player('tts.mp3', after=lambda: print('done'))
    player.start()
    global activate
    activate = True

async def supertts(speakText,server):
    global superLang
    voice_client = client.voice_client_in(server)
    tts = gTTS(text = speakText, lang = superLang)
    tts.save('supertts.mp3')
    player = voice_client.create_ffmpeg_player('supertts.mp3', after=lambda: print('done'))
    player.start()

@client.command(pass_context = True)
async def ttslang(ctx, myText):
    global myLang
    myLang = myText
    channel = client.get_channel(ctx.message.channel.id)
    await client.send_message(channel, str('Set default language to: ') + str(myLang))
    global activate
    activate = True

@client.command(pass_context = True)
async def sttslang(ctx, myText):
    global superLang
    superLang = myText
    channel = client.get_channel(ctx.message.channel.id)
    await client.send_message(channel, str('Set Super TTS default language to: ') + str(superLang))
    global activate
    activate = True

@client.command(pass_context = True)
async def ttsme(ctx):
    global speaker
    speaker = ctx.message.author
    channel = client.get_channel(ctx.message.channel.id)
    await client.send_message(channel, str('Set Super TTS user to: ') + str(speaker.name))
    global activate
    activate = True

@client.command(pass_context = True)
async def leave(ctx):
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    await voice_client.disconnect()
    global activate
    activate = True

client.run('NTYwNTI5ODExNDU4NzUyNTM4.XKBE_A.F954Syf-ceJLc8PaL8HttV-1S40') #PLTM
#client.run('NTYwODI4Njk0MTgxMDUyNDI3.D3_3-Q.hOanmx0vRyK-sqp-B71rQoVEozo') #test bot 2