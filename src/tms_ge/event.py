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

class EventUser(Event):
    event_type = EventType.USER

class EventKeyDown(Event):
    def __init__(self, key, mod, unicode, scancode):
        '''
        '''
        #TODO: Attribute setzen