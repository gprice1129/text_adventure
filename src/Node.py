from GameObject import * 
from Link import Link

class Node(GameObject):
    def __init__(self, description, firstDescription=None, 
            actors=dict(), items=dict(), links=dict()):
        super().__init__(description)
        self.visited = False
        self.firstDescription = firstDescription
        self.actors = GameObjectDictionary(actors)
        self.items = GameObjectDictionary(items)
        self.links = GameObjectDictionary(links)

    def describe(self):
        if (self.visited):
            return self.description
        self.visited = True
        if (self.firstDescription == None):
            return self.description
        return self.firstDescription

    def remove(self, gameObject, container):
        if (gameObject.key() in container):
            container.remove(gameObject)
                
    def insert(self, gameObject, container):
        container.insert(gameObject)

    def removeActor(self, actor):
        self.remove(actor, self.actors)

    def insertActor(self, actor):
        self.insert(actor, self.actors)

    def removeItem(self, item):
        self.remove(item, self.items)

    def insertItem(self, item):
        self.insert(item, self.items)
                            
    def removeLink(self, link):
        self.remove(link, self.links)

    def insertLink(self, link):
        self.insert(link, self.links)

    def directedConnect(self, node, validCommands, linkDescription=""):
        self.insertLink(Link(linkDescription, self, node, validCommands))

    def undirectedConnect(self, node, validCommands, linkDescription=""):
        self.directedConnect(node, validCommands, linkDescription)
        node.directedConnect(self, validCommands, linkDescription)
