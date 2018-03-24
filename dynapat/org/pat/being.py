
class Animal(object):
    sound = ' mmmm'

    def blah(self):
        pass

    def make_sound(self):
        return "Making sound:" + self.sound


class Duck(Animal):
    def __init__(self):
        self.sound = ' Quack Quack'

    def quack(self):
        return self.make_sound()


class Cheetah(Animal):
    def make_sound(self):
        return "Zoooom"


class Dog(Animal):
    def __init__(self):
        self.sound = ' Bow Wow'


def ping(type):
    animal = None
    if type == 'duck':
        animal = Duck()
    elif type == 'dog':
        animal = Dog()
    elif type == 'cheetah':
        animal = Cheetah()
    else:
        print "Error in type"

    try:
        print animal.make_sound()
    except:
        print "Cannot Bark"


# ping('cheetah')
