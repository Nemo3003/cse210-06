from constants import *
from game.scripting.action import Action
from game.casting.image import Image
from game.casting.point import Point


class DrawHudAction(Action):

    def __init__(self, video_service):
        self._video_service = video_service
        
    def execute(self, cast, script, callback):
        stats = cast.get_first_actor(STATS_GROUP)
        self._draw_label(cast, SCORE_GROUP, SCORE_FORMAT, stats.get_score())
        self._video_service.draw_image(Image("air_hockey/assets/images/one.png"), Point(100,50))

    def _draw_label(self, cast, group, format_str, data):
        labels = cast.get_actors(group)
        for label in labels:
            text = label.get_text()
            text.set_value(format_str.format(data))
            position = label.get_position()
            self._video_service.draw_text(text, position)