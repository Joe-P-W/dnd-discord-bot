import os
import io
import discord
import asyncio

from dnd_terms.spell_level_and_school import get_spell_level_and_school
from requests_handler.dnd_api import get_spell
from table_top_items.calculator import calculate
from table_top_items.coin import flip_coin
from table_top_items.dice import roll_dice
from discord.ext import commands


client = commands.Bot(command_prefix="/")


@client.event
async def on_ready():
    print("Bot initialised")


@client.event
async def on_message(message):
    if message.content.startswith("/r") or message.content.startswith("/roll"):
        await roll_dice(message)

    elif message.content.startswith("/c"):
        channel = message.channel
        reply = f"{message.author.mention} `{message.content.replace(' ', '').replace('/c', '').strip()}` = "
        reply += str(await calculate(message.content.replace("/c", "")))
        await channel.send(reply)

    elif message.content.startswith("/flip"):
        await flip_coin(message)

    elif message.content.startswith("/s") or message.content.startswith("/search"):
        channel = message.channel
        spell_name = message.content.replace("/search", "").replace("/s", "").strip()
        reply = f"{message.author.mention} `{spell_name}`\n"
        spell_info = await get_spell(spell_name)

        spell_description = '\n'.join(spell_info['desc'])

        reply += f"**{spell_info['name']}** - \n"
        reply += f"*{await get_spell_level_and_school(spell_info['level'], spell_info['school']['name'])}* \n"
        reply += f"**Casting Time:** {spell_info['casting_time']} \n"
        reply += f"**Range:** {spell_info['range']} \n"
        reply += f"**Components:** {', '.join(spell_info['components'])} " \
                 f"{'(' + spell_info.get('material').lower().rstrip('.') + ')' if spell_info.get('material') is not None else ''} \n"
        reply += f"{spell_description}"

        if len(reply) < 2000:
            await channel.send(reply)
        else:
            pass

    elif message.content.startswith("/help") or message.content.startswith("/h"):
        channel = message.channel
        reply = f"{message.author.mention}\n"

        await channel.send(reply)


client.run(os.getenv("dnd_bot_token"))
