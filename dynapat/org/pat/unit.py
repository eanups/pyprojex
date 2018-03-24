from abc import abstractmethod, ABCMeta


class Traversal:
    def __init__(self):
        pass

    @staticmethod
    def get_dep_list(unit):
        def iter_dep(curr_unit, deps, visited):
            if not deps:
                return visited
            else:
                next_unit = deps.pop(0)
                visited.append(next_unit)
                if next_unit.dl:
                    deps.extend(next_unit.dl)
                    return iter_dep(next_unit, deps, visited)
                else:
                    return iter_dep(curr_unit, deps, visited)

        d_visited = []
        return Traversal.get_unique_list(iter_dep(unit, unit.dl[:], d_visited))

    @staticmethod
    def get_unique_list(my_list):
        return [e for i, e in enumerate(my_list) if my_list.index(e) == i]


class Unit:
    __metaclass__ = ABCMeta

    def __init__(self, name, unit_id, attributes, dependencies):
        self.name = name
        self.unit_id = unit_id
        self.attr = [attr for attr in attributes]
        self.dl = [dep for dep in dependencies]

    def backup(self, unit):
        dep_list = Traversal.get_dep_list(unit)
        for item in dep_list:
            item.do_backup(item)

    def restore(self):
        pass

    @abstractmethod
    def do_backup(self, unit):
        raise NotImplementedError("do_backup not implemented ..")


class Backfill(Unit):
    def do_backup(self, unit):
        print("Backing up {} application data".format(unit.name))
        print("BFL")


class Reporting(Unit):
    def do_backup(self, unit):
        print("Backing up {} application data".format(unit.name))
        print("REP")


class Tables(Unit):
    def do_backup(self, unit):
        print("Backing up {} tabular data".format(unit.name))
        print("TAB")


class Volumes(Unit):
    def do_backup(self, unit):
        print("Backing up {} for volume data".format(unit.name))
        print("VOL")


class OSFiles(Unit):
    def do_backup(self, unit):
        print("Backing up {} for OS data".format(unit.name))
        print("OS")


def main():
    staging_tables = Tables('STAGING TABLES', 'TL400', ['x'], [])
    os_files = OSFiles('OS Files', 'OS343', ['jjj'], [])
    master_tables = Tables('MASTER TABLES', 'TL500', ['x'], [os_files])
    mapr_volumes = Volumes('VOLUME', 'VL300', ['abc'], [master_tables, os_files, staging_tables])

    bu = Backfill('BACKFILL', 'BU100', ['a', 'b', 'c'], [master_tables, mapr_volumes])
    ru = Reporting('REPORTING', 'RU200', ['b', 'd', 'x'], [staging_tables, master_tables])
    bu.backup(bu)
    print("-" * 80)
    ru.backup(ru)

if __name__ == '__main__':
    main()
