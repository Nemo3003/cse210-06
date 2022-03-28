from constants import *
from game.casting.sound import Sound
from game.scripting.action import Action
"""
This module handles the events in which the puck hits the borders
"""

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
        #TODO: Check if puck is in the border
        if puck == SCREEN_HEIGHT:
            self._audio_service.play_sound(slide_hit)
            body.set_position(x, FIELD_TOP)
            body.set_velocity(0, 0)

        if puck == SCREEN_WIDTH:
            self._audio_service.play_sound(slide_hit)
            body.set_position(FIELD_RIGHT, y)
            body.set_velocity(0, 0)


        if x < FIELD_LEFT:
            puck.bounce_x()
            self._audio_service.play_sound(slide_hit)

        if x >= (FIELD_RIGHT - PUCK_WIDTH):
            puck.bounce_x()
            self._audio_service.play_sound(slide_hit)

        if y < FIELD_TOP:
            puck.bounce_y()
            self._audio_service.play_sound(slide_hit)

        if y >= (FIELD_BOTTOM - PUCK_WIDTH):
            callback.on_next(GAME_OVER)
            self._audio_service.play_sound(goal)
