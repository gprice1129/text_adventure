class Action:
    def execute(self, **kwargs):
        raise NotImplementedError("An action must implement the execute method")

class MoveAction(Action):
    def execute(self, **kwargs):
        actor = kwargs["actor"]
        link = kwargs["link"]
        link.source.removeActor(actor)
        link.destination.insertActor(actor)
        actor.location = link.destination
