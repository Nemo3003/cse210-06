from constants import *
from game.scripting.action import Action

"""
    The striker must be controlled! so this is why this module exists :)
"""

class ControlStrikerAction(Action):

    def __init__(self, keyboard_service):
        self._keyboard_service = keyboard_service
        
    def execute(self, cast, script, callback):

        striker = cast.get_first_actor(STRIKER_GROUP)
        if self._keyboard_service.is_key_down(D) & self._keyboard_service.is_key_down(W): 
            striker.swing_upright()
        elif self._keyboard_service.is_key_down(A) & self._keyboard_service.is_key_down(W): 
            striker.swing_upleft()
        elif self._keyboard_service.is_key_down(D) & self._keyboard_service.is_key_down(S): 
            striker.swing_downright()
        elif self._keyboard_service.is_key_down(A) & self._keyboard_service.is_key_down(S): 
            striker.swing_downleft()
        elif self._keyboard_service.is_key_down(A): 
            striker.swing_left()
        elif self._keyboard_service.is_key_down(D): 
            striker.swing_right()
        elif self._keyboard_service.is_key_down(W): 
            striker.swing_up()  
        elif self._keyboard_service.is_key_down(S): 
            striker.swing_down()  
        else: 
            striker.stop_moving()   

class ControlStrikerAction2(Action):

    def __init__(self, keyboard_service):
        self._keyboard_service = keyboard_service
        
    def execute(self, cast, script, callback):

        striker2 = cast.get_first_actor(STRIKER_GROUP2)
        if self._keyboard_service.is_key_down(RIGHT) & self._keyboard_service.is_key_down(UP): 
            striker2.swing_upright()
        elif self._keyboard_service.is_key_down(LEFT) & self._keyboard_service.is_key_down(UP): 
            striker2.swing_upleft()
        elif self._keyboard_service.is_key_down(RIGHT) & self._keyboard_service.is_key_down(DOWN): 
            striker2.swing_downright()
        elif self._keyboard_service.is_key_down(LEFT) & self._keyboard_service.is_key_down(DOWN): 
            striker2.swing_downleft()
        elif self._keyboard_service.is_key_down(LEFT): 
            striker2.swing_left()
        elif self._keyboard_service.is_key_down(RIGHT): 
            striker2.swing_right()
        elif self._keyboard_service.is_key_down(UP): 
            striker2.swing_up()  
        elif self._keyboard_service.is_key_down(DOWN): 
            striker2.swing_down()  
        else: 
            striker2.stop_moving()



             
