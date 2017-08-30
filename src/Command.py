class Command:
    """Base class for all commands"""
    def __init__(self, actor=None):
        self.registeredActor = actor

    def registerActor(self, actor):
        if (actor is None):
           raise ValueError("Cannot register this command to 'None'") 
        self.registeredActor = actor

    def getArgumentPrompt(self):
        return None

    def validate(self, arguments):
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

class Move(Command):
    def getArgumentPrompt(self):
        prompt = ""
        links = self.registeredActor.location.links
        for i in range(len(links)):
            prompt += str(i + 1) + ". " + links[i].describe() + "\n"
        prompt += "Choose where you'd like to move: "
        return prompt

    def validate(self, arguments):
        tokens = arguments.split()
        if (len(tokens) == 0):
            return None 
        argument = tokens[0]
        if (not argument.isdigit()):
            return None
        linkIndex = int(argument)
        if (linkIndex > len(self.registeredActor.location.links)):
            return None
        return (linkIndex - 1)
         
    def execute(self, arguments):
        linkIndex = self.validate(arguments)
        if (linkIndex == None):
            return False
        link = self.registeredActor.location.links[linkIndex]
        link.source.removeActor(self.registeredActor)
        link.destination.appendActor(self.registeredActor)
        self.registeredActor.location = link.destination
        return True
