from constants import *
from game.casting.actor import Actor

#TODO: I honestly, have no idea what is this for. Maybe the actor or maybe the puck...

class Surface(Actor):
    """A solid, spherical object that is bounced around in the game."""
    
    def __init__(self, body, image, debug = False):
        """Constructs a new Puck.

        Args:
            body: A new instance of Body.
            image: A new instance of Image.
            debug: If it is being debugged. 
        """
        super().__init__(debug)
        self._body = body
        self._image = image

    def get_body(self):
        """Gets the puck's body.
        
        Returns:
            An instance of Body.
        """
        return self._body

    def get_image(self):
        """Gets the puck's image.
        
        Returns:
            An instance of Image.
        """
        return self._image
