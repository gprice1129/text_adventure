from Actor import *
from Node import *
from Command import *
from Link import *
from Interface import Interface
import Constants

# Simple example of a game

# Build the rooms 
nodeA = Node(
"""You find yourself in a blindingly white room. It takes a minute before your eyes adjust. 
You can see a grey hallway to your left and a green doorway on the far side of the room.""")
nodeB = Node(
"""You enter the black room. You can see the grey hallway and the ladder in the center of the room.""",
"""You walk into a room with pitch black paint on the walls and floor. You get flashbacks to the nightmares of your childhood. 
You see a grey hallway and you can make out a ladder in the middle of the room.""") 
nodeC = Node(
"""You walk into a green room filled with vegetation. There doesn't appear to be any other exit than the white doorway you came through.
You can hear rustling in the plants that surround you, is there something else in here?""")
nodeD = Node("""You climb the ladder and find yourself in a dimly lit room. There appears to be a thick coat of dust covering everything.
Looking closer at the floor you can see blood stains. You get the feeling you should leave as soon as possible.""")

# Build the links 
nodeA.undirectedConnect(nodeB, "Grey hallway")
nodeA.directedConnect(nodeC, "Green doorway")
nodeC.directedConnect(nodeA, "White doorway")
nodeD.undirectedConnect(nodeB, "Ladder")

# Build the player
player_commands = {"move": MoveCommand()}
player = Actor("Some person", commandList=player_commands, location=nodeA)

# Create the interface
interface = Interface(default="Enter a command: ", options=player_commands)

# Main loop
running = True

while running:
    interface.output(player.location.describe())
    userInput = interface.getInput()
    commandName, arguments = interface.getCommand(userInput)
    command = player.getCommand(commandName)
    commandError = None
    if (command != None):
        didCommandExecute = command.execute(arguments)
        if (not didCommandExecute):
            errorMessage = command.errorMessage()
            interface.output(errorMessage)
    else: 
        interface.output(Constants.Strings.default_error_message)
    interface.output()
