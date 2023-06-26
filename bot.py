import discord
from discord import app_commands
from discord.ext import commands


bot = commands.Bot(command_prefix="!", intents = discord.Intents.all())

@bot.event
async def on_ready():
    print("Bot is up and ready!")
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print (e)
    ### This section looks for the amount of servers the
    ### bot is in and displays it as a status message
    servers = len(bot.guilds)
    members = 0
    for guild in bot.guilds:
        members += guild.member_count - 1

    await bot.change_presence(activity = discord.Activity(
        type = discord.ActivityType.watching,
        name = f'{servers} servers and {members} members' ### This shows the servers and members
    ))


@bot.command()
async def server_info(ctx):
    for guild in client.guilds:
        print(guild.name) # prints all server's names

@bot.tree.command(name="hello")
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message(f"Hello {interaction.user.mention}! This is a slash command!", ephemeral=False)

@bot.tree.command(name="say")
@app_commands.describe(thing_to_say = "What should I say?")
async def say(interaction: discord.Interaction, thing_to_say: str):
    await interaction.response.send_message(f"{interaction.user.name} said: `{thing_to_say}`")

@bot.tree.command(name="isputindead")
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message(f"Hello {interaction.user.mention}! Putin is not dead sadly.", ephemeral=False)

@bot.command()
async def info(ctx):

    await ctx.send(ctx.guild)
    
bot.run('INSERT_BOT_TOKEN_HERE')
