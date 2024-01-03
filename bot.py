import yaml
import discord
import socket

bot = discord.Bot()

with open('config.yaml', 'r') as file:
  config = yaml.safe_load(file)

token = config["token"]
serwery = config["serwery"]
api = config["link_do_api"]

@bot.command(description="Wysyła informacje o bocie.")
async def info(ctx):
  await ctx.respond(f"Ten bot jest wrapperem do mojego API, który możesz znaleźć [tutaj](https://github.com/szewczuko/api) \nBot jest wpełni open source i jego kod możesz znaleźć [tutaj](https://github.com/szewczuko/api-wrapper)")

bot.run(token)