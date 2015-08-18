# CodeSkulptor runs Python programs in your browser.
# Click the upper left button to run this simple demo.

# CodeSkulptor runs in Chrome 18+, Firefox 11+, and Safari 6+.
# Some features may work in other browsers, but do not expect
# full functionality.  It does NOT run in Internet Explorer.

import simplegui
# (1) Globals
message = "Welcome!"
# (2) Helper functions

# Handler for mouse click
def click():
    global message
    message = "Good job!"
# (3) Classes
# (4) Define event handlers
# Handler to draw on canvas
def draw(canvas):
    canvas.draw_text(message, [50,112], 36, "Red")

# (5) Create a frame
frame = simplegui.create_frame("Home", 300, 200)
# (6) Assign callbacks to event handlers
frame.add_button("Click me", click)
frame.set_draw_handler(draw)

# (7) Start the frame animation and timers
frame.start()

