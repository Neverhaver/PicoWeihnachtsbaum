from telegram.ext import Updater, CallbackContext
from telegram import Update
from project_settings import settings
import multiprocessing
import random
import logging
import baum
import giphy
from time import time, sleep
from tls_class import TelegramLightsSequece

proc = multiprocessing.Process(target=baum.running_lights, args=())
proc.start()
print('startet')

token = settings["telegram"]["token"]  # telegram bot object
chat_id = settings["telegram"]["chat_id"]  # chat_id
updater = Updater(token=token, use_context=True)

dispatcher = updater.dispatcher
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)


def template(update: Update, context: CallbackContext, func, gif, caption):
    global proc
    if proc.is_alive():
        proc.terminate()
    context.bot.send_animation(chat_id=update.effective_chat.id,
                               animation=gif,
                               caption=caption)
    proc = multiprocessing.Process(target=func, args=())
    proc.start()


def white(update: Update, context: CallbackContext):
    template(update, context, baum.white,
             random.choice(giphy.gif_links['white']),
             'Weißer Baum')


def redgreen(update: Update, context: CallbackContext):
    template(update, context, baum.running_lights,
             random.choice(['https://media.giphy.com/media/GepjBlRKsD1uM/giphy.gif',
                            'https://media.giphy.com/media/eIG0HfouRQJQr1wBzz/giphy.gif',
                            'https://media.giphy.com/media/f72BA6kQXT4uQ/giphy.gif',
                            'https://media.giphy.com/media/S14tfL9B3U89sJKzqp/giphy.gif',
                            'https://media.giphy.com/media/Kzh29jxgcvv6tzdrIx/giphy.gif',
                            'https://media.giphy.com/media/PE04aN8plA7q8/giphy.gif']),
             'Rot und Grün läuft')


def start_rainbow(update: Update, context: CallbackContext):
    template(update, context, baum.rainbow,
             random.choice(['https://media.giphy.com/media/f5GyIBXJ3L0DS/giphy.gif',
                            'https://media.giphy.com/media/SKGo6OYe24EBG/giphy.gif',
                            'https://media.giphy.com/media/3o7TKNOYAv36eKJJra/giphy.gif',
                            'https://media.giphy.com/media/13AcmSNW5O7WV2/giphy.gif',
                            'https://media.giphy.com/media/AMCWmzsrL4He0/giphy.gif']),
             'Regenbogen \U0001F308')


def random_pulse(update: Update, context: CallbackContext):
    template(update, context, baum.pulse_random,
             random.choice(['https://media.giphy.com/media/chhT3mXVWab3jb1m2O/giphy.gif',
                            'https://media.giphy.com/media/xT5LMOnWyP9zZAzVXa/giphy.gif',
                            'https://media.giphy.com/media/26nfoKekcJcS0vImQ/giphy.gif']),
             'Pulsiert')


def very_random(update: Update, context: CallbackContext):
    template(update, context, baum.random_colors,
             random.choice(['https://media.giphy.com/media/zxxXYJqTlpBnO/giphy.gif',
                            'https://media.giphy.com/media/3orif1K3IJuX9UT1ra/giphy.gif',
                            'https://media.giphy.com/media/XBhzUNf7ta00w/giphy.gif',
                            'https://media.giphy.com/media/LwzDBXlwVOGz7zi8cp/giphy.gif']),
             'Mehr Farben')


def snaking(update: Update, context: CallbackContext):
    template(update, context, baum.an_und_aus,
             random.choice(['https://media.giphy.com/media/QtZKO7mb7ebpC/giphy.gif',
                            'https://media.giphy.com/media/3o72F7JTbNletrGzvO/giphy.gif'
                            'https://media.giphy.com/media/82DloUKOW5A76/giphy.gif',
                            'https://media.giphy.com/media/zPdwt79PXjMEo/giphy.gif']),
             'SssssSSSsssSsSSs \U0001F40D')


def bayern(update: Update, context: CallbackContext):
    template(update, context, baum.bayern,
             random.choice(['https://media.giphy.com/media/9DgffJbVRdAQeaLlWK/giphy.gif',
                            'https://media.giphy.com/media/3o7TKv9QWAFaac5XnG/giphy.gif',
                            'https://media.giphy.com/media/9DjXWKkutc2x8GtlO1/giphy.gif',
                            'https://media.giphy.com/media/3o7TKVmIIEFg62RWk8/giphy.gif',
                            'https://media.giphy.com/media/l2Je9wxCkedW0WRck/giphy.gif',
                            'https://media.giphy.com/media/AxVvk1zpoie6EfYFnW/giphy.gif']),
             'Ozapft is')


def stop(update: Update, context: CallbackContext):
    template(update, context, baum.off,
             random.choice(giphy.gif_links['finish']),
             'Aus und vorbei')


def read_tls(update: Update, context: CallbackContext):
    tls = TelegramLightsSequece()
    if not '[' in update.message.text:
        random_gif_result, _ = giphy.get_gif(update.message.text)
        context.bot.send_animation(
            chat_id=update.effective_chat.id,
            animation=random_gif_result,
            caption="I did not understand you, so here is a random gif, based on your message",
        )
        return
    checked_message = tls.set_sequece(update.message.text)
    if checked_message:
        context.bot.send_animation(
            chat_id=update.effective_chat.id,
            animation=random.choice(giphy.gif_links['error']),
            caption=f"Error: {checked_message}"
        )
        return

    template(update, context, baum.show_telegram_sequence(tls),
             random.choice(giphy.gif_links['start']),
             'Doing what you told me')


def random_selected_gif(update: Update, context: CallbackContext):
    context.bot.send_animation(
        chat_id=update.effective_chat.id,
        animation=random.choice(giphy.gif_links['other']),
        caption="Good choice, here is a gif for you  \U0001F49D",
    )

from telegram.ext import CommandHandler, MessageHandler, Filters
weisser_baum = CommandHandler('white', white)
dispatcher.add_handler(weisser_baum)
stop_baum = CommandHandler('black', stop)
dispatcher.add_handler(stop_baum)
gruenrot_baum = CommandHandler('redgreen', redgreen)
dispatcher.add_handler(gruenrot_baum)
rainbow_handler = CommandHandler('rainbow', start_rainbow)
dispatcher.add_handler(rainbow_handler)
pulse_handler = CommandHandler('randompulse', random_pulse)
dispatcher.add_handler(pulse_handler)
very_random_handler = CommandHandler('veryrandom', very_random)
dispatcher.add_handler(very_random_handler)
random_handler = CommandHandler('snaking', snaking)
dispatcher.add_handler(random_handler)
bayern_handler = CommandHandler('bayern', bayern)
dispatcher.add_handler(bayern_handler)
gif_handler = CommandHandler('gif', random_selected_gif)
dispatcher.add_handler(gif_handler)
message_handler = MessageHandler(Filters.text, callback=read_tls)
dispatcher.add_handler(message_handler)

updater.start_polling()
