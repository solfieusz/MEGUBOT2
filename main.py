import discord
import random
from discord.ext import commands
import youtube_dl
import os
import asyncio

intents = discord.Intents.default()
intents.members = True
intents = intents.all()

bot = commands.Bot(command_prefix='?', case_insensitive = True, intents = intents)

@bot.event
async def on_member_join(member):
    if member.guild.name == 'Mafia Fanatyków Eksplozji v2': 
        embed = discord.Embed(title=f'Siema {member.name} Witaj w Mafii!  ',
                    color=0xff0000,
                    font_size=200)
        await bot.get_channel(974668454344933419).send(f"{member.mention}")
        await bot.get_channel(974668454344933419).send(embed=embed)
        await member.send(f'Witamy w mafii! Enjoy your stay!')
    else:
        return


@bot.command('explosion')
async def explosion(ctx):
  await ctx.reply('https://tenor.com/view/house-explosion-explode-boom-kaboom-gif-19506150')

@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    if reason==None:
      reason="niewinność"
    await ctx.guild.kick(member)
    await ctx.send(f'{member.mention} został wyrzucony z mafii za: {reason}')

@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    if reason==None:
      reason="niewinność"
    await ctx.guild.ban(member)
    await ctx.send(f'{member.mention} został zbanowany z mafii za: {reason}')

@bot.command()
async def sraken(ctx):
  await ctx.reply('pierdaken')


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="Dźwięki eksplozji"))
    print("działa")

bot.run(os.getenv("TOKEN"))