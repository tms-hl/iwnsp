import event
from collections import namedtuple

'''
    Engine für Spiele auf der Basis von pygame
'''

class Game:
    '''
        Zentrale Steuerung des Spiels
    '''

    def __init__(self, width, height, gamestate):
        '''
            Parameters:
            width (int): Breite des Spielfensters
            height (int): Höhe des Spielfensters
            gamestate (Gamestate): Globaler Zustand des Spiels
        '''
        pygame.init()
        self.width = width
        self.height = height
        self.window = pygame.diplay((self.width, self.height))
        self.levels = {}
        self.gamestate = gamestate
        
    def add_level(self, name, level):
        '''
            Fügt dem Spiel ein Level hinzu
            
            Parameters:
            name (str): Name des Levels
            level (Level): Level-Objekt
        '''
        self.levels[name] = level
    
    def run(self, first_level):
        '''
            Startet das Spiel
            
            Parameters:
            first_level (str): Name des ersten Levels
        '''
        self.gamestate.current_level = first_level

        while not done:     # Starte Hauptschleife
            if self.gamestate.current_level != self.gamestate.next_level:   # Wenn next_level ist nicht mehr aktuelles Level ist:
                if self.gamestate.next_level == None:   # Hauptschleife beenden, wenn next_level ist None
                    done = True
                else:
                    self.gamestate.current_level = self.gamestate.next_level    # Sonst, aktuelles Level auf next_level setzen
                    self.levels[self.gamestate.current_level].run()
                    
            self.levels[self.gamestate.current_level].process_events()  # Events in aktuellem Level verarbeiten
            self.levels[self.gamestate.current_level].draw(self.window)     # Aktuelles Level auf Bildschirm malen
            self.window.update(self.levels[self.gamestate.current_level].area_changed)
        
class Gamestate:
    pass

class EventTrigger:
    def bind(self, event_type, function):
        '''
            Bindet eine Funktion an ein Ereignis

            Parameters:
            event_type (EventType): Typ des Events
            function (callable): Funktion, die bei dem Ereignis aufgerufen wird. Argument: Objekt des Typs Event
        '''
        pass

    def trigger(self, event):
        '''
            Löst ein Ereignis aus.

            Alle gebundenen Funktionen für diesen EventType werden ausgeführt
        '''
        pass

    def bound(self, event_type):
        '''
            Gibt zurück, ob ein bestimmter Ereignistyp gebunden wurde

            Parameters:
            event_type (EventType): Typ des gesuchten Events

            Returns:
            boolean: WAHR, wenn das Ereignis gebunden wurde
        '''
        pass

class Level(EventTrigger):

    def __init__(self, gamestate):
        '''
            Erstellt ein neues Level

            Parameters:
            gamestate: globaler Zustand des Spiels
        '''
        self.gamestate = gamestate

    def process_events(self):
        '''
            Verarbeitet pygame-Ereignisse
        '''
        # TODO: Ereignisse in tms_ge-Ereignisse umwandeln
        # TODO: gebundene Methoden aufrufen
        # TODO: process_events für alle Sprites aufrufen
        new_events = []
        for event in events:
            if event.type == pygame.KEYDOWN:
                new_events.append(event.KeyDown(event.key, event.mod, event.unicode, event.scancode))
            elif event.type == pygame.KEYUP:
                new_events.append(event.KeyUp(event.key, event.mod, event.unicode, event.scancode))
            elif event.type == pygame.MOUSEMOTION:
                new_events.append(event.MouseMove(event.pos, event.rel, event.buttons, event.touch))
            elif event.type == pygame.MOUSEDOWN:
                new_events.append(event.MouseDown(event.pos, event.button, event.touch))
            elif event.type == pygame.MOUSEUP:
                new_events.append(event.MouseUp(event.pos, event.button, event.touch))

        for sprite in self._sprites:
            sprite.process_events(new_events)

    def add_sprite(sprite):
        '''
        Gegebene Sprite zu Level hinzufügen
        '''
        self._sprites.append(sprite)

    def run(self):
        '''
            Initialisiert das Level.

            Wird von Unterklassen überschrieben. Hier werden Sprites erstellt und Ereignisse verbunden.
        '''
        pass

    def draw(self, surface):
        '''
            Zeichnet das Level auf das Fenster
        '''
        for sprite in self._sprites:
            surface.blit(sprite.draw(), (sprite.x, sprite.y))


    @property
    def area_changed(self):
        '''d
            Gib eine Liste mit Rechtecken zurück. In iesen Bereichen des Fensters wurden im letzten tick Änderungen ausgeführt
        '''
        rects = []
        for sprite in self._sprites:
            if sprite.changed:
                rects.append(sprite.rect)
                rects.append(sprite.old_state.rect)
        return rects

State = namedtuple("State", ["rect", "z", "costume_index"])
class Sprite(EventTrigger):
    
    def __init__(self):
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
        # old_state
        # changed
        self.old_state = None
        pass

    @property
    def pos(self):
        pass

    @pos.setter
    def pos(self, value):
        pass
        
    @property
    def rect(self):
        return pygame.Rect([self.x, self.y, self.w, self.h])
    
    @property
    def costume(self):
        '''
            gibt das aktuelle Kostüm zurück
        '''

    @property
    def current_state(self):
        return State(self.rect, self.z, self.costume_index)

    @property
    def changed(self):
        return self.old_state != self.current_state
    
    def draw(self):
        '''
            Zeichnet das aktuelle Kostüm

            Gibt ein pygame-Surface mit der Figur zurück
        '''
        pass
        
    def process_events(self, events):
        '''
            Verarbeitet pygame-Ereignisse
        '''
        pass
        
    def add_costume(self, costume):
        '''
            Fügt ein Kostüm hinzu
        '''
        pass
    
    def add_effect(self, name, effect):
        '''
            Fügt einen Effekt hinzu
        '''
        pass
    
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
        pass
    
    def start(self):
        '''
            Startet den Effekt
        '''
        pass
    
    def stop(self):
        '''
            Stoppt den Effekt. Dabei wir er auf den Startzustand zurückgesetzt
        '''
        pass
    
    def pause(self):
        '''
            Pausiert den Effekt. Der aktuelle Zustand bleibt erhalten
        '''
        pass