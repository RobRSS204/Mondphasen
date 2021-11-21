font = None
img1 = None
img2 = None
img3 = None
img4 = None

xPos = {
        '1' : 900,
        '2' : 750,
        '3' : 600,
        '4' : 750
        }

yPos = {
        '1' : 500,
        '2' : 350,
        '3' : 500,
        '4' : 650
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
    
    # title
    fill(255, 255, 0)
    textSize(50)
    text("Die vier Mondphasen", 250, 70)
    
    
    # instructions
    fill(255)
    textSize(15)
    text("Halte die Tasten:", 280, 460)
    text("1 = Vollmond" , 285, 480)
    text("2 = Abnehmender Mond" , 285, 500)
    text("3 = Neumond", 285, 520)
    text("4 = Zunehmender Mond", 285, 540)
    
    if keyPressed:
        if key == '1':
            fill(255)
            arc(xPos[key], yPos[key], 30, 30, HALF_PI, PI+HALF_PI)
            fill(125, 125, 125)
            arc(xPos[key], yPos[key], 30, 30, PI+HALF_PI, TWO_PI+HALF_PI)
            
            # Beschriftung hinzufügen
            fill(255)
            textSize(24)
            text("Vollmond:", 280, 750)
            textSize(15)
            text("Der sichtbare Mond wird zur komplett von der Sonne angestrahlt.", 290, 775)
            
            # Vollmond Foto hinzufügen
            image(img1, 280, 180, 192, 168)
            
        elif key == '2':
            fill(255)
            arc(xPos[key], yPos[key], 30, 30, HALF_PI, PI+HALF_PI)
            fill(125, 125, 125)
            arc(xPos[key], yPos[key], 30, 30, PI+HALF_PI, TWO_PI+HALF_PI)
            
            # Beschriftung hinzufügen
            fill(255)
            textSize(24)
            text("Abnehmender Mond", 280, 750)
            textSize(15)
            text("Der sichtbare Mond wird nur auf der rechten Seite von der Sonne angestrahlt.", 290, 775)
            
             # Abnehmender Mond Foto hinzufügen
            image(img4, 250, 150, 200, 200)
            
        elif key == '3':
            fill(255)
            arc(xPos[key], yPos[key], 30, 30, HALF_PI, PI+HALF_PI)
            fill(125, 125, 125)
            arc(xPos[key], yPos[key], 30, 30, PI+HALF_PI, TWO_PI+HALF_PI)
            
            # Beschriftung hinzufügen
            fill(255)
            textSize(24)
            text("Neumond", 280, 750)
            textSize(15)
            text("Von der Erde aus ist nur die Schattenseite des Mondes zu sehen.", 290, 775)
            
            # Neumond Foto hinzufügen
            image(img2, 250, 150, 225, 225)
            
        elif key == '4':
            fill(255)
            arc(xPos[key], yPos[key], 30, 30, HALF_PI, PI+HALF_PI)
            fill(125, 125, 125)
            arc(xPos[key], yPos[key], 30, 30, PI+HALF_PI, TWO_PI+HALF_PI)
            
            # Beschriftung hinzufügen
            fill(255)
            textSize(24)
            text("Zunehmender Mond", 280, 750)
            textSize(15)
            text("Der sichtbare Mond wird nur auf der linken Seite von der Sonne angestrahlt.", 290, 775)
            
             # Zunehmender Mond Foto hinzufügen
            image(img3, 250, 170, 259, 194)

def lunarOrbit():
    stroke(255,255,255)
    fill(0)
    circle(750, 500, 300)  

def sun():
    fill(255, 255, 0)
    circle(-900, 500, 2000) 
    
def earth():
    noStroke()
    fill(0,0,255)
    circle(750, 500, 100)

# Mond soll sich auf lunarOrbit bewegen und in Abhängigkeit der Position soll sich ein Bild und ein Text ändern.
