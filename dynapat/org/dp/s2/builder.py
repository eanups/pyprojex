

class WindTurbine:

    def __str__(self) -> str:
        blades_str = [str(blade) for blade in self.__blades]
        return "\nWind Turbine:\n\t" + str(blades_str) + "\n\t" + str(self.__shaft) + "\n\t" + str(self.__generator)

    # def __getattribute__(self, name: str) -> Any:
    #     return super().__getattribute__(name)

    def __init__(self):
        self.__blades = list()
        self.__shaft = None
        self.__generator = None

    def set_blades(self, blades):
        self.__blades = blades

    def get_blades(self):
        return self.__blades

    def get_shaft(self):
        return self.__shaft

    def get_generator(self):
        return self.__generator

    def set_shaft(self, shaft):
        self.__shaft = shaft

    def set_generator(self, generator):
        self.__generator = generator


class Blade:
    size = None

    def __str__(self):
        return "Blade Size:" + str(self.size)


class Shaft:
    type = None

    def __str__(self):
        return " Shaft Type:" + str(self.type)


class Generator:
    motor = None

    def __str__(self):
        return " Motor Type:" + str(self.motor)


class Director:
    __builder = None

    def set_builder(self, builder):
        self.__builder = builder

    def assemble_turbine(self):
        turbine = WindTurbine()

        shaft = self.__builder.build_shaft()
        turbine.set_shaft(shaft)

        generator = self.__builder.build_generator()
        turbine.set_generator(generator)

        blades = list()
        for i in range(4):
            blade = self.__builder.build_blade()
            blades.append(blade)
        turbine.set_blades(blades)

        return turbine


class TurbineBuilder:
    """
    Interface
    """
    def build_shaft(self): pass

    def build_generator(self): pass

    def build_blade(self): pass


class GETurbineBuilder(TurbineBuilder):

    def build_shaft(self):
        shaft = Shaft()
        shaft.type = 'GE Type-A'
        return shaft

    def build_blade(self):
        blade = Blade()
        blade.size = 120
        return blade

    def build_generator(self):
        generator = Generator()
        generator.motor = 'Top Spin Motor'
        return generator


class SiemensTurbineBuilder(TurbineBuilder):
    def build_shaft(self):
        shaft = Shaft()
        shaft.type = 'Siemens Type-14'
        return shaft

    def build_blade(self):
        blade = Blade()
        blade.size = 140
        return blade

    def build_generator(self):
        generator = Generator()
        generator.motor = 'Optimized Spin Motor'
        return generator

# Test

director = Director()
director.set_builder(GETurbineBuilder())
print(director.assemble_turbine())


director.set_builder(SiemensTurbineBuilder())
print(director.assemble_turbine())
