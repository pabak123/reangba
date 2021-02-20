import discord 
import asyncio
import os
from discord.ext import commands

everyone = False
client = discord.Client()


@client.event
async def on_ready():
    print("봇이 성공적으로 실행되었습니다.")
    messages = ["렌바 서버 공식 봇입니다!","렌바야 도움","렌바 디스코드에서 욕을 사용하지 마세요!","궁금한거는 바로 물어보세요!"]
    while True:
        await client.change_presence(status=discord.Status.online, activity=discord.Game(name=messages[0]))
        messages.append(messages.pop(0))
        await asyncio.sleep(5)# 5초마다 바뀜

@client.event
async def on_connect():
    for emoji in client.emojis:
        print(emoji)

        
@client.event
async def on_reaction_add(reaction, user):
    if str(reaction.emoji) == ("📢"):
        if str(user.id) == str(326334598206324736):
            if everyone == True:
                h = '@everyone'
            else:
                h = ''
            await reaction.message.remove_reaction(reaction.emoji, user)
            embed = discord.Embed(title= '📢ㅣ공지 사항', description=(f'{reaction.message.content}'), colour=0x00fff9)
            embed.set_footer(text='렌바 디스코드')
            await client.get_channel(int(811524005835702332)).send(h,embed=embed)

    if str(reaction.emoji) == ("🗑"):
        if str(user.id) == str(326334598206324736):
            await reaction.message.delete()


@client.event
async def on_message(message):

    if "개새끼" in message.content or "씨발" in message.content or "바보" in message.content:
        embed = discord.Embed(timestamp=message.created_at, colour=discord.Colour.red(), title=":no_entry_sign: | 경고!", description=f"{message.author.mention}님 욕하지 마세요")
        embed.add_field(name="사용한 욕설", value=f"{message.content}")
        await message.channel.send(embed=embed)
        await message.delete()

    if message.content.startswith('렌바야 도움'):
        embed = discord.Embed(title="렝바봇의 명령어들", description="렌바의 서버를 서포트 해주는 봇입니다!", color=0x00fff9) # Embed의 기본 틀(색상, 메인 제목, 설명)을 잡아줍니다
        embed.set_footer(text="상갈") # 하단에 들어가는 조그마한 설명을 잡아줍니다
        await message.channel.send(embed=embed) # embed를 포함 한 채로 메시지를 전송합니다.

    if message.content == "!채널생성":
        await guild.create_text_channel("{message.content}")

    if message.channel.id == 811523338383654932:
        if message.author.id == 326334598206324736:
            await message.add_reaction("📢")
            await message.add_reaction("🗑")

access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
