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
        except ValueError:
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
