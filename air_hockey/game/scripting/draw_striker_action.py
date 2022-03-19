from constants import *
from game.scripting.action import Action


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