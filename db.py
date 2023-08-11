import aiosqlite

async def create_tables():
	"Создает таблицы если таковой нету"
	async with aiosqlite.connect("db/EcoBot.db") as db:
			await db.execute('CREATE TABLE IF NOT EXISTS users (user_id INTEGER PRIMARY KEY, user_balace INTEGER, user_work TEXT DEFAULT "None") ')

			await db.execute('CREATE TABLE IF NOT EXISTS works (id INTEGER PRIMARY KEY, work TEXT, salary INTEGER, lvl INTEGER) ')
			await db.commit()



async def create_user(id: int):
	"Делает запись о пользователе"
	async with aiosqlite.connect("db/EcoBot.db") as db:
		await db.execute('INSERT INTO users (user_id, user_balace) VALUES (?, ?)', (id, 0))
		await db.commit()



async def get_user(user_id):
	"""Проверяет есть такой пользователь, если нет создает запись (по id)"""
	async with aiosqlite.connect("db/EcoBot.db") as db:
		async with db.execute('SELECT * FROM users WHERE user_id = ?', (user_id, )) as cursor:
			info = await cursor.fetchone()
			if info:
				return info
			else:
				await create_user(user_id)
				return await get_user(user_id)



async def add_money(user_id, money):
	async with aiosqlite.connect("db/EcoBot.db") as db:
		await db.execute('UPDATE users SET user_balace = user_balace + ? WHERE user_id = ?', (money, user_id))
		await db.commit()