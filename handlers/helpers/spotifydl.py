import os
import subprocess
from typing import List

from telegram import Update
from telegram.ext import CallbackContext


def downspotify(download_path: str, link: List[str]):
    os.mkdir(download_path)
    os.chdir(download_path)
    os.system(f'spotdl {link}')
    os.chdir("..")


def sendspotify(download_path: str, update: Update, context: CallbackContext):
    directory = os.listdir(download_path)
    for file in directory:
        if not file.endswith(".mp3"):
            continue
        result = context.bot.send_audio(
            caption=("From ✳️ @SongJeBot ✳️"),
            chat_id=update.effective_chat.id,
            audio=open(f'{download_path}/{file}', 'rb')
        )

    subprocess.run(['rm', '-r', download_path])
