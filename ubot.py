import time
import gc
import ujson
import urequests
from typing import List, Tuple, Union
from project_settings import settings
import ast


class TelegramLightsSequece():
    """Class that defines the format for telegram messages that can be converted to christmas light sequences"""
    def __init__(self):
        self.number_of_lights: int = settings["lights"]["number_of_lights"]
        self.max_sequence_length: int = settings["lights"]["max_sequence_length"]
        self.display_time: float = settings["lights"]["display_time"]
        self.full_sequence: List[List[Tuple[int, int, int]]] = [[(255, 255, 255) for i in range(self.number_of_lights)]]

    def check_sequence(self, str_sequence: str) -> Union[str, List]:
        try:
            sequence = ast.literal_eval(str_sequence)
        except SyntaxError:
            return "Light sequence not set up correctly. Most likely a missing bracket."

        if any(not isinstance(pixel_list, list) for pixel_list in sequence):
            return "Light sequence not adhering to expected type: List[List[tuple(int, int, int)]]"
        if any(not isinstance(pixel, int) or len(light) != 3
               for light_list in sequence
               for light in light_list
               for pixel in light):
            return "Light sequence not adhering to expected type: List[List[tuple(int, int, int)]]"

        if len(sequence) > self.max_sequence_length:
            return f"Sequence is too long, maximum length is {self.max_sequence_length}"

        if any(len(pixel_list) != self.number_of_lights for pixel_list in sequence):
            return f"List of pixel values is not consistent with actual number of lights ({self.number_of_lights})"

        if any(not all(0<=int(rgb_val)<=255 for rgb_val in pixel) for pixel_list in sequence for pixel in pixel_list):
            return "Pixel RGB values contain values outside the 0-255 range"

        return sequence

    def set_sequece(self, str_sequence):
        check_val = self.check_sequence(str_sequence)
        if isinstance(check_val, str):
            return check_val
        self.full_sequence = check_val


class ubot:

    def __init__(self, token, offset=0):
        self.url = 'https://api.telegram.org/bot' + token
        self.commands = {}
        self.default_handler = None
        self.message_offset = offset
        self.sleep_btw_updates = 3

        messages = self.read_messages()
        if messages:
            if self.message_offset == 0:
                self.message_offset = messages[-1]['update_id']
            else:
                for message in messages:
                    if message['update_id'] >= self.message_offset:
                        self.message_offset = message['update_id']
                        break

    def send(self, chat_id, text):
        data = ujson.dumps({'chat_id': chat_id, 'text': text})
        try:
            headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
            response = urequests.post(self.url + '/sendMessage', data=data, headers=headers)
            response.close()
            return True
        except:
            return False

    def send_gif(self, chat_id, text, gif_link):
        data = ujson.dumps({
            'chat_id': chat_id,
            'animation': gif_link,
            'caption': text
        })
        try:
            headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
            response = urequests.post(self.url + '/sendAnimation', data=data, headers=headers)
            response.close()
            return True
        except:
            return False

    def read_messages(self):
        result = []
        self.query_updates = {
            'offset': self.message_offset + 1,
            'limit': 1,
            'timeout': 30,
            'allowed_updates': ['message']}

        try:
            update_messages = urequests.post(self.url + '/getUpdates', json=self.query_updates).json()
            if 'result' in update_messages:
                for item in update_messages['result']:
                    result.append(item)
            return result
        except (ValueError):
            return None
        except (OSError):
            print("OSError: request timed out")
            return None

    def listen(self):
        while True:
            self.read_once()
            time.sleep(self.sleep_btw_updates)
            gc.collect()

    def read_once(self):
        messages = self.read_messages()
        if messages:
            if self.message_offset == 0:
                self.message_offset = messages[-1]['update_id']
                self.message_handler(messages[-1])
            else:
                for message in messages:
                    if message['update_id'] >= self.message_offset:
                        self.message_offset = message['update_id']
                        self.message_handler(message)
                        break

    def register(self, command, handler):
        self.commands[command] = handler

    def set_default_handler(self, handler):
        self.default_handler = handler

    def set_sleep_btw_updates(self, sleep_time):
        self.sleep_btw_updates = sleep_time

    def message_handler(self, message):
        if 'text' in message['message']:
            parts = message['message']['text'].split(' ')
            if parts[0] in self.commands:
                self.commands[parts[0]](message)
            else:
                if self.default_handler:
                    self.default_handler(message)
