"""
CS 246 Python Repository
This is a basic game of Pong that plays in the console.
"""

import keyboard
import time

running = False

def start():
    global running
    running = True
    game_loop()

def game_loop():
    global running
    while running == True:
        tick()
        time.sleep(.03)

def tick():
    global running
    print("tick")
    if keyboard.is_pressed(chr(27)):
        running = False

def main ():
    start()

if __name__ == "__main__":
    main()