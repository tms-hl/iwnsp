'''
    Engine für Spiele auf der Basis von pygame
'''

class Game:
    '''
        Zentrale Steuerung des Spiels
    '''
    
    def __init__(self, width, height):
        '''
            Parameters:
            width (int): Breite des Spielfensters
            height (int): Höhe des Spielfensters
        '''
        
        # TODO: pygame initialisieren
        # TODO: Attribut "window" als Fenster-Surface definieren
        # TODO: Attribut "levels" ist ein Dictionary mit Levels
        
    def add_level(self, name, level):
        '''
            Fügt dem Spiel ein Level hinzu
            
            Parameters:
            name (str): Name des Levels
            level (Level): Level-Objekt
        '''
        
    def run(self, first_level):
        '''
            Startet das Spiel
            
            Parameters:
            first_level (str): Name des ersten Levels
        '''
        # TODO: Spielschleife starten
        # TODO:
        
class Gamestate:
    pass

class Level:
    
    def tick(self, events):
        '''
            Führt einen Schritt der Spielschleife aus
        '''
        pass
    
    @property
    def area_changed(self):
        '''
            Gib eine Liste mit Rechtecken zurück. In diesen Bereichen des Fensters wurden im letzten tick Änderungen ausgeführt
        '''
        pass
    
class Sprite:
    
    def tick(self, events):
        '''
            Führt einen Schritt der Spielschleife aus
        '''
        
    