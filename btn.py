import glob
import random
from typing import Any

import pynput
from playsound import playsound
from pynput.mouse import Button
import logging

log = logging.getLogger(__name__)

class MousePress:
    def __init__(self):
        self.last_pressed = None

    def get_btn_type(self, btn):
        if btn == Button.left:
            return "left"

        if btn == Button.right:
            return "right"

        else:
            return "middle"

    def on_click(self, x, y, btn, pressed):
        if pressed:
            self.on_press(btn)

        else:
            self.on_release(btn)

    def on_press(self, btn):
        if btn != self.last_pressed:
            btn_type = self.get_btn_type(btn)

            files = glob.glob('soundpack/{0}/down/*.mp3'.format(btn_type))
            playsound(random.choice(files), block=False)

            self.last_pressed = btn

    def on_release(self, btn) -> Any:
        btn_type = self.get_btn_type(btn)

        files = glob.glob('soundpack/{0}/up/*.mp3'.format(btn_type))
        playsound(random.choice(files), block=False)

        self.last_pressed = None

    def run(self):
        with pynput.mouse.Listener(on_move = None, on_click = self.on_click, on_scroll = None) as listener:
            listener.join()

if __name__ == '__main__':
    app = MousePress()
    app.run()
