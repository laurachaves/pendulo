teta = PI/3
R = 200 #comprimento
g = 980.0 #aceleração da gravidade
vt = 0.01
h = R-R*cos(teta)
EM = g*h+(vt**2)/2
oldt = millis()/1000.0
ver = 1.0


def setup():
  size(800,800)
  


def draw():
    global oldt, teta, R, vt, g, h, EM, ver
    t = millis()/1000.00
    dt = t - oldt
    oldt = t
    
    
    omega = ver*vt/R
    teta -= omega*(dt)
    x = R*sin(teta)
    y = R-R*cos(teta)
    #print("2",EM-g*y)
    if EM < g*y:
        ver *= -1
    else:
        vt = (2*(EM-g*y))**0.5
    
    background(255)
    stroke(0)
    posx = 400+x
    posy = R-y
    line(400,0,posx, posy)
    fill(0)
    ellipse(posx,posy,20, 20)
