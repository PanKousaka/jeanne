import discord
import logging

import asyncio
import os
import random
 
# Set up some logging stuff. Copied from the discord.py documentation.
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler) 
logger.addHandler(handler)

from discord.ext.commands import Bot
bot = Bot(command_prefix="★")
@bot.event
async def on_read():
    await my_bot.change_presence(game=discord.Game(name='with Mashu'))

@bot.async_event
async def on_member_join(member):
    await bot.send_message(bot.get_channel("312066214815858698"),"Welcome to the Discord, " + "<@" + member.id + ">" + "! Please read the rules, and enjoy your stay.")
    await bot.send_message(bot.get_channel("361333545836478476"),"<@" + member.id + ">" + " (User ID: " + member.id + ") has joined.")
@bot.async_event
async def on_member_remove(member):
    await bot.send_message(bot.get_channel("312066214815858698"),"Farewell, " + "<@" + member.id + ">" + "!" )
    await bot.send_message(bot.get_channel("361333545836478476"),"<@" + member.id + ">" + " (User ID: " + member.id + ") has left." )

bot.run("MzYxMzI2OTUyMTYzOTY2OTk2.DKifdQ.79gIE_O_O2MWqLyVrwYKmq52XU4")
