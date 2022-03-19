from constants import *
from game.casting.sound import Sound
from game.scripting.action import Action


class CollideStrikerAction(Action):

    def __init__(self, physics_service, audio_service):
        self._physics_service = physics_service
        self._audio_service = audio_service
        
    def execute(self, cast, script, callback):
        puck = cast.get_first_actor(PUCK_GROUP)
        striker = cast.get_first_actor(STRIKER_GROUP)
        
        puck_body = puck.get_body()
        striker_body = striker.get_body()

        if self._physics_service.has_collided(puck_body, striker_body):
            puck.bounce_y()
            sound = Sound(SLIDE_HIT)
            self._audio_service.play_sound(sound)    