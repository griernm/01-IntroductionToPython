"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Aaron Wilkin, their colleagues, and Nathalie Grier.
"""
########################################################################
# DONE: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# DONE: 2.
#   You should have RUN the  m5e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
#
########################################################################
import rosegraphics as rg
window = rg.TurtleWindow()

lilo = rg.SimpleTurtle('turtle')
lilo.pen = rg.Pen('red', 10)
lilo.speed = 80

stitch = rg.SimpleTurtle('turtle')
stitch.pen = rg.Pen('blue', 10)
stitch.speed = 80

size = 200

for k in range(10):
    lilo.draw_regular_polygon(6,size)

    lilo.pen_up()
    lilo.right(5)
    lilo.forward(30)
    lilo.left(6)

    lilo.pen_down()

    size = size - 40



size = 150

for k in range(10):
    stitch.draw_regular_polygon(7, size)

    stitch.pen_up()
    stitch.left(4)
    stitch.backward(20)
    stitch.right(5)

    stitch.pen_down()

    size = size - 30

window.close_on_mouse_click()