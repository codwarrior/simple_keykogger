from pynput.mouse import Controller
from pynput.keyboard import Controller

def mousecontrol():
    mouse=Controller()
    mouse.position=(100,200)

def keyboardcontrol():
    keyboard=Controller()
    keyboard.type("I am Tasnim")

keyboardcontrol()
