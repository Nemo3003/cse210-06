from constants import *
from game.casting.point import Point
from game.scripting.action import Action

"""
    What is the striker going to do? Here you can modify that ;)
"""

class MoveStrikerAction(Action):

    def __init__(self):
        pass

    def execute(self, cast, script, callback):
        striker = cast.get_first_actor(STRIKER_GROUP)
        body = striker.get_body()
        velocity = body.get_velocity()
        position = body.get_position()
        x = position.get_x()
        y = position.get_y()
        
        position = position.add(velocity)
        
#This will allow us to make it to bounce
        if x < 0:
            position = Point(0, position.get_y())
        elif x > (SCREEN_WIDTH - STRIKER_WIDTH):
            position = Point(SCREEN_WIDTH - STRIKER_WIDTH, position.get_y())
        elif y < 0:
            position = Point(position.get_x(), 0)
        elif y > (SCREEN_HEIGHT - STRIKER_HEIGHT):
            position = Point(position.get_x(), SCREEN_HEIGHT - STRIKER_HEIGHT)
            
        body.set_position(position)

#Our second striker needs something to do :)
class MoveStrikerAction2(Action):

    def __init__(self):
        pass

    def execute(self, cast, script, callback):
        striker2 = cast.get_first_actor(STRIKER_GROUP2)
        body2 = striker2.get_body()
        velocity2 = body2.get_velocity()
        position2 = body2.get_position()
        x2 = position2.get_x()
        y2 = position2.get_y()
        
        position2 = position2.add(velocity2)

        if x2 < 0:
            position2 = Point(0, position2.get_y())
        elif x2 > (SCREEN_WIDTH - STRIKER_WIDTH):
            position2 = Point(SCREEN_WIDTH - STRIKER_WIDTH, position2.get_y())
        elif y2 < 0:
            position2 = Point(position2.get_x(), 0)
        elif y2 > (SCREEN_HEIGHT - STRIKER_HEIGHT):
            position2 = Point(position2.get_x(), SCREEN_HEIGHT - STRIKER_HEIGHT)
            
        body2.set_position(position2)
