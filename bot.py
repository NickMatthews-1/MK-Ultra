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
        name = f'{servers} servers and {members} members'
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

@bot.tree.command(name="isputindead",description="I hope so!")
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message(f"Hello {interaction.user.mention}! Putin is not dead sadly.", ephemeral=False)

@bot.command()
async def info(ctx):

    await ctx.send(ctx.guild)



@bot.command(name="poll", brief="Pokemon Go to the Polls", description="do !poll [insert-text] yes no to be able to use the poll command") ## This is a poll function. To use it do !poll INSERT-TEXT yes no
async def poll(ctx, question="Put the question here with a - between words", option1="You choose", option2="You choose"):
  if option1==None and option2==None:
    await ctx.channel.purge(limit=1)
    message = await ctx.send(f"```New poll: \n{question}```\n**✅ = Yes**\n**❎ = No**")
    await message.add_reaction('❎')
    await message.add_reaction('✅')
  elif option1==None:
    await ctx.channel.purge(limit=1)
    message = await ctx.send(f"```New poll: \n{question}```\n**✅ = {option1}**\n**❎ = No**")
    await message.add_reaction('❎')
    await message.add_reaction('✅')
  elif option2==None:
    await ctx.channel.purge(limit=1)
    message = await ctx.send(f"```New poll: \n{question}```\n**✅ = Yes**\n**❎ = {option2}**")
    await message.add_reaction('❎')
    await message.add_reaction('✅')
  else:
    await ctx.channel.purge(limit=1)
    message = await ctx.send(f"```New poll: \n{question}```\n**✅ = {option1}**\n**❎ = {option2}**")
    await message.add_reaction('❎')
    await message.add_reaction('✅')


@bot.tree.command(name="avatar",description="Gets user avatar") ## This displays an avatar of a person selected by the user. Slash Command
async def avatar(interaction:discord.Interaction,member:discord.Member):
    await interaction.response.send_message(member.display_avatar)

@bot.command(name="avatar",brief="Shows the users avatar" ,description="Gets the users avatar at full size") ## Not slash command
async def av(ctx,member: discord.Member):
    await ctx.send(member.display_avatar)

bot.run('INSERT_BOT_TOKEN_HERE')
