import Constants
from Action import *

class Command:
    """Base class for all commands"""
    def __init__(self, actor=None, action=None):
        self.registeredActor = actor
        self.action = action

    def registerActor(self, actor):
        if (actor is None):
           raise ValueError("Cannot register this command to 'None'") 
        self.registeredActor = actor

    def errorMessage(self):
        return Constants.Strings.default_error_message

    def validate(self, arguments):
        pass

    def options(self):
        pass

    def execute(self, arguments):
        raise NotImplementedError("A command must implement the execute method")
    
class CommandList:
    """Base class for sets of commands available to actors"""
    def __init__(self, commands={}):
        self.commands = commands;

    def hasCommand(self, commandName):
        return commandName in self.commands

    def getCommand(self, commandName):
        return self.commands[commandName]

    def getCommandActions(self):
        return self.commands.values()

class MoveCommand(Command):
    def __init__(self):
        super().__init__(action=MoveAction())

    def validate(self, arguments):
        if (arguments == ""):
            return None
        arguments = arguments.split()
        if (arguments[0] == "move"):
            if (len(arguments == 1)):
                return None
            arguments = arguments[1:]
        arguments = " ".join(arguments)
        links = self.options()
        validKeys = [x for x in links if x.startswith(arguments)]
        if (len(validKeys) != 1):
            return None
        return validKeys[0]

    def options(self):
        return self.registeredActor.location.links.keys()
         
    def errorMessage(self):
        return "I can't move there... "
         
    def execute(self, arguments):
        linkName = self.validate(arguments)
        if (linkName == None):
            return False
        link = self.registeredActor.location.links[linkName]
        self.action.execute(actor=self.registeredActor, link=link)
        return True
