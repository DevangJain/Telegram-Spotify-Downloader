import logging
import os

from handlers import sender
from handlers.helpers import spotifydl
from telegram import Update
from telegram.ext import CallbackContext, CommandHandler, Updater
from telegram import InlineKeyboardMarkup, InlineKeyboardbutton



logger = logging.getLogger(__name__)


def setup_logging():
    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO
    )
 
def start(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="""
-·=»‡«=·- ֆքօȶɨʄʏ ɖօառʟօǟɖ ɮօȶ -·=»‡«=·-
        
🍭  🎀  Featureʂ 🎀  🍭     
* Can download any spotify song.
* Can download any spotify playlist-(❌BETA-SLOW❌)
* Premium song supported
* Free Lol!

* 𝕌𝕊𝔼 /help 𝔽𝕆ℝ 𝕄𝕆ℝ𝔼 𝕀ℕ𝔽𝕆*
Made with💚by @phantomxhawk

[https://telegra.ph/file/ff06b4802f3a2ac7b6343.jpg]
""")

keyboard = [[
        InlineKeyboardButton("Option 1", callback_data='1'),
        InlineKeyboardButton("Option 2", callback_data='2')
    ], [InlineKeyboardButton("Option 3", callback_data='3')]]


    reply_markup = InlineKeyboardMarkup(keyboard)

     
def help(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="""
🍮♠ ʊֆǟɢɛ ♠🍮\n
*SINGLE  - Type /𝙨𝙥𝙤𝙩𝙞𝙛𝙮 "Song url"
*PLAYLIST- Type /𝙨𝙥𝙤𝙩𝙞𝙛𝙮 "Playlist url" (❌BETA-SLOW❌)""")
    
def error(update: Update, context: CallbackContext, error):
    logger.warning('Update "%s" caused error "%s"', update, error)
    

def main():
    TOKEN = os.environ.get('TOKEN')
    APP_NAME = os.environ.get('APP_NAME')

    # Port is given by Heroku
    PORT = os.environ.get('PORT')

    # Set up the Updater

    updater = Updater(
        TOKEN,
        use_context=True,
    )
    dp = updater.dispatcher
    # Add handlers
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('help', help))
    dp.add_error_handler(error)

    dp.add_handler(
        CommandHandler(
            'spotify',
            sender.botify,
            pass_args=True,
            pass_job_queue=True,
            pass_chat_data=True
        )
    )
    dp.add_handler(
        CommandHandler(
            'spotifydl',
            sender.botify,
            pass_args=True,
            pass_job_queue=True,
            pass_chat_data=True
        )
    )    
    dp.add_handler(CommandHandler(
            'help',
            sender.botify,
            pass_args=True,
            pass_job_queue=True,
            pass_chat_data=True
        )
    )    

    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
