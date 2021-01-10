import os

from discord.ext import commands

from dnd_functions.message_formatting import format_spell
from requests_handler.dnd_api import get_spell
from table_top_items.calculator import calculate
from table_top_items.coin import flip_coin
from table_top_items.dice import roll_dice

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

        spell_info = await get_spell(spell_name)

        for reply in await format_spell(message, spell_name, spell_info):
            await channel.send(reply)

    elif message.content.startswith("/help") or message.content.startswith("/h"):
        channel = message.channel
        reply = f"{message.author.mention}\n"

        await channel.send(reply)


client.run(os.getenv("dnd_bot_token"))
