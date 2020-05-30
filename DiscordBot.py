from discord.ext import commands

bot = commands.Bot(command_prefix="::")

@bot.command(pass_context=True)
async def ping(ctx, string = ""):
    if string.lower().replace(" ", "") == "":
        await ctx.send("Usage: /ping <message>")
        return
    await ctx.send(f"Pong: {string}")

bot.run("BOT TOKEN")
