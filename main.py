import disnake
from disnake.ext import commands
from db import *


bot = commands.InteractionBot(test_guilds=[1001202553884786749])

@bot.event
async def on_ready():
	await create_tables()

@bot.slash_command(description="Показывает баланс пользователя")
async def balace(inter, user: disnake.User = None):
	if user == None:
		info = await get_user(inter.author.id)
	elif user.isinstance(disnake.User):
		info = await get_user(user.id)
	await inter.response.send_message(f"Баланс: {info[1]}")

@bot.slash_command(description="Добавляет монет пользователю", default_member_permissions = disnake.Permissions(administrator=True))
async def add_balance(inter, user: disnake.User, money:int):
	await add_money(user.id, money)
	await inter.response.send_message(f"Пользователю <@!{user.id}> добавлено {money} монет")
bot.run("NoNo")
