# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
ball_pos = [WIDTH / 2, HEIGHT / 2] # for initial state - try to remove
ball_vel = [1, -1]
# initialize ball_pos and ball_vel for new bal in middle of table
ball_pos = [WIDTH / 2, HEIGHT / 2]
paddle1_vel= 0
paddle2_vel = 0
score = [0,0]
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    if direction == RIGHT:
        ball_vel[0] = 1*(random.randrange(120, 240)/60)
        ball_vel[1] = -1*(random.randrange(60, 180)/60)
    elif direction == LEFT:
        ball_vel[0] = -1*(random.randrange(120, 240)/60)
        ball_vel[1] = -1*(random.randrange(60, 180)/60)
    
# define event handlers
def new_game():
    global ball_direction
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score
    paddle1_pos = 200
    paddle2_pos = 200
    spawn_ball(RIGHT)
    score = [0,0]
    
def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
    #added
    global paddle1_vel, paddle2_vel, score
 
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "RED")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "GREEN")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "BLUE")
      
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]   
    
    # draw ball
    canvas.draw_circle(ball_pos, 20, 2, "Red", "White") 
    # update paddle's vertical position, keep paddle on the screen
    if (paddle1_pos >= HEIGHT - PAD_HEIGHT):
        paddle1_pos =HEIGHT - PAD_HEIGHT
    elif (paddle2_pos >= HEIGHT - PAD_HEIGHT):
        paddle2_pos = HEIGHT - PAD_HEIGHT
    elif (paddle1_pos <= 0):
        paddle1_pos = 0
    elif (paddle2_pos <= 0):
        paddle2_pos = 0
           
        
    paddle1_pos += paddle1_vel;
    paddle2_pos += paddle2_vel;

    
    # draw paddles
    canvas.draw_line([PAD_WIDTH, (paddle1_pos)],[PAD_WIDTH, PAD_HEIGHT+(paddle1_pos)], 10, "RED")
    canvas.draw_line([WIDTH - PAD_WIDTH, (paddle2_pos)],[WIDTH - PAD_WIDTH, PAD_HEIGHT+(paddle2_pos)], 10, "YELLOW")
    
    
    # determine whether paddle and ball collide
    if (ball_pos[1]-BALL_RADIUS >= paddle1_pos and ball_pos[1]+BALL_RADIUS <=paddle1_pos+PAD_HEIGHT and ball_pos[0]-BALL_RADIUS == PAD_WIDTH):
        ball_vel[0] = - ball_vel[0]
    elif (ball_pos[1]+BALL_RADIUS >= paddle2_pos and ball_pos[1]-BALL_RADIUS <=paddle2_pos+PAD_HEIGHT and ball_pos[0]+BALL_RADIUS == WIDTH-PAD_WIDTH):
        ball_vel[0] = - ball_vel[0]
    elif ball_pos[0] >= WIDTH-BALL_RADIUS-PAD_WIDTH:
        spawn_ball(LEFT)
        score[0] +=1
    elif ball_pos[0] <= BALL_RADIUS+PAD_WIDTH:
        spawn_ball(RIGHT)
        score[1] +=1
    # draw scores
    canvas.draw_text(str(score[0]), [50,50],60,"Red")
    canvas.draw_text(str(score[1]), [520,50],60,"Yellow")
    # Wall collision
    wallCollision()

# TODO: continually update until keyup event
def keydown(key):
    
    global paddle1_vel, paddle2_vel
    #print('keydown ' + chr(key))
    if key == simplegui.KEY_MAP["s"]:
        paddle1_vel +=3
    if key == simplegui.KEY_MAP["w"]:
        #print (chr(key))
        paddle1_vel -=3
    elif (chr(key) == '('):
        paddle2_vel +=3
    elif (chr(key) =='&'):
        paddle2_vel -=3
        
def keyup(key):
    global paddle1_vel, paddle2_vel
    #print ('keyup ' + chr(key))
    paddle1_vel = 0
    paddle2_vel = 0
    
def wallCollision():
    # Ball collision with side of walls
    # 0 = x, 1 = y where y is the vertical component and x is the horizontal component
    if ball_pos[1] <= BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
    elif ball_pos[1] >= HEIGHT-BALL_RADIUS:
        ball_vel[1] = -ball_vel[1]
# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Reset", new_game, 200)

# start frame
new_game()
frame.start()

