from Actor import *
from Node import *
from Command import *
from Link import *
import Interface
import Constants

# Simple example of a game

# Build the rooms 
nodeA = Node("A white room")
nodeB = Node("A black room")
nodeC = Node("A green room")
nodeD = Node("A blue room")

# Build the links 
nodeA.undirectedConnect(nodeB, "Grey hallway")
nodeA.directedConnect(nodeC, "Green doorway")
nodeC.directedConnect(nodeA, "White doorway")
nodeD.undirectedConnect(nodeB, "Ladder")
# Build the player
player_commands = {"use": Move()}
player = Actor("Some person", commandList=player_commands, location=nodeA)

# Main loop

running = True

while running:
    Interface.output(player.location.describe())
    commandName = Interface.getCommand("Enter a command: ")    
    command = player.getCommand(commandName)
    if (command != None):
        argumentPrompt = command.getArgumentPrompt()
        arguments = Interface.getInput(argumentPrompt)
        executionSuccess = command.execute(arguments)
    if (command == None or not executionSuccess):
        print("I can't do that...")
