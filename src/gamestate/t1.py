
class Gamestate:
    def __init__(self, current_level, next_level, level_changed):
        self.current_level = current_level
        self.next_level = next_level 
        self.level_changed = level_changed

level_changed = property(Gamestate)
    
current_level = 1
next_level = 1

print(current_level)

if current_level != next_level:
    level_changed = true