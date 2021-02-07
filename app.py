import discord

client = discord.Client()

@client.event
async def on_ready():
     print(client.ueser.id)
     print("준비되었어요!")

@client.event
async def on_message(message):
     if message.content.startswith("!핑"):
          await message.channel.send("퐁!")
    if message.content.startswith("/팀나누기 "):
        try:
            user_id = message.author.name
            await message.channel.send("팀 나누기 시작합니다~♪")
            team = message.content[7:]
            peopleteam = team.split("/")
            people = peopleteam[0]
            team = peopleteam[1]
            person = people.split(" ")
            teamname = team.split(" ")
            random.shuffle(teamname)
            for i in range(0, len(person)):
                await message.channel.send(person[i]+ " ------> " + teamname[i])
            await message.channel.send("팀나누기가 완료되었어요~!")
            print("팀나누기 명령어를 성공적으로 수행을 완료했어요.")
        except IndexError:
            embed=discord.Embed(title="ERROR",description="사람이름과 팀 이름이 지정되지 않음 또는 사람이름과 팀 이름 숫자가 같지 않습니다.",color= 0xff0000)
            await message.channel.send(embed=embed)

client.run("ODA3ODY2MTk3MDA4OTczODM0.YB-OBg.YX3bze6rHn6S62GRECH34Q9t5aw")