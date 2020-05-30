from discord.ext import commands
import discord
import json
import os

if "\\" in os.getcwd():
	sep = "\\"
else:
	sep = "/"

bot = commands.Bot(command_prefix="/")
token = "BOT TONKEN"

@bot.event
async def on_ready():
	print("==========")
	print("봇 준비 완료!")
	print("==========")
	game = discord.Game("/경고")
	await bot.change_presence(status=discord.Status.online, activity=game)


@bot.command(pass_context=True)
async def 경고(ctx, name="not", count=1, reason="generic reason"):
	if name == "not":
		await ctx.send("사용법: /경고 `닉네임` `경고갯수` `사유`")
		return
	try:
		count = int(count)
	except:
		await ctx.send("오류! 경고 갯수는 숫자여야 합니다.")
		return
	found = False
	id = "undefined"
	for i in range(len(ctx.channel.guild.members)):
		if ctx.channel.guild.members[i].name == name:
			found = True
			id = ctx.channel.guild.members[i].id

	if found and id != "undefined":
		await ctx.send(f"{name}에게 경고 {count}가 부여되었습니다.\n이유: {reason}\n총 경고 갯수: {getWarn(name)}")
		await checkBan(name, channel=ctx.channel)
		writeFile(name, count)
	else:
		await ctx.send(f"{name}님은 이 서버에서 찾아볼 수 없습니다.")


def writeFile(text: str, count: int):
	json_data = {}
	if not os.path.isfile("test.json"):
		s = open("test.json", "w")
		s.close()
		json_data = {}
		with open("test.json", "w") as file:
			json.dump(json_data, file, indent=4)


	with open("test.json", "r") as jsonFile:
		json_data = json.load(jsonFile)
	try:
		totalWarn = json_data[text]
	except:
		totalWarn = 0
	json_data[text] = totalWarn + count
	with open("test.json", "w") as file:
		json.dump(json_data, file, indent=4)

def getWarn(text: str) -> int:
	if not os.path.isfile("test.json"):
		return 0
	json_data = {}
	with open("test.json", "r") as file:
		json_data = json.load(file)
	try:
		totalWarn = json_data[text]
	except:
		totalWarn = 0
	return int(totalWarn)

async def checkBan(name: str, channel):
	warn = getWarn(name)
	if warn >= 5:
		#await channel.guild.leave(channel.guild.)
		await channel.send_message(f"{name}님이 경고 횟수 초과로 서버에서 추방되었습니다.")


bot.run(token)
