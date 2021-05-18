import os
import uuid

from handlers.helpers import spotifydl
from telegram import Update
from telegram.ext import CallbackContext


def botify(update: Update, context: CallbackContext):
    song_link = context.args[0]
    download_path = os.getcwd() + "/" + str(uuid.uuid4())

    context.bot.sendChatAction(chat_id =update.effective_chat.id,  action = "typing")
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐢𝐧𝐠 🔁")
    

    context.bot.sendChatAction(chat_id =update.effective_chat.id,  action = "record_video")
    spotifydl.downspotify(download_path, song_link)
    
    context.bot.sendChatAction(chat_id =update.effective_chat.id,  action = "record_audio")
    spotifydl.sendspotify(download_path, update, context)


