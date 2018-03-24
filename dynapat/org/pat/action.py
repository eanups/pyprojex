class Action:
    _methods = ['move', 'sleep', 'eat', 'fight', 'sound']

    def __init__(self, animal):
        self.animal = animal

    def __getattr__(self, attr):
        if attr in self._methods:
            return getattr(self.animal, attr)

    def sound(self):
        return self.animal.make_sound()

