import action
import being

dog = being.Dog()
duck = being.Duck()

dog_act = action.Action(dog)
duck_act = action.Action(duck)

try:
    print dog_act.sound()
    print duck_act.sound()
except AttributeError:
    print 'Invalid Action'


