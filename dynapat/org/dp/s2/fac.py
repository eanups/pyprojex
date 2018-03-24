class PlantInterface:
    def grow(self): pass


class TreeInterface(PlantInterface):
    def provide_shade(self): pass


class MangoTree(TreeInterface):
    def grow(self):
        print("Growing a mango tree")

    def provide_shade(self):
        print("Provide shade and some mangoes to eat")


class JackFruitTree(TreeInterface):
    def grow(self):
        print("Growing a jack fruit tree")

    def provide_shade(self):
        print("Provide shade and some jack-fruit to eat")


class Tamarind(TreeInterface):
    def grow(self):
        print("Growing a tamarind tree")


class TreeFactory:
    @staticmethod
    def plant_tree(tree):
        if tree == 'mango':
            return MangoTree()
        elif tree == 'jack-fruit':
            return JackFruitTree()
        elif tree == 'tamarind':
            return Tamarind()
        else:
            # raise TypeError("Invalid Tree Type")
            assert 0, 'Could not find tree'


# Make use of the TreeFactory to plant more trees

tree_factory = TreeFactory()
mango_tree = tree_factory.plant_tree('mango')
mango_tree.grow()
mango_tree.provide_shade()

print('-' * 50)

jack_fruit_tree = tree_factory.plant_tree('jack-fruit')
jack_fruit_tree.grow()
jack_fruit_tree.provide_shade()


print('-' * 50)

tamarind_tree = tree_factory.plant_tree('tamarind')
tamarind_tree.grow()
tamarind_tree.provide_shade()
