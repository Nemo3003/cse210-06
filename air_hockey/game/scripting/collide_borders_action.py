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


#         1. Find the set of coordinates for the goals (a range of points)
# a.(For left goal) if x < right bound of goalA AND y is between the range of the goal
# b. (For right goal) if x > left bound of goalB AND y is between the range of the goal

        stat_a, stat_b = cast.get_actors(STATS_GROUP)

        if x <= (GOAL_LEFT):
            if y >= (280) and y <= (460):
                stat_b.add_points(1)
                callback.on_next(TRY_AGAIN)
                self._audio_service.play_sound(goal)
                if stat_b.get_score() == 5:
                    callback.on_next(GAME_OVER)
                    callback.on_next(NEW_GAME)

        elif x >= (GOAL_RIGHT):
            if y >= (280) and y <= (460):
                stat_a.add_points(1)
                callback.on_next(TRY_AGAIN)
                self._audio_service.play_sound(goal)
                if stat_a.get_score() == 5:
                    callback.on_next(GAME_OVER)
                    callback.on_next(NEW_GAME)
                


        if x < FIELD_LEFT:
            puck.bounce_x()
            self._audio_service.play_sound(slide_hit)

        if x >= (FIELD_RIGHT - PUCK_WIDTH):
            puck.bounce_x()
            self._audio_service.play_sound(slide_hit)

        if y < (FIELD_TOP):
            puck.bounce_y()
            self._audio_service.play_sound(slide_hit)
            
        if y < (FIELD_TOP):
            puck.bounce_y()
            self._audio_service.play_sound(slide_hit)

        if y >= (FIELD_BOTTOM - 25):
            puck.bounce_y()
            self._audio_service.play_sound(slide_hit)   

# update check

            

