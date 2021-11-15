#   a123_apple_1.py
import turtle as trtl

#-----setup-----
apple_image = "apple.gif" # Store the file name of your shape

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image) # Make the screen aware of the new file
wn.bgpic("background.gif")
apple = trtl.Turtle()
drawer = trtl.Turtle()
#-----functions-----
# given a turtle, set that turtle to be shaped by the image file
def draw_apple(active_apple):
  active_apple.shape(apple_image)
  wn.update()
def drop_apple():
  apple.penup()
  drawer.clear()
  drawer.hideturtle()
  apple.goto(0,-130)
  
def draw_an_A():
  drawer.goto(-10,-30)
  drawer.color("white")
  drawer.write("A", font=("Arial", 30, "bold"))
  

#-----function calls-----
draw_apple(apple)
draw_an_A()
wn.onkeypress(drop_apple, "a")
wn.listen()
wn.mainloop()
    

