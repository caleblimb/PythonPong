"""
CS 246 Python Repository

This is a basic game of Pong that plays in the console.
"""

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
        if False:
            running = False

def tick():
    print("tick")

def main ():
    start()

if __name__ == "__main__":
    main()