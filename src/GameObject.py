# Base class for all objects in the game

class GameObject:
    def __init__(self, description=""):
        self.description = description

    def describe(self):
        return self.description

class GameObjectContainer(GameObject):
    def __init__(self, objects):
        super().__init__()
        self.objects = list(objects)

    def __len__(self):
        return len(self.objects)

    def __getitem__(self, key):
        return self.objects[key]

    def __str__(self):
        return str(self.objects)

    def describe(self):
        return ", ".join(map(lambda x: x.describe(), self.objects))

    def append(self, gameObject):
        self.objects.append(gameObject)

    def remove(self, gameObject):
        self.objects.remove(gameObject)
