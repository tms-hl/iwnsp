from enum import Enum

class EventType:
    USER = 0
    KEYDOWN = 1
    KEYUP = 2
    MOUSEMOVE = 3
    MOUSEDOWN = 4
    MOUSEUP = 5
    COLLIDE = 6

class Event:
    pass

class User(Event):
    event_type = EventType.USER

class KeyDown(Event):
    event_type = EventType.KEYDOWN
    def __init__(self, key, mod, unicode, scancode):
        '''
        '''
        self.key = key
        self.mod = mod
        self.unicode = unicode
        self.scancode = scancode

class KeyUp(Event):
    event_type = EventType.KEYUP
    def __init__(self, key, mod, unicode, scancode):
        '''
        '''
        self.key = key
        self.mod = mod
        self.unicode = unicode
        self.scancode = scancode

class MouseMove(Event):
    event_type = EventType.MOUSEMOVE
    def __init__(self, pos, rel, buttons, touch):
        '''
        '''
        self.pos = pos
        self.rel = rel
        self.buttons = buttons
        self.touch = touch

class MouseDown(Event):
    event_type = EventType.MOUSEDOWN
    def __init__(self, pos, button, touch):
        '''
        '''
        self.pos = pos
        self.button = button
        self.touch = touch

class MouseUp(Event):
    event_type = EventType.MOUSEUP
    def __init__(self, pos, button, touch):
        '''
        '''
        self.pos = pos
        self.button = button
        self.touch = touch


class Collide(Event):
    event_type = EventType.COLLIDE
    def __init__(self):
        '''
        '''
        pass
