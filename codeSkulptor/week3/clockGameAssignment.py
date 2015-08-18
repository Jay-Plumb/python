# template for "Stopwatch: The Game"
import simplegui
import math
# define global variables
interval = 100
integer = 0
width = 500
height = 500
position = [width/2-60, height/2-40]
hitMiss = [0,0]
hitMissPosition = [width-40, 25]
D = 0
running = False
# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    global D
    A = t/600
    B = (t%600)/10
    D = t%10
    if(B < 10):
        B = '0'+str(B)
        
    return str(A) + ':' + str(B)  + ':'+ str(D)
   
# define event handlers for buttons; "Start", "Stop", "Reset"
def start_handler():
   global running
   timer.start() 
   running = True
   hitMiss[1] +=1
    
def stop_handler():
    global running
    if(running):
        stop_whole_number()   
    running = False
    timer.stop()
        
def reset_handler():
    global integer
    timer.stop()
    integer = 0
    hitMiss[0] = 0
    hitMiss[1] = 0
    
# define event handler for timer with 0.1 sec interval
def increment():
    global integer
    integer+=1


def result():
    global hitMiss
    return str(hitMiss[0]) + '/' + str(hitMiss[1])

def stop_whole_number():
    if (str(D) == '0'):
        hitMiss[0]+=1   
    return hitMiss[0]

# define draw handler
def draw_time(canvas):
    global integer
    canvas.draw_text(format(integer), position,60,"Red")
    canvas.draw_text(result(), hitMissPosition,20,"Blue")
    
# create frame
frame = simplegui.create_frame("Stopwatch", width, height)
frame.set_draw_handler(draw_time)
frame.add_button("Start", start_handler, 100)
frame.add_button("Stop", stop_handler, 100)
frame.add_button("Reset", reset_handler, 100)
# register event handlers
timer = simplegui.create_timer(interval, increment)

# start frame
frame.start()


# Please remember to review the grading rubric

