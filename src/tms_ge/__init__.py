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
    
    def __init__(self):
        self.bind(EventType.CLICK, self.on_click)
    
    def on_click(self, event):
        pass
    
    @property
    def area_changed(self):
        '''
            Gib eine Liste mit Rechtecken zurück. In diesen Bereichen des Fensters wurden im letzten tick Änderungen ausgeführt
        '''
        pass
    
class Sprite:
    
    def __init__(self, surface):
        # TODO: Attribute
        # x: int
        # y: int
        # z: int
        # w: int
        # h: int
        # costumes
        # costume_index
        # effects
        # _surface
        # old_position
        # new_position
        # changed
    
    @property
    def rect(self):
        pass
    
    @property
    def costume(self):
        '''
            gibt das aktuelle Kostüm zurück
        '''
        
    def tick(self, events):
        '''
            Führt einen Schritt der Spielschleife aus
        '''
    
    def draw(self):
        '''
            Zeichnet das Sprite auf die Oberfläche
        '''
        
    def add_costume(self, costume):
        '''
            Fügt ein Kostüm hinzu
        '''
        pass
    
    def add_effect(self, name, effeeinen Schritt der Spielschleife aus
        '''
        passct):
        '''
            Fügt einen Effekt hinzu
        '''

class Costume(self):
    def draw(self):
        pass
    
class Effect:
    def __init__(self):
        # TODO:
        # Attribute
        # repeat: bool
        # active: bool    
        pass
    
    def tick(self, sprite):
        '''
            Führt auf sprite den nächsten Schritt des Effekts aus
        '''
        
    def start(self):
        '''
            Startet den Effekt
        '''
    
    def stop(self):
        '''
            Stoppt den Effekt. Dabei wir er auf den Startzustand zurückgesetzt
        '''
        
    def pause(self):
        '''
            Pausiert den Effekt. Der aktuelle Zustand bleibt erhalten
        '''