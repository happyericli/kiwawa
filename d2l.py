import discord
from discord.ext import commands

from lotify.client import Client

import os
import json

bot = commands.Bot(command_prefix='>')
discordbot_token = os.environ['OTUyMTA2MzQwODEyMTkzNzky.YixMIA.3IGNhtPWGRYpOW4Rk_Kk_Kfj2-0']
lotify_token = os.environ['bf05e9bEGf5AwJxsqnTWZ1MtJqJwdmaQ5URYZfziPoh']
discord_webhook_id = int(os.environ['https://discord.com/api/webhooks/952110323442266153/lG68Z6xxxd0GJO5CJcfjz3lkZkMGb_nUWI81_VoAVhDZA8jT7Cb_s2-RmzmhqVM_Cuw8'].split('/')[-2])
lotify = Client()

@bot.command()
async def ping(ctx):
    lotify.send_message(
        access_token = lotify_token,
        message = 'pong'
    )
    await ctx.send('pong')

@bot.listen()
async def on_message(message):
    if message.webhook_id == discord_webhook_id: return
    lotify_message = "＜" + message.author.display_name + "＞：\n"
    lotify_message += message.content
    lotify.send_message(
        access_token = lotify_token,
        message = lotify_message
    )

bot.run(discordbot_token)