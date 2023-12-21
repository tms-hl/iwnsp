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