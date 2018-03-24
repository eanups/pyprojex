
class Item:
    def __init__(self, name, i_d_list):
        self.dl = i_d_list
        self.name = name

    def __str__(self):
        return self.name


def get_dep_list(unit):
    def iter_dep(unit, deps, visited):
        if not deps:
            return visited
        else:
            next_unit = deps.pop(0)
            visited.append(next_unit)
            if next_unit.dl:
                deps.extend(next_unit.dl)
                return iter_dep(next_unit, deps, visited)
            else:
                return iter_dep(unit, deps, visited)

    dependency_list = []
    return iter_dep(unit, unit.dl[:], dependency_list)


def get_unique_list(my_list):
    return [e for i, e in enumerate(my_list) if my_list.index(e) == i]


def main():

    K = Item('K', [])
    L = Item('L', [])
    X = Item('X', [K])
    Y = Item('Y', [])
    C = Item('C', [K, L])
    D = Item('D', [Y])
    B = Item('B', [X, Y])
    A = Item('A', [B, C, D])
    res = get_dep_list(A)
    dep_list = [item.__str__() for item in res]
    print("Dependency List       : ", dep_list)
    uniq_dep_list = get_unique_list(dep_list)
    print("Unique Dependency List: ", uniq_dep_list)

if __name__ == '__main__':
    main()
