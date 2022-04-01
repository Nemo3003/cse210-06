import csv
from constants import *
from game.casting.actor import Actor 
from game.casting.animation import Animation
from game.casting.surface import Surface
from game.casting.puck import Puck
from game.casting.body import Body
from game.casting.image import Image
from game.casting.label import Label
from game.casting.point import Point
from game.casting.striker import Striker
from game.casting.stats import Stats
from game.casting.text import Text 
from game.scripting.change_scene_action import ChangeSceneAction
from game.scripting.check_over_action import CheckOverAction
from game.scripting.collide_borders_action import CollideBordersAction
from game.scripting.collide_striker_action import CollideStrikerAction
from game.scripting.collide_striker_action import CollideStrikerAction2
from game.scripting.control_striker_action import ControlStrikerAction
from game.scripting.control_striker_action import ControlStrikerAction2
from game.scripting.draw_surface import DrawSurface
from game.scripting.draw_puck_action import DrawPuckAction
from game.scripting.draw_dialog_action import DrawDialogAction
from game.scripting.draw_hud_action import DrawHudAction
from game.scripting.draw_striker_action import DrawStrikerAction
from game.scripting.draw_striker_action import DrawStrikerAction2
from game.scripting.end_drawing_action import EndDrawingAction
from game.scripting.initialize_devices_action import InitializeDevicesAction
from game.scripting.load_assets_action import LoadAssetsAction
from game.scripting.move_puck_action import MovePuckAction
from game.scripting.move_striker_action import MoveStrikerAction
from game.scripting.move_striker_action import MoveStrikerAction2
from game.scripting.play_sound_action import PlaySoundAction
from game.scripting.release_devices_action import ReleaseDevicesAction
from game.scripting.collide_goal_action import CollideGoalAction
from game.scripting.start_drawing_action import StartDrawingAction
from game.scripting.timed_change_scene_action import TimedChangeSceneAction
from game.scripting.unload_assets_action import UnloadAssetsAction
from game.services.raylib.raylib_audio_service import RaylibAudioService
from game.services.raylib.raylib_keyboard_service import RaylibKeyboardService
from game.services.raylib.raylib_physics_service import RaylibPhysicsService
from game.services.raylib.raylib_video_service import RaylibVideoService
"""
HEY YOU! yes you, here you can manage the different scenes. Video specifically
"""

class SceneManager:
    """The person in charge of setting up the cast and script for each scene."""
    
    AUDIO_SERVICE = RaylibAudioService()
    KEYBOARD_SERVICE = RaylibKeyboardService()
    PHYSICS_SERVICE = RaylibPhysicsService()
    VIDEO_SERVICE = RaylibVideoService(GAME_NAME, SCREEN_WIDTH, SCREEN_HEIGHT)

    CHECK_OVER_ACTION = CheckOverAction()
    COLLIDE_BORDERS_ACTION = CollideBordersAction(PHYSICS_SERVICE, AUDIO_SERVICE)
    COLLIDE_STRIKER_ACTION = CollideStrikerAction(PHYSICS_SERVICE, AUDIO_SERVICE)
    COLLIDE_STRIKER_ACTION2 = CollideStrikerAction2(PHYSICS_SERVICE, AUDIO_SERVICE)
    CONTROL_STRIKER_ACTION = ControlStrikerAction(KEYBOARD_SERVICE)
    CONTROL_STRIKER_ACTION2 = ControlStrikerAction2(KEYBOARD_SERVICE)
    COLLIDE_GOAL_ACTION = CollideGoalAction(PHYSICS_SERVICE,AUDIO_SERVICE)
    DRAW_SURFACE = DrawSurface(VIDEO_SERVICE)
    DRAW_PUCK_ACTION = DrawPuckAction(VIDEO_SERVICE)
    DRAW_DIALOG_ACTION = DrawDialogAction(VIDEO_SERVICE)
    DRAW_HUD_ACTION = DrawHudAction(VIDEO_SERVICE)
    DRAW_STRIKER_ACTION= DrawStrikerAction(VIDEO_SERVICE)
    DRAW_STRIKER_ACTION2= DrawStrikerAction2(VIDEO_SERVICE)
    END_DRAWING_ACTION = EndDrawingAction(VIDEO_SERVICE)
    INITIALIZE_DEVICES_ACTION = InitializeDevicesAction(AUDIO_SERVICE, VIDEO_SERVICE)
    LOAD_ASSETS_ACTION = LoadAssetsAction(AUDIO_SERVICE, VIDEO_SERVICE)
    MOVE_PUCK_ACTION = MovePuckAction()
    MOVE_STRIKER_ACTION = MoveStrikerAction()
    MOVE_STRIKER_ACTION2 = MoveStrikerAction2()
    RELEASE_DEVICES_ACTION = ReleaseDevicesAction(AUDIO_SERVICE, VIDEO_SERVICE)
    START_DRAWING_ACTION = StartDrawingAction(VIDEO_SERVICE)
    UNLOAD_ASSETS_ACTION = UnloadAssetsAction(AUDIO_SERVICE, VIDEO_SERVICE)

    def __init__(self):
        pass

    def prepare_scene(self, scene, cast, script):
        if scene == NEW_GAME:
            self._prepare_new_game(cast, script)
        elif scene == TRY_AGAIN:
            self._prepare_try_again(cast, script)
        elif scene == IN_PLAY:
            self._prepare_in_play(cast, script)
        elif scene == GAME_OVER:    
            self._prepare_game_over(cast, script)
    
    # ----------------------------------------------------------------------------------------------
    # scene methods
    # ----------------------------------------------------------------------------------------------
    
    def _prepare_new_game(self, cast, script):
        self._add_stat_a(cast)
        self._add_stat_b(cast)
        self._add_score_a(cast)
        self._add_score_b(cast)
        self._add_surface(cast)
        self._add_puck(cast)
        self._add_striker(cast)
        self._add_striker2(cast)
        self._add_dialog(cast, ENTER_TO_START)
        

        self._add_initialize_script(script)
        self._add_load_script(script)
        script.clear_actions(INPUT)
        script.add_action(INPUT, ChangeSceneAction(self.KEYBOARD_SERVICE, TRY_AGAIN))
        self._add_output_script(script)
        self._add_unload_script(script)
        self._add_release_script(script)
               
    def _prepare_try_again(self, cast, script):
        self._add_surface(cast)
        self._add_puck(cast)
        self._add_striker(cast)
        self._add_striker2(cast)
        self._add_dialog(cast, FACEOFF)

        script.clear_actions(INPUT)
        script.add_action(INPUT, TimedChangeSceneAction(IN_PLAY, 2))
        self._add_update_script(script)
        self._add_output_script(script)
        script.add_action(OUTPUT, PlaySoundAction(self.AUDIO_SERVICE, PUCK_DROP))

    def _prepare_in_play(self, cast, script):
        self._activate_puck(cast)
        cast.clear_actors(DIALOG_GROUP)

        script.clear_actions(INPUT)
        script.add_action(INPUT, self.CONTROL_STRIKER_ACTION)
        script.add_action(INPUT, self.CONTROL_STRIKER_ACTION2)
        self._add_update_script(script)
        self._add_output_script(script)

    def _prepare_game_over(self, cast, script):
        self._add_surface(cast)
        self._add_puck(cast)
        self._add_striker(cast)
        self._add_striker2(cast)
        self._add_dialog(cast, WAS_GOOD_GAME)

        script.clear_actions(INPUT)
        script.add_action(INPUT, TimedChangeSceneAction(NEW_GAME, 5))
        script.clear_actions(UPDATE)
        self._add_output_script(script)

    # ----------------------------------------------------------------------------------------------
    # casting methods
    # ----------------------------------------------------------------------------------------------
    
    def _activate_surface(self, cast):
        surface = cast.get_first_actor(SURFACE_GROUP)
        surface.release()

    def _add_surface(self, cast):
        cast.clear_actors(SURFACE_GROUP)
        x = 30
        y = SCREEN_HEIGHT - 690
        position = Point(x, y)
        size = Point(SURFACE_WIDTH, SURFACE_HEIGHT)
        body = Body(position, size)
        image = Image(SURFACE_IMAGE)
        surface = Surface(body, image, True)
        cast.add_actor(SURFACE_GROUP, surface)
    
    def _activate_puck(self, cast):
        puck = cast.get_first_actor(PUCK_GROUP)
        puck.release()

    def _add_puck(self, cast):
        cast.clear_actors(PUCK_GROUP)
        x = CENTER_X - (PUCK_WIDTH / 2)
        y = (SCREEN_HEIGHT / 2) - 5
        position = Point(x, y)
        size = Point(PUCK_WIDTH, PUCK_HEIGHT)
        velocity = Point(0, 0)
        body = Body(position, size, velocity)
        image = Image(PUCK_IMAGE)
        puck = Puck(body, image, True)
        cast.add_actor(PUCK_GROUP, puck)

    def _add_dialog(self, cast, message):
        cast.clear_actors(DIALOG_GROUP)
        text = Text(message, FONT_FILE, FONT_SMALL, ALIGN_CENTER)
        position = Point(CENTER_X, CENTER_Y - 123)
        label = Label(text, position)
        cast.add_actor(DIALOG_GROUP, label)

    def _add_score_a(self, cast):
        cast.clear_actors(SCORE_GROUP)
        score_display = PLAYER_A.format(SCORE_FORMAT)
        text = Text(score_display, FONT_FILE, FONT_SMALL, ALIGN_CENTER)
        position = Point(CENTER_X-300, HUD_MARGIN)
        label = Label(text, position)
        cast.add_actor(SCORE_GROUP, label)
    
    def _add_score_b(self, cast):
        score_display = PLAYER_B.format(SCORE_FORMAT)
        text = Text(score_display, FONT_FILE, FONT_SMALL, ALIGN_CENTER)
        position = Point(CENTER_X+300, HUD_MARGIN)
        label = Label(text, position)
        cast.add_actor(SCORE_GROUP, label)

    def _add_stat_a(self, cast):
        cast.clear_actors(STATS_GROUP)
        stats = Stats()
        cast.add_actor(STATS_GROUP, stats)

    def _add_stat_b(self, cast):
        stats = Stats()
        cast.add_actor(STATS_GROUP, stats)

    def _add_striker(self, cast):
        cast.clear_actors(STRIKER_GROUP)
        x = CENTER_X - 490
        y = (SCREEN_HEIGHT / 2) - 25
        position = Point(x, y)
        size = Point(STRIKER_WIDTH, STRIKER_HEIGHT)
        velocity = Point(0, 0)
        body = Body(position, size, velocity)
        image = Image(STRIKER_IMAGES)
        striker = Striker(body, image, True)
        cast.add_actor(STRIKER_GROUP, striker)

    def _add_striker2(self, cast):
        cast.clear_actors(STRIKER_GROUP2)
        x = CENTER_X + 390
        y = (SCREEN_HEIGHT / 2) - 25
        position = Point(x, y)
        size = Point(STRIKER_WIDTH, STRIKER_HEIGHT)
        velocity = Point(0, 0)
        body = Body(position, size, velocity)
        image = Image(STRIKER2_IMAGES)
        striker2 = Striker(body, image, True)
        cast.add_actor(STRIKER_GROUP2, striker2)

    # ----------------------------------------------------------------------------------------------
    # scripting methods
    # ----------------------------------------------------------------------------------------------
    def _add_initialize_script(self, script):
        script.clear_actions(INITIALIZE)
        script.add_action(INITIALIZE, self.INITIALIZE_DEVICES_ACTION)

    def _add_load_script(self, script):
        script.clear_actions(LOAD)
        script.add_action(LOAD, self.LOAD_ASSETS_ACTION)
    
    def _add_output_script(self, script):
        script.clear_actions(OUTPUT)
        script.add_action(OUTPUT, self.START_DRAWING_ACTION)
        script.add_action(OUTPUT, self.DRAW_HUD_ACTION)
        script.add_action(OUTPUT, self.DRAW_SURFACE)
        script.add_action(OUTPUT, self.DRAW_PUCK_ACTION)
        script.add_action(OUTPUT, self.DRAW_STRIKER_ACTION)
        script.add_action(OUTPUT, self.DRAW_STRIKER_ACTION2)
        script.add_action(OUTPUT, self.DRAW_DIALOG_ACTION)
        script.add_action(OUTPUT, self.END_DRAWING_ACTION)

    def _add_release_script(self, script):
        script.clear_actions(RELEASE)
        script.add_action(RELEASE, self.RELEASE_DEVICES_ACTION)
    
    def _add_unload_script(self, script):
        script.clear_actions(UNLOAD)
        script.add_action(UNLOAD, self.UNLOAD_ASSETS_ACTION)
        
    def _add_update_script(self, script):
        script.clear_actions(UPDATE)
        script.add_action(UPDATE, self.MOVE_PUCK_ACTION)
        script.add_action(UPDATE, self.MOVE_STRIKER_ACTION)
        script.add_action(UPDATE, self.MOVE_STRIKER_ACTION2)
        script.add_action(UPDATE, self.COLLIDE_BORDERS_ACTION)
        script.add_action(UPDATE, self.COLLIDE_STRIKER_ACTION)
        script.add_action(UPDATE, self.COLLIDE_STRIKER_ACTION2)
        script.add_action(UPDATE, self.MOVE_STRIKER_ACTION)
        script.add_action(UPDATE, self.MOVE_STRIKER_ACTION2)
        script.add_action(UPDATE, self.CHECK_OVER_ACTION)
