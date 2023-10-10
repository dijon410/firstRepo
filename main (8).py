import turtle as trtl

#Exploration set up ===============
ward = trtl.Turtle()
carl = trtl.Turtle()
yarl = trtl.Turtle()
#draw ground======
ward.penup()
ward.goto(-200,-30)
ward.pendown()
ward.goto(200,-30)
#================
ward.penup()
ward.goto(0,100)
ward.pendown()
carl.penup()
carl.goto(-90,80)
carl.pendown()
yarl.penup()
yarl.goto(50,50)
yarl.pendown()
wn = trtl.Screen()
#======================================

#A generic algorithm so that when you pass through a turtle it will fall to the ground and stop.
def turtleFall(myTurtle):
  myTurtle.goto(0,0)

#Function calls =======================
turtleFall(ward)
turtleFall(yarl)
turtleFall(carl)