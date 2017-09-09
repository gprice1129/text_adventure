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
    def __init__(self, identifier):
        super().__init__(action=MoveAction())
        self.identifier = identifier

    def validate(self, arguments):
        if (arguments == ""):
            return None
        arguments = arguments.split()
        if (arguments[0] == self.identifier):
            if (len(arguments == 1)):
                return None
            arguments = arguments[1:]
        arguments = " ".join(arguments)
        links = self.options()
        validKeys = [x for x in links if x.startswith(arguments)]
        if (len(validKeys) != 1):
            return None
        return validKeys[0]

    def registerLink(self, link):
        link.registerCommands([self])

    def options(self):
        links = self.registeredActor.location.links
        return [x for x in links.keys() if self.identifier in links[x].validCommands]
         
    def errorMessage(self):
        return "I can't move there... "
         
    def execute(self, arguments):
        linkName = self.validate(arguments)
        if (linkName == None):
            return False
        link = self.registeredActor.location.links[linkName]
        if (link.validate(self.identifier)):
            self.action.execute(actor=self.registeredActor, link=link)
            self.registeredActor.moved = True
            return True
        else: 
            return False

class ClimbCommand(MoveCommand):
    def __init__(self):
        super().__init__(identifier="climb")

    def errorMessage(self):
        return "I can't use that to climb... "

class OpenCommand(MoveCommand):
    def __init__(self):
        super().__init__(identifier="open")

    def errorMessage(self):
        return "I can't open that... "

class UseCommand(MoveCommand):
    def __init__(self):
        super().__init__(identifier="use")
        
    def errorMessage(self):
        return "I can't use that... "
