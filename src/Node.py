from GameObject import * 
from Link import Link

class Node(GameObject):
    def __init__(self, description, actors=[], items=[], links=[]):
        super(description)
        self.actors = GameObjectContainer(actors);
        self.items = GameObjectContainer(items);
        self.links = GameObjectContainer(links);

    def describe(self):
        print self.description
        print "Actors: " + actors.describe()
        print "Items: " + items.describe()
        print "Links: " + links.describe() 

    def remove(self, gameObject, container):
        if (container.count(gameObject) > 0):
            container.remove(gameObject)
    
    def append(self, gameObject, container):
        container.append(gameObject)

    def removeActor(self, actor):
        self.remove(actor, self.actors)

    def appendActor(self, actor):
        self.append(actor, self.actors)

    def removeItem(self, item):
        self.remove(item, self.items)

    def appendItem(self, item):
        self.append(item, self.items)
                            
    def removeLink(self, link):
        self.remove(link, self.links)

    def appendLink(self, link):
        self.append(link, self.links)

    def directedConnect(self, node, linkDescription=""):
        link = Link(linkDescription, self, node)
        self.appendLink(link) 

    def undirectedConnect(self, node, linkDescription=""):
        self.directedConnect(node, linkDescription)
        node.directedConnect(self, linkDescription) 
