# Base class for all objects in the game

class GameObject:
    def __init__(self, description=""):
        self.description = description

    def describe(self):
        return self.description

class GameObjectContainer(GameObject):
    def __init__(self, objects=[]):
        super()
        self.objects = objects

    def describe(self):
        return ", ".join(self.objects) 

    def append(self, gameObject):
        self.objects.append(gameObject)

    def remove(self, gameObject):
        self.objects.remove(gameObject)
