"""
CS 246 Python Repository
This is a basic game of Pong that plays in the console.
"""

import keyboard
import random
import time

running = False
game_height = 25
game_width = 50

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
ball_vx = random.uniform(0.8, 1.0)
ball_vy = 1.0

ball_size = 2

#scoreboard
player_score = 4
computer_score = 2

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
        time.sleep(.1)

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
    global ball_size

    #"Clears" the console
    frame = ''
    frame += ('\n' * 5)

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
            elif (abs(x - ball_x) < ball_size and abs(y - int(ball_y)) < ball_size):
                screen_line += 'O'
            #Fill empty space
            else:
                screen_line += ' '
            #Draw scren_line
            if x == game_width - 1:
                frame += (screen_line + '\n')

    frame += ("Score: " + str(player_score) + " | " + str(computer_score)) + '\n'
    frame +=  ("W and S to move") + '\n'
    frame += ("Press Escape to Quit") + '\n'
    print (frame)

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
    global ball_size

    #update ball position
    ball_x += ball_vx
    ball_y += ball_vy

    #Check if ball collides with top or bottom
    if ball_y < ball_size + 1 or ball_y > game_height - 1 - ball_size:
        ball_vy *= -1

    #Check if ball collides with the players paddle
    if ball_x < paddle_gap + 2 and ball_x > paddle_gap + 1 and abs(ball_y - player_pos) < paddle_height + ball_size:
        ball_vx *= -1

    #Check if ball collides with the computers paddle
    if ball_x > game_width - paddle_gap - 1 - ball_size and ball_x < game_width - paddle_gap - ball_size and abs(ball_y - computer_pos) < paddle_height + ball_size:
        ball_vx *= -1

    #Check if ball is out of bounds
    if ball_x < 0 - ball_size:
        ball_x = game_width / 2
        ball_vx = random.uniform(0.8, 1.0)
        computer_score += 1
    if ball_x > game_width + ball_size:
        ball_x = game_width / 2
        ball_vx = random.uniform(-1.0, -0.8)
        player_score += 1

def update_computer():
    global ball_y
    global ball_x
    global ball_vx
    global computer_pos

    if ball_vx > 0 and ball_x > game_width / 1.5:
        if ball_y < computer_pos:
           computer_pos -= 0.5

        if ball_y > computer_pos:
           computer_pos += 0.5

#Main method
def main ():
    start()

if __name__ == "__main__":
    main()