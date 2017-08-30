from GameObject import * 
from Link import Link

class Node(GameObject):
    def __init__(self, description, actors=list(), items=list(), links=list()):
        super().__init__(description)
        self.actors = GameObjectContainer(actors);
        self.items = GameObjectContainer(items);
        self.links = GameObjectContainer(links);

    def describe(self):
        description = self.description 
        description += "\nActors: " + self.actors.describe()
        description += "\nItems: " + self.items.describe()
        description += "\nLinks: " + self.links.describe() 
        return description

    def remove(self, gameObject, container):
        if (gameObject in container):
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
        self.appendLink(Link(linkDescription, self, node))
        print(self.links.objects is node.links.objects)

    def undirectedConnect(self, node, linkDescription=""):
        self.appendLink(Link(linkDescription, self, node))
        node.appendLink(Link(linkDescription, node, self))
