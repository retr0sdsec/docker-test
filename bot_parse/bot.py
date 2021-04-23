import config
import logging
import asyncio
from datetime import datetime

from aiogram import Bot, Dispatcher, executor, types
from sqlighter import SQLighter

from stopgame import StopGame

logging.basicConfig(level=logging.INFO)


bot = Bot(token=config.API_TOKEN)
dp = Dispatcher(bot)

db = SQLighter('db.db')

sg = StopGame('lastkey.txt')

@dp.message_handler(commands=['subscribe'])
async def subscribe(message: types.Message):
	if(not db.subscriber_exists(message.from_user.id)):
		db.add_subscriber(message.from_user.id)
	else:
		db.update_subscription(message.from_user.id, True)

	await message.answer("Вы успешно подписались на рассылку!\nЖдите, скоро выйдут новые обзоры и вы узнаете о них первыми =)")

@dp.message_handler(commands=['unsubscribe'])
async def unsubscribe(message: types.Message):
	if(not db.subscriber_exists(message.from_user.id)):
		db.add_subscriber(message.from_user.id, False)
		await message.answer("Вы итак не подписаны.")
	else:
		db.update_subscription(message.from_user.id, False)
		await message.answer("Вы успешно отписаны от рассылки.")

async def scheduled(wait_for):
	while True:
		await asyncio.sleep(wait_for)

		new_games = sg.new_games()

		if(new_games):
			new_games.reverse()
			for ng in new_games:
				nfo = sg.game_info(ng)

				subscriptions = db.get_subscriptions()

				with open(sg.download_image(nfo['image']), 'rb') as photo:
					for s in subscriptions:
						await bot.send_photo(
							s[1],
							photo,
							caption = nfo['title'] + "\n" + "Оценка: " + nfo['score'] + "\n" + nfo['link'],
							disable_notification = True
						)

				sg.update_lastkey(nfo['id'])

if __name__ == '__main__':
	loop = asyncio.get_event_loop()
	loop.create_task(scheduled(10))
	executor.start_polling(dp, skip_updates=True)
