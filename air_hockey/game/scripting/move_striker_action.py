from constants import *
from game.casting.point import Point
from game.scripting.action import Action


class MoveStrikerAction(Action):

    def __init__(self):
        pass

    def execute(self, cast, script, callback):
        striker = cast.get_first_actor(STRIKER_GROUP)
        body = striker.get_body()
        velocity = body.get_velocity()
        position = body.get_position()
        x = position.get_x()
        
        position = position.add(velocity)

        if x < 0:
            position = Point(0, position.get_y())
        elif x > (SCREEN_WIDTH - STRIKER_WIDTH):
            position = Point(SCREEN_WIDTH - STRIKER_WIDTH, position.get_y())
            
        body.set_position(position)


class MoveStrikerAction2(Action):

    def __init__(self):
        pass

    def execute(self, cast, script, callback):
        striker2 = cast.get_first_actor(STRIKER_GROUP2)
        body2 = striker2.get_body()
        velocity2 = body2.get_velocity()
        position2 = body2.get_position()
        x2 = position2.get_x()
        
        position2 = position2.add(velocity2)

        if x2 < 0:
            position2= Point(0, position2.get_y())
        elif x2 > (SCREEN_WIDTH - STRIKER_WIDTH):
            position2 = Point(SCREEN_WIDTH - STRIKER_WIDTH, position2.get_y())
            
        body2.set_position(position2)
        