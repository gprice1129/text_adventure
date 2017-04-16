# An event is some interaction that happens between a source and a target

# Both sources and targets should be interactables

# How the source and target interact are dependent on how the interaction is
# defined between those two types of interactables
class Event:
    def __init__(self, source, target):
        self.source = source
        self.target = target
        
    def register(self, eventQueue):
        eventQueue.push(self)
        
    def execute(self):
        source.interactWith(target)         
