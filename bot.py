import yaml
import discord
import socket

with open('config.yaml', 'r') as file:
  config = yaml.safe_load(file)

token = config["token"]
serwery = config["serwery"]
api = config["link_do_api"]

bot = discord.Bot()
bot.run(token)