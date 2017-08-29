class Command:
    """Base class for all commands"""
    def __init(self, actor=None):
        self.registeredActor = actor

    def registerActor(self, actor):
        if (actor is None):
           raise ValueError("Cannot register this command to 'None'") 
        self.registeredActor = actor

    def execute(self):
        raise NotImplementedError("A command must implement the execute method")

class CommandList:
    """Base class for sets of commands available to actors"""
    def __init__(self, commands={}):
        self.commands = commands;

    def hasCommand(self, commandName):
        return commands.has_key(commandName)

    def getCommand(self, commandName):
        return commands[commandName]

class Move(Command):
    def execute(self):
        link.source.remove(registeredActor)
        link.destination.append(registeredActor)

class Message(Command):
    def execute(self, message):
        return message
