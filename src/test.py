from Actor import *
from Node import *
from Command import *
from Link import *
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
player_commands = {"use": MoveCommand()}
player = Actor("Some dude", commandList=player_commands, location=NodeA)

# Main loop

running = True

while running:
    

