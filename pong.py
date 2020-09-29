"""
CS 246 Python Repository
This is a basic game of Pong that plays in the console.
"""

import keyboard
import random
import time

running = False
game_height = 30
game_width = 100

#size of paddles
paddle_height = 3

#distance of paddles from side
paddle_gap = 2

#position of paddles
player_pos = game_height / 2
computer_pos = game_height / 2

#ball position
ball_x = game_width / 2.0
ball_y = game_height / 2.0

#ball velocity
ball_vx = random.uniform(0.5, 1.0)
ball_vy = 0.5

#scoreboard
player_score = 0
computer_score = 0

#Initializes game variables and conditions
def start():
    global running
    running = True
    #"Clear" console
    print ('\n' * 500)
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

    update_computer()
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
    print ('\n' * 10)
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

    print ("Score: " + str(player_score) + " | " + str(computer_score))
    print ("W and S to move")
    print ("Press Escape to Quit")

def update_ball():
    global ball_x
    global ball_y
    global ball_vx
    global ball_vy
    global paddle_height
    global game_width
    global game_height
    global player_score
    global computer_score

    #update ball position
    ball_x += ball_vx
    ball_y += ball_vy

    #Check if ball collides with top or bottom
    if ball_y < 2 or ball_y > game_height - 3:
        ball_vy *= -1

    #Check if ball collides with the players paddle
    if ball_x < paddle_gap + 2 and ball_x > 2 and abs(ball_y - player_pos) < paddle_height:
        ball_vx *= -1

    #Check if ball collides with the computers paddle
    if ball_x > game_width - paddle_gap - 2 and ball_x < game_width - 2 and abs(ball_y - computer_pos) < paddle_height:
        ball_vx *= -1

    #Check if ball is out of bounds
    if ball_x < 0:
        ball_x = game_width / 2
        computer_score += 1

    if ball_x > game_width:
        ball_x = game_width / 2
        player_score += 1

def update_computer():
    global ball_y
    global ball_x
    global ball_vx
    global computer_pos

    if ball_vx > 0 and ball_x > game_width / 2:
        if ball_y < computer_pos:
           computer_pos -= 1.0

        if ball_y > computer_pos:
           computer_pos += 1.0

#Main method
def main ():
    start()

if __name__ == "__main__":
    main()