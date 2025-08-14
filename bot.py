# My-telegram-bot

from telegram.ext import Updater, CommandHandler  # اصلاح: "telogram" → "telegram"

def start(update, context):  # اصلاح: "updates" → "update"
    update.message.reply_text('ربات شما فعال است! 🎉')  # اصلاح متن پیام

TOKEN = "8213374526:AAHkNk-bR8lLa-tOctRXfNgumgWhJD8n3ow"
updater = Updater(TOKEN, use_context=True)  # اصلاح: پرانتز و ویرگول
updater.dispatcher.add_handler(CommandHandler('start', start))  # اصلاح: "shapstone" → "dispatcher"
updater.start_polling()  # اصلاح: "start_pulling" → "start_polling"
