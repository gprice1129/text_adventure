# A generic map element where entities can be placed
from Interactable import Interactable

class Node(Interactable):
    def __init__(self, description="", links=[], interactables=[], 
                       formatter=None):
        self.description = description
        self.links = links
        self.interactions = interactions
        self.formatter = formatter

    def updateDescription(self, newDescription):
        description = newDescription

    def removeLink(self, link):
        links.remove(link)

    def addLink(self, link):
        links.append(link)

    def removeInteractable(self, interactable):
        interactables.remove(interactable)

    def addInteractable(self, interactable):
        interactables.append(interactable)

    def interact(self, target):
        pass

    def display(self):
        self.formatter.display(self)
    
