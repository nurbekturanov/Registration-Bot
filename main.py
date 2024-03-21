from telegram.ext import Application, CommandHandler, CallbackQueryHandler
from telegram import Update
from users_handler import user_handler, user_callback_handler
from states import conv_handler, start
import settings


def main() -> None:
    app = Application.builder().token(settings.BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(conv_handler)
    app.add_handler(CommandHandler("users", user_handler))
    app.add_handler(CallbackQueryHandler(user_callback_handler))

    app.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
