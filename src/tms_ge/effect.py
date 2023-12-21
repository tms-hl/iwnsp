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
