
class Gamestate:
    def __init__(self, current_level, next_level):
        self.current_level = current_level
        self.next_level = next_level 
    
current_level = 1
next_level = 1

def lc(self):
    if current_level != next_level:
        level_changed = True
    else:
        level_changed = False

level_changed = property(lc)