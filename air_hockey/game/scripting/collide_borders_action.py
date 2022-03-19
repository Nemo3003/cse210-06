from constants import *
from game.casting.sound import Sound
from game.scripting.action import Action


class CollideBordersAction(Action):

    def __init__(self, physics_service, audio_service):
        self._physics_service = physics_service
        self._audio_service = audio_service    
        
    def execute(self, cast, script, callback):
        puck = cast.get_first_actor(PUCK_GROUP)
        body = puck.get_body()
        position = body.get_position()
        x = position.get_x()
        y = position.get_y()
        slide_hit = Sound(SLIDE_HIT)
        goal = Sound(GOAL)
                
        if x < FIELD_LEFT:
            puck.bounce_x()
            self._audio_service.play_sound(slide_hit)

        elif x >= (FIELD_RIGHT - PUCK_WIDTH):
            puck.bounce_x()
            self._audio_service.play_sound(slide_hit)

        if y < FIELD_TOP:
            puck.bounce_y()
            self._audio_service.play_sound(slide_hit)

        elif y >= (FIELD_BOTTOM - PUCK_WIDTH):
            callback.on_next(GAME_OVER)
            self._audio_service.play_sound(goal)