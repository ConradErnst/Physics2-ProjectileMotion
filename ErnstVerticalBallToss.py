from vpython import *
#GlowScript 3.0 VPython
#
# ball drop with air resistance
#

#
# initialization
#

table = box(pos=vector(0,0,0), size=vector(20,0.2,20), color=color.red)
brass = ring(pos=vector(0,10,0), axis=vector(0,0,1), radius=10, thickness=0.2, color=color.yellow)
vline = box(pos=vector(10,0,0), size=vector(20,0.2,0.2), color=color.white)
vline.rotate(angle=pi/2, axis=vec(0,0,1), origin=vector(0,0,0))

ball = sphere(pos=vector(0,0,0), radius=0.5, color=color.cyan, make_trail=False) 
ball.velocity = vector(0,20,0)
 
vscale = 0.3 
varr = arrow(pos=ball.pos, axis=vscale*ball.velocity, color=color.green)

t = 0 
deltat = 0.005

g = 9.8             # acceleration due to gravity
m = 0.1             # mass of object 
c = 0.0             # coefficient of friction

#
# buttons
#

def play():
    global running
    running = True
    #print("Play")
button(text="Play", bind = play)

def pause():
    global running
    running = False
    #print("Pause")
button(text="Pause", bind = pause)

#
# displays
#

scene.append_to_caption("\n\n")
scene.append_to_caption(" time = ")
TimeReadout = wtext(text="0 s")
scene.append_to_caption("\n\n")
scene.append_to_caption(" velocity = ")
VelocityReadout = wtext(text="10 m/s")
scene.append_to_caption("\n\n")

#
# graph
#

gd = graph(width=600, height=400,
      xtitle='<i>time (s) </i>', ytitle='<i> velocity (m/s) </i>',
      foreground=color.black, background=color.white,
      xmin=0, xmax=5, ymin=-40, ymax=40)
      
f1 = gcurve(color=color.cyan)          # a graphics curve

#
# animate ball
#

scene.autoscale = False

while True: 
    
    rate(100)
    
    if running: 
        
        TimeReadout.text = "{:.3f}".format(t) + " s"
        VelocityReadout.text = "{:.3f}".format(ball.velocity.y) + " s"
        f1.plot(t,ball.velocity.y)
        
        accel = (-1.0*m*g - c*ball.velocity.y)/m
        avec  = vector(0, accel, 0) 
        
        ball.velocity = ball.velocity + avec*deltat 
        ball.pos = ball.pos + ball.velocity*deltat
    
        varr.pos = ball.pos                         # move arrow
        varr.axis = vscale*ball.velocity            # adjust arrow
        
        t = t + deltat 
        
        if ball.pos.y <= 0: 
            running = False
        
        
        
        
        
        
        
        

4