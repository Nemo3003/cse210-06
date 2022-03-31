import pathlib
from game.casting.color import Color

# -------------------------------------------------------------------------------------------------- 
# GENERAL GAME CONSTANTS
# -------------------------------------------------------------------------------------------------- 

# GAME
GAME_NAME = "Air Hockey Game - Group 8"
FRAME_RATE = 60

# SCREEN
SCREEN_WIDTH = 1100
SCREEN_HEIGHT = 750
CENTER_X = SCREEN_WIDTH / 2
CENTER_Y = SCREEN_HEIGHT / 2

# FIELD
FIELD_TOP = 60 + 45
FIELD_BOTTOM = SCREEN_HEIGHT - 40
FIELD_LEFT = 55
FIELD_RIGHT = SCREEN_WIDTH - 55

# GOAL 
GOAL_TOP = 60
GOAL_BOTTOM = SCREEN_HEIGHT
GOAL_LEFT = 0
GOAL_RIGHT = SCREEN_WIDTH

# FONT
FONT_FILE = "air_hockey/assets/fonts/zorque.otf"
FONT_SMALL = 32
FONT_LARGE = 48

# SOUND
COUNTDOWN_A = "air_hockey/assets/sounds/countdown_a.wav"
COUNTDOWN_B = "air_hockey/assets/sounds/countdown_b.wav"
GOAL = "air_hockey/assets/sounds/goal.wav"
PUCK_DROP = "air_hockey/assets/sounds/puck_drop.wav"
SLIDE = "air_hockey/assets/sounds/slide.wav"
SLIDE_HIT = "air_hockey/assets/sounds/slide_hit.wav"

# TEXT
ALIGN_CENTER = 0
ALIGN_LEFT = 1
ALIGN_RIGHT = 2

# COLORS
BLACK = Color(0, 0, 0)
WHITE = Color(255, 255, 255)
PURPLE = Color(255, 0, 255)

# KEYS
A = "a"
S = "s"
D = "d"
W = "w"

LEFT = "left"
RIGHT = "right"
UP = "up"
DOWN = "down"

SPACE = "space"
ENTER = "enter"
PAUSE = "p"

# SCENES
NEW_GAME = 0
TRY_AGAIN = 1
IN_PLAY = 3
GAME_OVER = 4

# -------------------------------------------------------------------------------------------------- 
# SCRIPTING CONSTANTS
# -------------------------------------------------------------------------------------------------- 

# PHASES
INITIALIZE = 0
LOAD = 1
INPUT = 2
UPDATE = 3
OUTPUT = 4
UNLOAD = 5
RELEASE = 6

# -------------------------------------------------------------------------------------------------- 
# CASTING CONSTANTS
# -------------------------------------------------------------------------------------------------- 

# STATS
STATS_GROUP = "stats"

# HUD
HUD_MARGIN = 15
SCORE_GROUP = "score"
SCORE_FORMAT = "SCORE: {}"

# SURFACE
SURFACE_GROUP = "surface"
SURFACE_IMAGE = "air_hockey/assets/images/surface.png"
SURFACE_WIDTH = 1040
SURFACE_HEIGHT = 669

# PUCK
PUCK_GROUP = "pucks"
PUCK_IMAGE = "air_hockey/assets/images/puck.png"
PUCK_WIDTH = 50
PUCK_HEIGHT = 50
PUCK_VELOCITY = 6

# STRIKERS
STRIKER_GROUP = "striker"
STRIKER_GROUP2 = "striker2"
STRIKER_IMAGES = "air_hockey/assets/images/striker.png"
STRIKER_WIDTH = 100
STRIKER_HEIGHT = 99
STRIKER_RATE = 6
STRIKER_VELOCITY = 8


# DIALOG
DIALOG_GROUP = "dialogs"
ENTER_TO_START = "PRESS ENTER TO START"
FACEOFF = "FACEOFF"
WAS_GOOD_GAME = "GAME OVER"
