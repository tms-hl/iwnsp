'''
    Engine für Spiele auf der Basis von pygame
'''

class Game:
    def __init__(self):
        self.window = pygame.diplay((500, 500))
        self.levels = {}
        self.gamestate = Gamestate()
        
    def add_level(self, name, level):
        self.levels[name] = level
    
    def run(self, first_level):
        self.gamestate.current_level = first_level
        while not done:
            if self.gamestate.current_level != self.gamestate.next_level:
                if self.gamestate.next_level == None:
                    done = True
                else:
                    self.gamestate.current_level = self.gamestate.next_level
            self.levels[self.gamestate.current_level].process_events()
            self.levels[self.gamestate.current_level].draw(self.window)
            self.window.update(self.levels[self.gamestate.current_level].area_changed)
        
class Gamestate:

    def __init__(self):
        # Attribute
        # current_level: string Name des gerade aktiven Levels
        # next_level: string Name des Levels, das beim nächsten Tick gestartet werden soll
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

    def __init__(self, surface, gamestate):
        '''
            Erstellt ein neues Level

            Parameters:
            surface: pyfoot Surface, das Spielefenster
            gamestate: globaler Zustand des Spiels
        '''
        pass

    def process_events(self, events):
        '''
            Verarbeitet pygame-Ereignisse
        '''
        # TODO: Ereignisse in tms_ge-Ereignisse umwandeln
        # TODO: gebundene Methoden aufrufen
        # TODO: process_events für alle Sprites aufrufen
        pass
        
    def run(self):
        '''
            Initialisiert das Level.

            Wird von Unterklassen überschrieben. Hier werden Sprites erstellt und Ereignisse verbunden.
        '''
        pass

    def draw(self):
        '''
            Zeichnet das Level auf das Fenster
        '''
        pass
        
    @property
    def area_changed(self):
        '''
            Gib eine Liste mit Rechtecken zurück. In diesen Bereichen des Fensters wurden im letzten tick Änderungen ausgeführt
        '''
        pass
    
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
        # old_position
        # new_position
        # changed
        pass

    @property
    def pos(self):
        pass

    @pos.setter
    def pos(self, value):
        pass
        
    @property
    def rect(self):
        pass
    
    @property
    def costume(self):
        '''
            gibt das aktuelle Kostüm zurück
        '''
        pass

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
