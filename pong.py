"""
CS 246 Python Repository
This is a basic game of Pong that plays in the console.
"""

import keyboard
import time

running = False
game_height = 30
game_width = 100

paddle_height = 3
paddle_gap = 2
player_pos = game_height / 2
computer_pos = game_height / 2

ball_x = game_width / 2.0
ball_y = game_height / 2.0
ball_vx = -1.0
ball_vy = 1.0

#Initializes game variables and conditions
def start():
    global running
    running = True
    print ('\n' * 500)
    game_loop()

#Basic game loop
def game_loop():
    global running
    while running == True:
        tick()
        time.sleep(.2)

#Updates game
def tick():
    global running
    global player_pos
    #Check for Escape key to Quit
    if keyboard.is_pressed(chr(27)):
        running = False

    #Check for W key
    if keyboard.is_pressed(chr(119)):
        player_pos -= 1.0

    #Check for S key
    if keyboard.is_pressed(chr(115)):
        player_pos += 1.0

    update_ball()
    draw()

#Draws game to console
def draw():
    global game_width
    global game_height
    global computer_pos
    global player_pos
    global paddle_height

    #"Clears" the console
    print ('\n' * 50)
    for y in range(0, game_height):
        screen_line = ''
        for x in range(0, game_width):
            #Add game border
            if y == 0 or y == game_height - 1 or x == 0 or x == game_width - 1:
                screen_line += '*'
            #Add paddles
            elif (x == paddle_gap and abs(y - int(player_pos)) < paddle_height) or (x == game_width - paddle_gap - 1 and abs(y - int(computer_pos)) < paddle_height):
                screen_line += '#'
            #Add ball
            elif (x == int(ball_x) and y == int(ball_y)):
                screen_line += 'O'
            #Fill empty space
            else:
                screen_line += ' '
            #Draw scren_line
            if x == game_width - 1:
                print (screen_line)

    print ("Press Escape to Quit")

def update_ball():
    global ball_x
    global ball_y
    global ball_vx
    global ball_vy
    global paddle_height
    global game_width
    global game_height

    ball_x += ball_vx
    ball_y += ball_vy

    if ball_y < 2 or ball_y > game_height - 3:
        ball_vy *= -1

    if ball_x < paddle_gap + 2 and abs(ball_y - player_pos) < paddle_height:
        ball_vx *= -1

    if ball_x > game_width - paddle_gap - 2 and abs(ball_y - computer_pos) < paddle_height:
        ball_vx *= -1

#Main method
def main ():
    start()

if __name__ == "__main__":
    main()