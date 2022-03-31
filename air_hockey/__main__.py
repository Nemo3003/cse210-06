from constants import *
from game.directing.director import Director
from game.directing.scene_manager import SceneManager

"""
MAIN: The main file is used to execute the game. Just hit "run" and enjoy the magic 
Disclaimer: Sometimes some errors may come out, we are terrible sorry about that, we did our best :)
"""
def main():
    director = Director(SceneManager.VIDEO_SERVICE)
    director.start_game()

if __name__ == "__main__":
    main()
