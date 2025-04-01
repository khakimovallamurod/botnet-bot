from telegram.ext import Application, CommandHandler, MessageHandler, filters
import handlears
import config

def main():
    TOKEN = config.get_token()

    db = Application.builder().token(TOKEN).build()

    db.add_handler(CommandHandler('start', handlears.start))
    db.add_handler(MessageHandler(filters.PHOTO & ~filters.COMMAND, handlears.photo_message))

    db.run_polling()

if __name__ == '__main__':
    main()
