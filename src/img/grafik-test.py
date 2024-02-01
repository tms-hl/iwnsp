import pygame			# importiert das Pygame-Modul, muss immer am Anfang stehen

# EINSTELLUNGEN

BREITE = 80
HOEHE = 100
ZEILE = 1
ANZAHL = 6
GESCHWINDIGKEIT = 10
DATEI = "hero_spritesheet.png"

# ENDE DER EINSTELLUNGEN

RAND = 100

# Konstanten
SCHWARZ = (0,0,0)		# Farbwerte im RGB-Format: https://www.w3schools.com/colors/colors_picker.asp

pygame.init()
fenster = pygame.display.set_mode((BREITE+RAND, HOEHE+RAND))	# erzeugt ein Fenster in den Dimensionen 800x600 Pixel
clock = pygame.time.Clock()

try:
    sheet = pygame.image.load(DATEI).convert()
except pygame.error as e:
    print(f"Datei kann nicht geladen werden: {DATEI}")
    raise SystemExit(e)

# Hauptschleife: wird wiederholt, solange das Spiel läuft
i = 0
spiel_aktiv = True
while spiel_aktiv:
    clock.tick(GESCHWINDIGKEIT)
    # Ereignisschleife, hier wird auf Benutzereingaben reagiert
    # Liste der wichtigsten Ereignisse:
    # https://www.geeksforgeeks.org/pygame-event-handling/
    for event in pygame.event.get():
        if event.type == pygame.QUIT:		# jedes Ereignis, das verarbeitet werden soll, muss in dieser Art abgefragt werden
            print("Quit")
            spiel_aktiv = False
            
    fenster.fill(SCHWARZ)					# Hintergrundfarbe einstellen
    
    i = (i + 1) % ANZAHL
    image = pygame.Surface((BREITE,HOEHE)).convert()
    fenster.blit(sheet, (RAND/2,RAND/2), pygame.Rect(i*BREITE, ZEILE*HOEHE, BREITE, HOEHE))
    
    pygame.display.flip()					# schreibt die Anzeige auf das Fenster, sollte am Ende der Hauptschleife stehen

pygame.quit()		# beendet das Spiel, muss immer am Ende des Programms stehen