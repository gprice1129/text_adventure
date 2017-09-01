# Base class for all objects in the game

class GameObject:
    def __init__(self, description=""):
        self.description = description

    def describe(self):
        return self.description

    def key(self):
        return self.description.lower()

class GameObjectContainer(GameObject):
    def __init__(self):
        super().__init__()

    def __getitem__(self, key):
        return self.objects.__getitem__(key)

    def __len__(self):
        return len(self.objects)

    def __str__(self):
        return str(self.objects)

    def __contains__(self, item):
        return self.objects.__contains__(item)

    def __delitem__(self, item):
        self.objects.__delitem__(item)

class GameObjectList(GameObjectContainer):
    def __init__(self, objects):
        self.objects = list(objects)
        super().__init__()

    def describe(self):
        return ", ".join(map(lambda x: x.describe(), self.objects))

    def append(self, gameObject):
        self.objects.append(gameObject)

    def remove(self, gameObject):
        self.objects.remove(gameObject)


class GameObjectDictionary(GameObjectContainer):
    def __init__(self, objects):
        self.objects = dict(objects)
        super().__init__()

    def describe(self):
        return " ".join(map(lambda x: x.describe(), self.objects.values()))

    def keys(self):
        return self.objects.keys()

    def values(self):
        return self.objects.values()

    def insert(self, gameObject):
        self.objects[gameObject.key()] = gameObject

    def remove(self, gameObject):
        del self.objects[gameObject.key()]
