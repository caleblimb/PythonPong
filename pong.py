"""
CS 246 Python Repository
This is a basic game of Pong that plays in the console.
"""

import keyboard
import time

running = False

#Initializes game variables and conditions
def start():
    global running
    running = True
    game_loop()

#Basic game loop
def game_loop():
    global running
    while running == True:
        tick()
        time.sleep(.05)

#Updates game
def tick():
    global running
    #Check for Escape key to Quit
    if keyboard.is_pressed(chr(27)):
        running = False
    draw()

#Draws game to console
def draw():
    print ("\n" * 50)
    print ("Press Escape to Quit")

#Main method
def main ():
    start()

if __name__ == "__main__":
    main()