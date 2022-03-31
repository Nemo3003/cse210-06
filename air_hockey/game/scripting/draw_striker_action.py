from constants import *
from game.scripting.action import Action

"""
    This is it! you need to control what the striker is doing? well, this bad boy can do it!
"""

class DrawStrikerAction(Action):

    def __init__(self, video_service):
        self._video_service = video_service
        
    def execute(self, cast, script, callback):

        striker = cast.get_first_actor(STRIKER_GROUP)
        body = striker.get_body()

        if striker.is_debug():
            rectangle = body.get_rectangle()
            self._video_service.draw_rectangle(rectangle, PURPLE)
            
        image = striker.get_image()
        position = body.get_position()
        self._video_service.draw_image(image, position)        

class DrawStrikerAction2(Action):

    def __init__(self, video_service):
        self._video_service = video_service
        
    def execute(self, cast, script, callback):
        striker2 = cast.get_first_actor(STRIKER_GROUP2)
        body2 = striker2.get_body()

        if striker2.is_debug():
            rectangle2 = body2.get_rectangle()
            self._video_service.draw_rectangle(rectangle2, PURPLE)
            
        image = striker2.get_image()    
        position2 = body2.get_position()
        self._video_service.draw_image(image, position2)
