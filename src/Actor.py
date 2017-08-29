from GameObject import *
from Command import CommandList, Message

class Actor(GameObject):
    def __init__(self, description="", items=[], commandList={}, location=None):
        super(description)
        self.items = GameObjectContainer(items)
        self.commandList = CommandList(commands)
        for commands in commandList.values:
            commands.registerActor(self)
        self.location = location
        if (location != None):
            location.appendActor(self)

   def getCommand(self, commandName):
        if (self.commandList.hasCommand(commandName):
            return self.commandList.getCommand(commandName)
#        if (self.commandList.hasCommand(Constants.Strings.default_command):
#            return self.commandList.getCommand(Constant.Strings.default_command)
#        return Message(Constant.Strings.no_command)
