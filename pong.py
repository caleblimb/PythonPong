"""
CS 246 Python Repository
This is a basic game of Pong that plays in the console.
"""

import keyboard
import time

running = False
game_height = 30
game_width = 100

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
    global game_width
    global game_height

    #"Clears" the console
    print ('\n' * 50)
    for y in range(0, game_height):
        screen_line = ''
        for x in range(0, game_width):
            #Add game border
            if y == 0 or y == game_height - 1 or x == 0 or x == game_width - 1:
                screen_line += '*'
            else:
                screen_line += ' '
            if x == game_width - 1:
                print (screen_line)

    print ("Press Escape to Quit")

#Main method
def main ():
    start()

if __name__ == "__main__":
    main()