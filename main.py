from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton

bot = Bot(token='5203101527:AAE0fXaezWx_kJRDXIkvSBvyEMiu1jZJwlw')
dp = Dispatcher(bot)

button1 = KeyboardButton("Bot haqida")
button2 = KeyboardButton("Qo'llanma")
keyboard1 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(button1).add(button2)


@dp.message_handler(commands=['start', 'help'])
async def welcome(message: types.Message):
  await message.reply("Assalomu alaykum, botimizga hush kelibsiz", reply_markup=keyboard1)
  
  @dp.message_handler()
  async def kb_answer(message: types.Message):
    if message.text == 'Bot haqida':
      await message.answer('Salom %firstname% ushbu bot orqali/n matnlarni eng-uzb shaklida/n tarjima qila olasiz!)
                           elif message.text == "Qo'llanma":
                           await message.answer("Bot faqat eng-uzb shaklida tarjima qiladi!")
                           else:
                           await message.answer(f'Your message is: {message.text}')
  
  
  
  executer.start_polling(dp)
