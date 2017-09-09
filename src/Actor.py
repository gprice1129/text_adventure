from GameObject import *
from Command import CommandList

class Actor(GameObject):
    def __init__(self, description="", items={}, commandList={}, location=None):
        super().__init__(description)
        self.items = GameObjectDictionary(items)
        self.commandList = CommandList(commandList)
        for command in self.commandList.getCommandActions():
            command.registerActor(self)
        self.location = location
        if (location != None):
            location.insertActor(self)
        self.moved = True

    def getCommand(self, commandName):
        if (self.commandList.hasCommand(commandName)):
            return self.commandList.getCommand(commandName)
