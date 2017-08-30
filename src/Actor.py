from GameObject import *
from Command import CommandList

class Actor(GameObject):
    def __init__(self, description="", items=[], commandList={}, location=None):
        super().__init__(description)
        self.items = GameObjectContainer(items)
        self.commandList = CommandList(commandList)
        for command in self.commandList.getCommandActions():
            command.registerActor(self)
        self.location = location
        if (location != None):
            location.appendActor(self)

    def getCommand(self, commandName):
        if (self.commandList.hasCommand(commandName)):
            return self.commandList.getCommand(commandName)
