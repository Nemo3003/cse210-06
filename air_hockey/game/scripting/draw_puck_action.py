from constants import *
from game.scripting.action import Action
from game.casting.image import Image
from game.casting.point import Point

"""
    Let us draw the puck's action! 
"""

class DrawPuckAction(Action):

    def __init__(self, video_service):
        self._video_service = video_service
        
    def execute(self, cast, script, callback):
        puck = cast.get_first_actor(PUCK_GROUP)
        body = puck.get_body()

        if puck.is_debug():
            rectangle = body.get_rectangle()
            self._video_service.draw_rectangle(rectangle, PURPLE)
            
        image = puck.get_image()
        position = body.get_position()
        self._video_service.draw_image(image, position)
        # for testing
        # self._video_service.draw_image(Image("air_hockey/assets/images/one.png"), Point(10,350))

