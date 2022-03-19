from constants import *
from game.scripting.action import Action


class ControlStrikerAction(Action):

    def __init__(self, keyboard_service):
        self._keyboard_service = keyboard_service
        
    def execute(self, cast, script, callback):
        striker = cast.get_first_actor(STRIKER_GROUP)
        if self._keyboard_service.is_key_down(LEFT): 
            striker.swing_left()
        elif self._keyboard_service.is_key_down(RIGHT): 
            striker.swing_right()  
        else: 
            striker.stop_moving()        