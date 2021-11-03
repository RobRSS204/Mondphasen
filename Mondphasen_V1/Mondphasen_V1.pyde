xPos = {
        '1' : 600,
        '3' : 750,
        '5' : 900,
        '7' : 750
        }

yPos = {
        '1' : 500,
        '3' : 350,
        '5' : 500,
        '7' : 650
        }
    
def setup():
    size(1000, 1000)
    
def draw():
    background(0)
    sun()
    lunarOrbit()
    earth()
    
    if keyPressed:
        if key == '1':
            fill(255)
            circle(xPos[key], yPos[key], 30)
        elif key == '3':
            fill(255)
            arc(xPos[key], yPos[key], 30, 30, HALF_PI, PI+HALF_PI)
            fill(125, 125, 125)
            arc(xPos[key], yPos[key], 30, 30, PI+HALF_PI, TWO_PI+HALF_PI)
        elif key == '5':
            fill(125, 125, 125)
            circle(xPos[key], yPos[key], 30)
        elif key == '7':
            fill(255)
            arc(xPos[key], yPos[key], 30, 30, PI+HALF_PI, TWO_PI+HALF_PI)
            fill(125, 125, 125)
            arc(xPos[key], yPos[key], 30, 30, HALF_PI, PI+HALF_PI)

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

# Mond soll sich auf lunarOrbit bewegen und in Abhängigkeit der Position soll sich ein Bild und ein Text ändern.
