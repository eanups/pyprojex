class Tree(object):
    """ Base class for all plants """
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def get_name(self):
        return self.name

    def get_species(self):
        return self.species

    def __str__(self):
        return "%s is a %s Tree" % (self.name, self.species)


class MangoTree(Tree):

    def __init__(self, name, is_tall):
        super().__init__(name, "Mango")
        self.is_tall = is_tall

    def __str__(self):
        more_info = ""
        if self.is_tall:
            more_info = " and is wide"
        return super().__str__() + more_info


class CoconutTree(Tree):

    def __init__(self, name, is_wide):
        super().__init__(name, "Coconut")
        self.is_wide = is_wide

    def __str__(self):
        more_info = ""
        if self.is_wide:
            more_info = " and is Tall"
        return super().__str__() + more_info


# Run and check

banyan = Tree("LonelyTree", "Banyan")
print(banyan)

mango = MangoTree("TangyMangy", True)
print(mango)

coconut = CoconutTree("Coco", True)
print(coconut)

print(CoconutTree.__bases__)
print(Tree.__subclasses__())



