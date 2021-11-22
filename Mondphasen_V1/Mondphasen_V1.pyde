font = None
img1 = None
img2 = None
img3 = None
img4 = None
img5 = None
phase = 1

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
    global font, img1, img2, img3, img4, img5
    size(1000, 1000)
    font = createFont("Roboto-Light.ttf", 24)
    img1 = loadImage("super_full_moon.jpeg")
    img2 = loadImage("new_moon.jpeg")
    img3 = loadImage("waning_moon.jpeg")
    img4 = loadImage("waxing_moon.jpeg")
    img5 = loadImage("earth.png")

def draw():
    global img, phase
    
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
    text("Pfeil rechts = Vollmond" , 285, 480)
    text("Pfeil unten = Zunehmender Mond", 285, 500)
    text("Pfeil links = Neumond", 285, 520)
    text("Pfeil oben = Abnehmender Mond" , 285, 540)
    
    if keyPressed:
        if keyPressed and key == CODED:
            if phase == 1 and keyCode == RIGHT:
                moon(xPos['1'], yPos['1'])
                
                # Beschriftung hinzufügen
                fill(255)
                textSize(24)
                text("Vollmond:", 280, 750)
                textSize(15)
                text("Die der Erde zugewandte Seite des Mondes wird vollstaendig von der Sonne beleuchtet.", 290, 775)
                fill(255, 0, 0)
                text("Pfeil rechts = Vollmond" , 285, 480)
                
                # Vollmond Foto hinzufügen
                image(img1, 280, 180, 192, 168)
                
            elif phase == 1 and keyCode == UP:
                phase == 2
                moon(xPos['2'], yPos['2'])
                
                # Beschriftung hinzufügen
                fill(255)
                textSize(24)
                text("Abnehmender Mond", 280, 750)
                textSize(15)
                text("Der sichtbare Mond wird nur auf der rechten Seite der Sonne angestrahlt.", 290, 775)
                fill(255, 0, 0)
                text("Pfeil oben = Abnehmender Mond" , 285, 540)
                
                # Abnehmender Mond Foto hinzufügen
                image(img4, 250, 150, 200, 200)
            
            elif phase == 1 and keyCode == LEFT:
                phase == 3
                moon(xPos['3'], yPos['3'])
                
                # Beschriftung hinzufügen
                fill(255)
                textSize(24)
                text("Neumond", 280, 750)
                textSize(15)
                text("Von der Erde aus ist nur die Schattenseite des Mondes zu sehen.", 290, 775)
                fill(255, 0, 0)
                text("Pfeil links = Neumond" , 285, 520)
                
                # Neumond Foto hinzufügen
                image(img2, 250, 150, 225, 225)
            
            elif phase == 1  and keyCode == DOWN:
                phase == 4
                moon(xPos['4'], yPos['4'])
                
                # Beschriftung hinzufügen
                fill(255)
                textSize(24)
                text("Zunehmender Mond", 280, 750)
                textSize(15)
                text("Der sichtbare Mond wird nur auf der linken Seite der Sonne angestrahlt.", 290, 775)
                fill(255, 0, 0)
                text("Pfeil unten = Zunehmender Mond" , 285, 500)
                
                # Zunehmender Mond Foto hinzufügen
                image(img3, 250, 170, 259, 194)

def lunarOrbit():
    stroke(255,255,255)
    fill(0)
    circle(750, 500, 300)  

def sun():
    fill(255, 255, 50)
    circle(-900, 500, 2000)
    
def earth():
    image(img5, 700, 450, 100, 100)
    
def moon(x, y):
    fill(255)
    arc(x, y, 30, 30, HALF_PI, PI+HALF_PI)
    fill(125, 125, 125)
    arc(x, y, 30, 30, PI+HALF_PI, TWO_PI+HALF_PI)

# Mond soll sich auf lunarOrbit bewegen und in Abhängigkeit der Position soll sich ein Bild und ein Text ändern.
