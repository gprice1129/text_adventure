from GameObject import *

class Link(GameObject):
    def __init__(self, description="", source=None, destination=None):
        super().__init__(description)
        self.source = source
        self.destination = destination
