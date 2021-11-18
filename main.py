import turtle as trtl
import random as rand

#-----setup-----
apple_image = "apple.gif" # Store the file name of your shape

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image)
wn.bgpic("background.gif")

letters = ["A", "B", "C", "D", "E"]


apple_list = []
apple_letters = []

for i in range (5):
  apple_list.append(trtl.Turtle())
  apple_letters.append(rand.choice(letters))

#-----functions-----
def draw_apple(index):
  apple_list[index].penup()
  apple_list[index].shape(apple_image)
  wn.tracer(False)
  apple_list[index].setx(rand.randint(-150,150))
  apple_list[index].sety(rand.randint(-15,100))
  apple_list[index].sety(apple_list[index].ycor()-30)
  apple_list[index].color("blue")
  apple_list[index].write(apple_letters[index], align = "center", font=("Courier", 25, "bold")) 
  apple_list[index].sety(apple_list[index].ycor()+30)
  apple_list[index].showturtle()
  wn.tracer(True)
  wn.update()

def drop_apple(index):
  apple_list[index].penup()
  apple_list[index].clear()
  apple_list[index].sety(-150)
  apple_list[index].hideturtle()
 

def letterA():
  for i in range (5):
   if apple_letters[i] == "A":
    drop_apple(i)

def letterB():
  for i in range (5):
   if apple_letters[i] == "B":
    drop_apple(i)

def letterC():
  for i in range (5):
   if apple_letters[i] == "C":
    drop_apple(i)

def letterD():
  for i in range (5):
   if apple_letters[i] == "D":
    drop_apple(i)

def letterE():
  for i in range (5):
   if apple_letters[i] == "E":
    drop_apple(i)

#-----function calls-----
for i in range (5):
  draw_apple(i)

wn.onkeypress(letterA, "a")
wn.onkeypress(letterB, "b")
wn.onkeypress(letterC, "c")
wn.onkeypress(letterD, "d")
wn.onkeypress(letterE, "e")

wn.listen()
wn.mainloop()

