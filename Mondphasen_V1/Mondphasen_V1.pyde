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
#Textpositionen
x1 = 280
x2 = x1 + 5
x3 = x1 + 10
y1 = 460
y2 = y1 + 20
y3 = y1 + 40
y4 = y1 + 60
y5 = y1 + 80
y6 = 775

#Position Erde und abhängige Objekte
xe = 750
ye = 500

#Position und grösse der Bilder
xi = x1
yi = 150
b = 210

    
def setup():
    global font, img1, img2, img3, img4, img5
    size(1000, 1000)
    font = createFont("Roboto-Light.ttf", 24)
    img1 = loadImage("full_moon.jpeg")
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
    text("Halte die Tasten:", x1, y1)
    text("Pfeil rechts = Vollmond" , x2, y2)
    text("Pfeil unten = Zunehmender Mond", x2, y3)
    text("Pfeil links = Neumond", x2, y4)
    text("Pfeil oben = Abnehmender Mond" , x2, y5)
    
    if keyPressed:
        if keyPressed and key == CODED:
            if phase == 1 and keyCode == RIGHT:
                moon(xPos['1'], yPos['1'])
                
                # Beschriftung hinzufügen
                fill(255)
                textSize(24)
                text("Vollmond:", x1, y6 - 25)
                textSize(15)
                text("Die der Erde zugewandte Seite des Mondes wird vollstaendig von der Sonne beleuchtet.", x3, y6)
                fill(255, 0, 0)
                text("Pfeil rechts = Vollmond" , x2, y2)
                
                # Vollmond Foto hinzufügen
                image(img1, xi, yi, b, b)
                
            elif phase == 1 and keyCode == UP:
                phase == 2
                moon(xPos['2'], yPos['2'])
                
                # Beschriftung hinzufügen
                fill(255)
                textSize(24)
                text("Abnehmender Mond", x1, y6 - 25)
                textSize(15)
                text("Der sichtbare Mond wird nur auf der rechten Seite der Sonne angestrahlt.", x3, y6)
                fill(255, 0, 0)
                text("Pfeil oben = Abnehmender Mond" , x2, y5)
                
                # Abnehmender Mond Foto hinzufügen
                image(img4, xi, yi, b, b)
            
            elif phase == 1 and keyCode == LEFT:
                phase == 3
                moon(xPos['3'], yPos['3'])
                
                # Beschriftung hinzufügen
                fill(255)
                textSize(24)
                text("Neumond", x1, y6 - 25)
                textSize(15)
                text("Von der Erde aus ist nur die Schattenseite des Mondes zu sehen.", x3, y6)
                fill(255, 0, 0)
                text("Pfeil links = Neumond" , x2, y4)
                
                # Neumond Foto hinzufügen
                image(img2, xi, yi, b, b)
            
            elif phase == 1  and keyCode == DOWN:
                phase == 4
                moon(xPos['4'], yPos['4'])
                
                # Beschriftung hinzufügen
                fill(255)
                textSize(24)
                text("Zunehmender Mond", x1, y6 - 25)
                textSize(15)
                text("Der sichtbare Mond wird nur auf der linken Seite der Sonne angestrahlt.", x3, y6)
                fill(255, 0, 0)
                text("Pfeil unten = Zunehmender Mond" , x2, y3)
                
                # Zunehmender Mond Foto hinzufügen
                image(img3, xi, yi, b, b)

def lunarOrbit():
    stroke(255,255,255)
    fill(0)
    circle(xe, ye, 300)  

def sun():
    fill(255, 255, 50)
    circle(-900, ye, 2000)
    
def earth():
    image(img5, xe - 50, ye - 50, 100, 100)
    
def moon(x, y):
    fill(255)
    arc(x, y, 30, 30, HALF_PI, PI+HALF_PI)
    fill(125, 125, 125)
    arc(x, y, 30, 30, PI+HALF_PI, TWO_PI+HALF_PI)

# Mond soll sich auf lunarOrbit bewegen und in Abhängigkeit der Position soll sich ein Bild und ein Text ändern.
