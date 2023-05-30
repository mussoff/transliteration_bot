import os
import logging

from aiogram import Bot, Dispatcher, executor, types

TOKEN = os.getenv('TOKEN')

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    text = f'Привет, {user_name}! Напиши фамилию, имя и отчество'
    logging.info(f'{user_name=} {user_id} sent message: {message.text}')
    await message.reply(text)


@dp.message_handler()
async def send_translit_name(message: types.Message):
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    text = message.text
    dict = {'a':'A', 'б':'B', 'в':'V', 'г':'G', 'д':'D', 'е':'E', 'ё':'E', 'ж':'ZH', 'з':'Z', 'и':'I', 'й':'I', 'к':'K', 
            'л':'L', 'м':'M', 'н':'N', 'о':'O', 'п':'P', 'р':'R', 'с':'S', 'т':'T', 'у':'U', 'ф':'F', 'х':'KH', 'ц':'TS',
            'ч':'CH', 'ш':'SH', 'щ':'SHCH', 'ъ':'IE', 'ы':'Y', 'ь' : '', 'э':'E', 'ю':'IU', 'я':'IA'}
    for key in dict:
        text = text.lower().replace(key, dict[key]).upper()
    logging.info(f'{user_name=} {user_id} sent message: {message.text}, got response: {text}')
    await bot.send_message(user_id, text)


if __name__ == '__main__':
    executor.start_polling(dp)