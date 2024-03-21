from telegram import Update
from telegram.ext import ContextTypes
from keyboards import generate_user_keyboard
import math
from data import *

async def user_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = generate_user_keyboard(current_p=None)

    await update.message.reply_text(
        "Bu yerda siz ro'yhatdan o'tgan foydalanuvchilarni ko'rishingiz va ular haqida ma'lumot olishingiz mumkin.", 
        reply_markup=keyboard
    )


async def user_callback_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    data = update.callback_query.data
    chat_id = update.callback_query.message.chat.id
    if data.startswith('users'):
        _, current_p = data.split("|")
        current_p = int(current_p)
        keyboard = generate_user_keyboard(current_p)
        if keyboard == update.effective_message.reply_markup:
            await update.callback_query.answer("Siz allaqachon ushbu sahifadasiz!")
        else:
            if current_p == 0:
                return await update.callback_query.answer("Siz allaqachon birinchi sahifadasiz!")
            elif current_p == math.ceil(len(REGISTERED_USERS)/USERS_PER_PAGE) + 1:
                return await update.callback_query.answer("Siz allaqachon oxirgi sahifadasiz!")
            else:
                keyboard = generate_user_keyboard(current_p)
                await context.bot.edit_message_reply_markup(
                    chat_id=update.effective_chat.id,
                    message_id=update.effective_message.message_id,
                    reply_markup=keyboard
                )
    elif data.startswith('info'):
        _, id, current_p = data.split('|')
        id = int(id)
        current_p = int(current_p)
        keyboard = generate_user_keyboard(current_p)
        found_user = None
        for user in REGISTERED_USERS:
            if user['id'] == id:
                found_user = user
                break

        if found_user:
            info_message = f"Foydalanuvchi ma'lumotlari:\n\n"
            info_message += f"▪ Ism Familiya: {found_user['full_name']}\n"
            info_message += f"▪ Yosh: {found_user['age']}\n"
            info_message += f"▪ Tel: {found_user['phone_number']}\n"
            info_message += f"▪ Viloyat: {found_user.get('region', "N/A")}\n"
            info_message += f"▪ Tillar: {found_user.get('selected_languages_str', [])}\n"


            await update.callback_query.answer()
            await context.bot.send_message(chat_id=chat_id, text=info_message)
        else:
            await update.callback_query.answer()
            await update.callback_query.edit_message_text("😑Foydalanuvchi topilmadi!")
    elif data == 'cross':
        await update.callback_query.answer()
        await update.callback_query.edit_message_text("😊Ajratgan vaqtingiz uchun raxmat!")
