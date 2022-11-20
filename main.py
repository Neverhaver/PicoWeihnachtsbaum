from project_settings import settings, gif_links
import multiprocessing
import random
import logging
import baum_pico
import ubot
import giphy
from time import time, sleep

proc = multiprocessing.Process(target=baum_pico.running_lights, args=())
proc.start()
print('startet')

token = settings["telegram"]["token"]  # telegram bot object
chat_id = settings["telegram"]["chat_id"]  # chat_id
bot = ubot.ubot(token=token)
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)


def template(chat_origin_id, func, gif, caption):
    global proc
    if proc.is_alive():
        proc.terminate()
    bot.send_animation(chat_id=chat_origin_id,
                       animation=gif,
                       caption=caption)
    proc = multiprocessing.Process(target=func, args=())
    proc.start()


def start(chat_origin_id):
    template(chat_origin_id, baum_pico.white,
             random.choice(gif_links['start']),
             'Weißer Baum')


def redgreen(chat_origin_id):
    template(chat_origin_id, baum_pico.running_lights,
             random.choice(['https://media.giphy.com/media/GepjBlRKsD1uM/giphy.gif',
                            'https://media.giphy.com/media/eIG0HfouRQJQr1wBzz/giphy.gif',
                            'https://media.giphy.com/media/f72BA6kQXT4uQ/giphy.gif',
                            'https://media.giphy.com/media/S14tfL9B3U89sJKzqp/giphy.gif',
                            'https://media.giphy.com/media/Kzh29jxgcvv6tzdrIx/giphy.gif',
                            'https://media.giphy.com/media/PE04aN8plA7q8/giphy.gif']),
             'Rot und Grün läuft')


def start_rainbow(chat_origin_id):
    template(chat_origin_id, baum_pico.rainbow,
             random.choice(['https://media.giphy.com/media/f5GyIBXJ3L0DS/giphy.gif',
                            'https://media.giphy.com/media/SKGo6OYe24EBG/giphy.gif',
                            'https://media.giphy.com/media/3o7TKNOYAv36eKJJra/giphy.gif',
                            'https://media.giphy.com/media/13AcmSNW5O7WV2/giphy.gif',
                            'https://media.giphy.com/media/AMCWmzsrL4He0/giphy.gif']),
             'Regenbogen \U0001F308')


def random_pulse(chat_origin_id):
    template(chat_origin_id, baum_pico.pulse_random,
             random.choice(['https://media.giphy.com/media/chhT3mXVWab3jb1m2O/giphy.gif',
                            'https://media.giphy.com/media/xT5LMOnWyP9zZAzVXa/giphy.gif',
                            'https://media.giphy.com/media/26nfoKekcJcS0vImQ/giphy.gif']),
             'Pulsiert')


def very_random(chat_origin_id):
    template(chat_origin_id, baum_pico.random_colors,
             random.choice(['https://media.giphy.com/media/zxxXYJqTlpBnO/giphy.gif',
                            'https://media.giphy.com/media/3orif1K3IJuX9UT1ra/giphy.gif',
                            'https://media.giphy.com/media/XBhzUNf7ta00w/giphy.gif',
                            'https://media.giphy.com/media/LwzDBXlwVOGz7zi8cp/giphy.gif']),
             'Mehr Farben')


def snaking(chat_origin_id):
    template(chat_origin_id, baum_pico.an_und_aus,
             random.choice(['https://media.giphy.com/media/QtZKO7mb7ebpC/giphy.gif',
                            'https://media.giphy.com/media/3o72F7JTbNletrGzvO/giphy.gif'
                            'https://media.giphy.com/media/82DloUKOW5A76/giphy.gif',
                            'https://media.giphy.com/media/zPdwt79PXjMEo/giphy.gif']),
             'SssssSSSsssSsSSs \U0001F40D')


def bayern(chat_origin_id):
    template(chat_origin_id, baum_pico.bayern,
             random.choice(['https://media.giphy.com/media/9DgffJbVRdAQeaLlWK/giphy.gif',
                            'https://media.giphy.com/media/3o7TKv9QWAFaac5XnG/giphy.gif',
                            'https://media.giphy.com/media/9DjXWKkutc2x8GtlO1/giphy.gif',
                            'https://media.giphy.com/media/3o7TKVmIIEFg62RWk8/giphy.gif',
                            'https://media.giphy.com/media/l2Je9wxCkedW0WRck/giphy.gif',
                            'https://media.giphy.com/media/AxVvk1zpoie6EfYFnW/giphy.gif']),
             'Ozapft is')


def stop(chat_origin_id):
    template(chat_origin_id, baum_pico.off,
             random.choice(gif_links['finish']),
             'Aus und vorbei')


last_executed_message = 0
timestamp_pico_start = time()

while True:
    messages = bot.read_messages()
    for result in messages:
        if result['message']['date'] < timestamp_pico_start:
            continue
        if int(result['update_id']) < last_executed_message:
            last_executed_message = int(result['update_id'])
            message_text = result['message']['text']
            chat_origin_id = result['message']['from']['id']

            if message_text == "/start":
                start(chat_origin_id)
                continue
            elif message_text == "/stop":
                stop(chat_origin_id)
                continue
            elif message_text == "/redgreen":
                redgreen(chat_origin_id)
                continue
            elif message_text == "/rainbow":
                start_rainbow(chat_origin_id)
                continue
            elif message_text == "/randompulse":
                random_pulse(chat_origin_id)
                continue
            elif message_text == "/veryrandom":
                very_random(chat_origin_id)
                continue
            elif message_text == "/snaking":
                snaking(chat_origin_id)
                continue
            elif message_text == "/bayern":
                bayern(chat_origin_id)
                continue

            if message_text[0] == '[':
                tls = ubot.TelegramLightsSequece()
                checked_message = tls.set_sequece(message_text)
                if isinstance(checked_message, str):
                    bot.send_gif(
                        chat_origin_id,
                        f"Error: {checked_message}",
                        random.choice(gif_links['error'])
                    )
                continue

            random_gif_result, _ = giphy.get_gif(message_text)

            bot.send_gif(
                chat_origin_id,
                "Could not interpret your message as a light-command, so here is a random gif, based on your message",
                random_gif_result
            )
            sleep(1)
        sleep(1)
