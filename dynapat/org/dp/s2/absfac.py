class PlantInterface:
    def grow(self): pass


class TreeInterface(PlantInterface):
    def provide_shade(self): pass


class FruitTreeInterface(TreeInterface):
    def provide_fruit(self): pass


class WoodTreeInterface(TreeInterface):
    def provide_wood(self): pass


class MangoTree(FruitTreeInterface):
    def grow(self):
        print("Growing a mango tree")

    def provide_shade(self):
        print("Provide shade to rest")

    def provide_fruit(self):
        print("Provide mangoes to eat in summer")


class JackFruitTree(FruitTreeInterface):
    def grow(self):
        print("Growing a jack fruit tree")

    def provide_shade(self):
        print("Provide plenty of shade to rest")

    def provide_fruit(self):
        print("Provide jack fruits to eat")


class TeakTree(WoodTreeInterface):
    def grow(self):
        print("Growing a jack fruit tree")

    def provide_shade(self):
        print("Provide plenty of shade to rest")

    def provide_wood(self):
        print("Provide Teak to build furniture")


class Tamarind(TreeInterface):
    def grow(self):
        print("Growing a tamarind tree")

# ------


class GrowTreeInterface:
    def grow_tree(tree): pass


class WoodTreeFactory(GrowTreeInterface):
    @staticmethod
    def grow_tree(tree):
        if tree == 'teak':
            return TeakTree()
        else:
            # raise TypeError("Invalid Tree Type")
            assert 0, 'Could not find tree'


class FruitTreeFactory(GrowTreeInterface):
    @staticmethod
    def grow_tree(tree):
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

tree_factory = FruitTreeFactory()
mango_tree = tree_factory.grow_tree('mango')
mango_tree.grow()
mango_tree.provide_shade()

print('-' * 50)

jack_fruit_tree = tree_factory.grow_tree('jack-fruit')
jack_fruit_tree.grow()
jack_fruit_tree.provide_shade()


print('-' * 50)

tamarind_tree = tree_factory.grow_tree('tamarind')
tamarind_tree.grow()
# tamarind_tree.provide_shade()

print('-' * 50)


tree_factory = WoodTreeFactory()
teak_tree = tree_factory.grow_tree('teak')
teak_tree.grow()
teak_tree.provide_shade()
teak_tree.provide_wood()
