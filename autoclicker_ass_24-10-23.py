import time
import threading
from random import uniform
from pynput.keyboard import  Controller, Listener, KeyCode, Key
from winsound import PlaySound, SND_ALIAS

start_stop_key = Key.f4
stop_key = Key.f4
#delay_intervalo = (2,3)
delay_intervalo = (140,160)
#pulsed_key = KeyCode(char="6")
pulsed_key = Key.f8

class Clickteclao(threading.Thread):

    def __init__(self, delay_intervalo, pulsed_key):
        super(Clickteclao, self).__init__()
        self.delay_intervalo = delay_intervalo 
        self.pulsed_key = pulsed_key
        self.running = False
        self.program_running = True
 
    def start_clicking(self):
        self.running = True
 
    def stop_clicking(self):
        self.running = False
 
    def exit(self):
        self.stop_clicking()
        self.program_running = False
 
    def run(self):
        while self.program_running:
            while self.running:
                self.delay = uniform(self.delay_intervalo[0], self.delay_intervalo[1])
                time.sleep(self.delay)
                teclao.press(pulsed_key)
                teclao.release(pulsed_key)
            time.sleep(0.1)

teclao = Controller()
click_thread = Clickteclao(delay_intervalo, pulsed_key)
click_thread.start()
 
def on_press(key):
   
    if key == start_stop_key:
        if click_thread.running:
            #winsound.PlaySound("beep-08b.wav", winsound.SND_ALIAS)
            #winsound.PlaySound("beep-07a.wav", winsound.SND_ALIAS)
            PlaySound("SystemHand", SND_ALIAS)
            print(" - - - - OFF - - - -")
            click_thread.stop_clicking()
        else:
            #winsound.PlaySound("beep-07a.wav", winsound.SND_ALIAS)
            #winsound.PlaySound("beep-08b.wav", winsound.SND_ALIAS)
            PlaySound("SystemExit", SND_ALIAS)
            print(" + + + + ON  + + + +")
            click_thread.start_clicking()
           
    elif key == stop_key:
        click_thread.exit()
        listener.stop()
 
with Listener(on_press=on_press) as listener:
    listener.join()

