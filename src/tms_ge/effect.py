class Effect:
    def __init__(self, sprite):
        # TODO:
        # Attribute
        # repeat: bool
        # active: bool
        # sprite: Figur, für die der Effekt gilt
        pass
            
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

    def tick(self):
        '''
            führt den nächsten Schritt des Effekts aus
        '''
        pass
        
class EffectAnimation:
    '''
        Eine Animation wechselt automatisch die Kostüme des Sprites
    '''
    pass