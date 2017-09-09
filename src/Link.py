from GameObject import *

class Link(GameObject):
    def __init__(self, description="", source=None, 
                 destination=None, validCommands=[]):
        super().__init__(description)
        self.source = source
        self.destination = destination
        self.validCommands = set(validCommands) 

    def validate(self, command):
        if (len(self.validCommands) == 0):
            return True
        return command in self.validCommands
