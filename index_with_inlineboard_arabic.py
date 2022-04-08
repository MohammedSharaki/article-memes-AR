import random
import os
from telegram.chataction import ChatAction
from time import sleep
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters
from telegram import ReplyKeyboardMarkup
from telegram.update import Update
from telegram.ext.updater import Updater

yourpath = r"D:\my articles\make bot using python\arabic meme"
lis = []

for root, dirs, files in os.walk(yourpath, topdown=False):
    for name in files:
        lis.append(os.path.join(root, name))
print("loading.....")
API_KEY = "2071868441:AAGEKDCMCKQtkLf05Nj4PFu4nj7xxij_ZKE"


def start_commend(update: Update, context: CallbackContext):
    kd_layout = [['ارسال ميم']]
    kbds = ReplyKeyboardMarkup(kd_layout)
    update.message.reply_text(
        text="""اضغط علي ارسال ميم """, reply_markup=kbds)


def echo(update: Update, context: CallbackContext):
    """
    message to handle any "Option [0-9]" Regrex.
    """
    context.bot.send_chat_action(
        chat_id=update.effective_chat.id, action=ChatAction.UPLOAD_PHOTO)
    chat_id = update.message.chat_id
    sleep(1)
    n = random.randint(0, 3)
    sleep(1)
    file = lis[n]
    if update.message.text == "ارسال ميم":

        context.bot.send_photo(chat_id, photo=open(file, 'rb'))


def main():
    updaters = Updater(API_KEY, use_context=True)
    dp = updaters.dispatcher
    dp.add_handler(CommandHandler("start", start_commend))
    dp.add_handler(MessageHandler(Filters.regex(r"."), echo))
    updaters.start_polling()
    updaters.idle()


main()
