# whenever a text start with '/' its a command , other than this its a message
# for every message we need message handler and command

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

def start (update, context):
    update.message.reply_text("UwU")

def help(update, context):
    update.message.reply_text("Hewp :o")

def handle_text(update,context):
    update.message.reply_text(owo.text_to_owo(update.message.text))


def main():
    updater = Updater("YOUR-BOT-API-KEY", use_context=True)

    dp =updater.dispatcher #this is where you register your handlers

    dp.add_handler(CommandHandler("start",start))
    dp.add_handler(CommandHandler("help",help))

    dp.add_handler(MessageHandler(Filters.text,handle_text))

    updater.start_polling()
    updater.idle()


if __name__=='__main__':
    main()



