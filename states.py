import math
from telegram import (
    ReplyKeyboardRemove,
    ReplyKeyboardMarkup,
    KeyboardButton,
    Update,
    InlineKeyboardMarkup,
)
from telegram.ext import (
    CommandHandler,
    ContextTypes,
    ConversationHandler,
    MessageHandler,
    filters,
    CallbackQueryHandler,
)

from data import *
from keyboards import (
    generate_region_inline_keyboard,
    generate_language_keyboard,
    send_contact,
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Assalomu alaykum! Botdan foydalanish uchun ro'yhatdan o'tishingiz lozim!\n\nRo'yhatdan o'tish uchun 👉🏻 /register ni bosing."
    )


async def register(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✍️ Ismingizni yozing!")
    return NAME


async def name(update: Update, context: ContextTypes.DEFAULT_TYPE):
    name = update.message.text
    context.user_data["name"] = name
    await update.message.reply_text("✍️ Familiyangizni yozing!")
    return SURNAME


async def surname(update: Update, context: ContextTypes.DEFAULT_TYPE):
    surname = update.message.text
    context.user_data["surname"] = surname
    await update.message.reply_text("📅 Necha yoshdasiz?")
    return AGE


async def age(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        age = int(update.message.text)
        if age >= 10:
            context.user_data["age"] = age
            await update.message.reply_text(
                "📱 Telefon raqamingizni jo'nating!", reply_markup=send_contact()
            ),
            return PHONE_NUMBER
        else:
            await update.message.reply_text(
                "Ro'yhatdan o'tish uchun yoshingiz 10 yoki undan yuqori bo'lishi shart!"
            )
            return AGE
    except:
        await update.message.reply_text("Iltimos, faqat butun son kiriting!")
        return AGE


async def phone_number(update: Update, context: ContextTypes.DEFAULT_TYPE):
    phone_number = update.message.contact.phone_number
    context.user_data["phone_number"] = "+" + phone_number
    await update.message.reply_text(
        f"Raqamingiz qabul qilindi!\n👉🏻 +{phone_number}",
        reply_markup=ReplyKeyboardRemove(),
    )
    await update.message.reply_text(
        "📍 Qasyi Viloyatdansiz?",
        reply_markup=InlineKeyboardMarkup(generate_region_inline_keyboard()),
    )
    return REGION


async def region(update: Update, context: ContextTypes.DEFAULT_TYPE):
    region = update.callback_query.data
    context.user_data["region"] = region
    await update.callback_query.answer()
    await update.callback_query.edit_message_text(
        "Biladigan tillaringizn Tanlang\n(tugatgach ✔️Done tugmasini bosing)",
        reply_markup=generate_language_keyboard(context, None, None),
    ),

    return LANGUAGE


async def lang_callback_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    data = update.callback_query.data
    if "languages" not in context.user_data:
        context.user_data["languages"] = set()
    if data.startswith("lang"):
        _, current_p = data.split("|")
        current_p = int(current_p)
        keyboard = generate_language_keyboard(context, data, current_p)
        if keyboard == update.effective_message.reply_markup:
            await update.callback_query.answer("Siz allaqachon ushbu sahifadasiz!")
        else:
            if current_p == 0:
                await update.callback_query.answer(
                    "Siz allaqachon birinchi sahifadasiz!"
                )
                return LANGUAGE
            elif current_p == math.ceil(len(leng_list) / 3) + 1:
                await update.callback_query.answer("Siz allaqachon oxirgi sahifadasiz!")
                return LANGUAGE
            else:
                keyboard = generate_language_keyboard(context, data, current_p)
                await context.bot.edit_message_reply_markup(
                    chat_id=update.effective_chat.id,
                    message_id=update.effective_message.message_id,
                    reply_markup=keyboard,
                )

    elif data.startswith("Done"):
        if not context.user_data["languages"]:
            msg = "❗Iltimos kamida bitta tilni tanlang.\n\nBiladigan tillaringizn Tanlang\n(tugatgach ✔️Done tugmasini bosing)"
            if msg != update.effective_message.text:
                await update.callback_query.edit_message_text(
                    "❗Iltimos kamida bitta tilni tanlang.\n\nBiladigan tillaringizn Tanlang\n(tugatgach ✔️Done tugmasini bosing)",
                    reply_markup=generate_language_keyboard(context, data, None),
                )
            else:
                await update.callback_query.answer(
                    "Siz biror tilni tanlashingiz lozim!"
                )

            return LANGUAGE

        selected_languages = context.user_data["languages"]
        selected_languages_str = ""
        for l in selected_languages:
            if l in LANGUAGES.keys():
                selected_languages_str += f"{LANGUAGES[l]}, "

        if REGISTERED_USERS:
            id = REGISTERED_USERS[-1]["id"] + 1
        else:
            id = 1
        context.user_data["id"] = id
        full_name = context.user_data["name"] + " " + context.user_data["surname"]
        age = context.user_data["age"]
        phone_number = context.user_data["phone_number"]
        region = context.user_data["region"]

        user_data = {
            "full_name": full_name,
            "age": age,
            "phone_number": phone_number,
            "region": region,
            "selected_languages_str": selected_languages_str,
            "id": id,
        }
        REGISTERED_USERS.append(user_data)
        await update.callback_query.answer()
        await update.callback_query.edit_message_text(
            f"✅Ro'yhatdan muvaffaqiyatli o'tdingiz!\n\nSizning ma'lumotlaringiz.\n\n▫ Ism Familiya: {full_name}\n▫ Yosh: {age}\n▫ Tel: {phone_number}\n▫ Viloyat: {region}\n▫ Tillar: {selected_languages_str}",
        )
        return ConversationHandler.END
    elif data.startswith("for"):
        _, key, current_p = data.split("|")
        current_p = int(current_p)

        if key in context.user_data["languages"]:
            context.user_data["languages"].remove(key)
        else:
            context.user_data["languages"].add(key)

        await update.callback_query.edit_message_text(
            "Biladigan tillaringizn Tanlang\n(tugatgach ✔️Done tugmasini bosing)",
            reply_markup=generate_language_keyboard(context, data, current_p),
        )
        return LANGUAGE


async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "So'g bo'ling. Ishlarizga omad!", reply_markup=ReplyKeyboardRemove()
    )
    return ConversationHandler.END


conv_handler = ConversationHandler(
    entry_points=[CommandHandler("register", register)],
    states={
        NAME: [MessageHandler(filters.TEXT & ~filters.COMMAND, name)],
        SURNAME: [MessageHandler(filters.TEXT & ~filters.COMMAND, surname)],
        AGE: [MessageHandler(filters.TEXT & ~filters.COMMAND, age)],
        PHONE_NUMBER: [
            MessageHandler(filters.CONTACT & ~filters.COMMAND, phone_number)
        ],
        REGION: [CallbackQueryHandler(region)],
        LANGUAGE: [CallbackQueryHandler(lang_callback_handler)],
    },
    fallbacks=[CommandHandler("cancel", cancel)],
)
