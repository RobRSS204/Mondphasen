def setup():
    size(1000, 1000)
    background(0, 0, 0)
    
def draw():
    sun()
    lunarOrbit()
    earth()
    moon()

def lunarOrbit():
    stroke(255,255,255)
    fill(0)
    circle(750, 500, 300)  

def sun():
    fill(255, 255, 0)
    circle(-4970, 500, 10000) 
    
def earth():
    noStroke()
    fill(0,0,255)
    circle(750, 500, 100)
    
def moon():
    fill(125, 125, 125)
    circle(900, 500, 30)

# moond soll sich auf lunarOrbit bewegen und in Abhängigkeit der Position soll sich ein Bild und ein Text ändern.
