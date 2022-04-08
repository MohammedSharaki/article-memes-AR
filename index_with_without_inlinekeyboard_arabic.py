import random
import os
from telegram.chataction import ChatAction
from time import sleep
from telegram.ext import Updater, CommandHandler, CallbackContext
from telegram.update import Update
from telegram.ext.updater import Updater

yourpath = r"D:\my articles\make bot using python\arabic meme"
lis = []

for root, dirs, files in os.walk(yourpath, topdown=False):
    for name in files:
        lis.append(os.path.join(root, name))
        print(lis)
print("loading.....")
API_KEY = '2071868441:AAGEKDCMCKQtkLf05Nj4PFu4nj7xxij_ZKE'


def start_commend(update: Update, context: CallbackContext):
    """
    message to handle any "Option [0-9]" Regrex.
    """
    context.bot.send_chat_action(
        chat_id=update.effective_chat.id, action=ChatAction.UPLOAD_PHOTO)
    chat_id = update.message.chat_id
    sleep(1)
    n = random.randint(0, 3)
    file = lis[n]

    context.bot.send_photo(chat_id, photo=open(file, 'rb'))


def main():
    updaters = Updater(API_KEY, use_context=True)
    dp = updaters.dispatcher
    dp.add_handler(CommandHandler("start", start_commend))
    updaters.start_polling()
    updaters.idle()


main()
