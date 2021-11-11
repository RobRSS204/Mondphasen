font = None
img1 = None
img2 = None
img3 = None
img4 = None

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
    global font, img1, img2, img3, img4
    size(1000, 1000)
    font = createFont("Roboto-Light.ttf", 24)
    img1 = loadImage("super_full_moon.jpeg")
    img2 = loadImage("new_moon.jpeg")
    img3 = loadImage("waning_moon.jpeg")
    img4 = loadImage("waxing_moon.jpeg")
    
def draw():
    global img
    
    background(0)
    sun()
    lunarOrbit()
    earth()
    
    if keyPressed:
        if key == '1':
            fill(255)
            circle(xPos[key], yPos[key], 30)
            
            # Beschriftung hinzufügen
            fill(255)
            textSize(24)
            text("Vollmond", 460, 510)
            
            # Vollmond Foto hinzufügen
            image(img1, 280, 180, 192, 168)
            
        elif key == '3':
            fill(255)
            arc(xPos[key], yPos[key], 30, 30, HALF_PI, PI+HALF_PI)
            fill(125, 125, 125)
            arc(xPos[key], yPos[key], 30, 30, PI+HALF_PI, TWO_PI+HALF_PI)
            
            # Beschriftung hinzufügen
            fill(255)
            textSize(24)
            text("Abnehmender Mond", 645, 320)
            
             # Abnehmender Mond Foto hinzufügen
            image(img3, 250, 170, 259, 194)
            
        elif key == '5':
            fill(125, 125, 125)
            circle(xPos[key], yPos[key], 30)
            
            # Beschriftung hinzufügen
            fill(255)
            textSize(24)
            text("Neumond", 460, 510)
            
            # Neumond Foto hinzufügen
            image(img2, 250, 150, 225, 225)
            
        elif key == '7':
            fill(255)
            arc(xPos[key], yPos[key], 30, 30, PI+HALF_PI, TWO_PI+HALF_PI)
            fill(125, 125, 125)
            arc(xPos[key], yPos[key], 30, 30, HALF_PI, PI+HALF_PI)
            
            # Beschriftung hinzufügen
            fill(255)
            textSize(24)
            text("Zunehmender Mond", 645, 700)
            
             # Zunehmender Mond Foto hinzufügen
            image(img4, 250, 150, 200, 200)

def lunarOrbit():
    stroke(255,255,255)
    fill(0)
    circle(750, 500, 300)  

def sun():
    fill(255, 255, 0)
    circle(-4890, 500, 10000) 
    
def earth():
    noStroke()
    fill(0,0,255)
    circle(750, 500, 100)

# Mond soll sich auf lunarOrbit bewegen und in Abhängigkeit der Position soll sich ein Bild und ein Text ändern.
