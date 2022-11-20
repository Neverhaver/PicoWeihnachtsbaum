import board
import neopixel
import time
import random
from tls_class import TelegramLightsSequece
from project_settings import settings
import numpy as np

pixel_pin = board.D21
num_pixels = settings["lights"]["number_of_lights"]
ORDER = neopixel.GRB

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER)


def show_telegram_sequence(tls: TelegramLightsSequece):
    try:
        while True:
            for light_list in tls.full_sequence:
                for i in range(len(light_list)):
                    pixels[i] = light_list[i]
                pixels.show()
                time.sleep(tls.display_time)
    except:
        pass


def white():
    pixels.fill((150, 255, 30))
    pixels.show()


def off():
    pixels.fill((0, 0, 0))
    pixels.show()


def rainbow():
    def wheel(pos):
        # Input a value 0 to 255 to get a color value.
        # The colours are a transition r - g - b - back to r.
        if pos < 0 or pos > 255:
            r = g = b = 0
        elif pos < 85:
            r = int(pos * 3)
            g = int(255 - pos * 3)
            b = 0
        elif pos < 170:
            pos -= 85
            r = int(255 - pos * 3)
            g = 0
            b = int(pos * 3)
        else:
            pos -= 170
            r = 0
            g = int(pos * 3)
            b = int(255 - pos * 3)
        return (r, g, b)  # if ORDER in (neopixel.RGB, neopixel.GRB) else (r, g, b, 0)

    def rainbow_cycle(wait):
        for j in range(255):
            for i in range(num_pixels):
                pixel_index = (i * 256 // num_pixels) + j
                pixels[i] = wheel(pixel_index & 255)
            pixels.show()
            time.sleep(wait)

    while True:
        rainbow_cycle(0.05)  # rainbow cycle with 1ms delay per step


def running_lights():
    def insert_top_to_bottom(test_list):
        return [test_list[-1]] + test_list[0: -1]

    def insert_bottom_to_top(test_list):
        return test_list[1:] + [test_list[0]]

    lights = [(0, 0, 0) for i in range(num_pixels)]
    len_sleep = 0.2
    for i in range(int(round(num_pixels/2))):
        lights[i] = (255, 0, 0)
        if i > 45:
            lights[i] = (int(255 - (i - 45) / 5 * 255), int((i - 45) / 6 * 255), 0)

    for i in range(int(round(num_pixels/2)), num_pixels):
        lights[i] = (0, 255, 0)
        if i > 95:
            lights[i] = (int((i - 95) / 5 * 255), int(255 - (i - 95) / 6 * 255), 0)

    pixels.show()
    time.sleep(len_sleep)

    while True:
        lights = insert_bottom_to_top(lights)
        for i in range(len(lights)):
            pixels[i] = lights[i]

        pixels.show()
        time.sleep(len_sleep)


def pulse_random():
    t = 0
    num_lights = 20
    len_pulse = 200

    def percent_pulse(t):
        return

    def pulses(t):
        percent = int((np.sin(2 * np.pi * t / 1000) + 1) * 255 / 2)
        percent = percent / 255
        # print(percent)
        return (int(150 * percent), int(255 * percent), int(30 * percent))

    active_lights = random.sample(range(100), num_lights)
    already_changed = True

    while True:
        val_pulse = pulses(t)
        if val_pulse[0] < 5 and not already_changed:
            active_lights = random.sample(range(100), num_lights)
            already_changed = True
            # print(active_lights)
        if val_pulse[0] > 5:
            already_changed = False

        for pix in active_lights:
            pixels[pix] = val_pulse
        for i in range(100):
            if i not in active_lights:
                pixels[i] = (0, 0, 0)
        pixels.show()
        # time.sleep(0.01)
        t = t + 1

def random_colors():
    list_cols = [(random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255)) for i in range(num_pixels)]
    while True:
        for i in range(num_pixels):
            pixels[i] = list_cols[i]
        pixels.show()
        time.sleep(2)
        list_new_cols = [(random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255)) for i in
                         range(num_pixels)]
        # while i < 20:
        #
        #    time.sleep(0.1)
        list_cols = list_new_cols


def an_und_aus():
    while True:
        for i in range(num_pixels):
            pixels[i] = ((150, 255, 30))
            pixels.show()
            time.sleep(0.05)
        for i in range(num_pixels):
            pixels[i] = ((0, 0, 0))
            pixels.show()
            time.sleep(0.05)


def bayern():
    def insert_top_to_bottom(test_list):
        return [test_list[-1]] + test_list[0: -1]

    def insert_bottom_to_top(test_list):
        return test_list[1:] + [test_list[0]]

    lights = [(0, 0, 0) for i in range(num_pixels)]
    len_sleep = 0.2
    for i in range(25):
        lights[i] = (255, 255, 255)

    for i in range(25, 50):
        lights[i] = (0, 0, 255)

    for i in range(50, 75):
        lights[i] = (255, 255, 255)

    for i in range(75, 100):
        lights[i] = (0, 0, 255)

    # print(lights)
    pixels.show()
    time.sleep(len_sleep)

    while True:
        lights = insert_bottom_to_top(lights)
        for i in range(len(lights)):
            pixels[i] = lights[i]

        pixels.show()
        time.sleep(len_sleep)


# rainbow()
# running_lights()
# pulse_random()
# random_colors()
# an_und_aus()
# bayern()

# off()
# white()

if __name__ == '__main__':
    running_lights()
