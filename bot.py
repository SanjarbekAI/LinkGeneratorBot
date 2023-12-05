from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

API_TOKEN = '6432695102:AAFgw8IcBv9PYLLG98oCaHRYMY3NMhwJ0BQ'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

ADMINS = [5374970910]

generate_link_button = ReplyKeyboardMarkup(
    keyboard=[[
        KeyboardButton(text="🔗 Link olish")
    ]], resize_keyboard=True
)


@dp.message_handler(commands="start", chat_id=ADMINS)
async def admin_start_handler(message: types.Message):
    print(message)
    text = "Bir marttalik link olish uchun pastdagi tugmadan foydalaning"
    await message.answer(text=text, reply_markup=generate_link_button)


@dp.message_handler(text="🔗 Link olish")
async def create_invite_link(message: types.Message):
    try:
        chat_id = -1002140470690
        result = await bot.create_chat_invite_link(chat_id=chat_id, member_limit=1)
        invite_link = result.invite_link

        await message.reply(text=invite_link)
    except Exception as e:
        await message.reply(f"Qaytadan urinib ko'ring: {e}")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
