from departamento import Departamento


class Area(Departamento):
    def __init__(self):
        Departamento.__init__(self)
        self.__nombre_area = ""
        self.__presupuesto = 5


    #getters y setters
    def get_nombre_area(self):
        return self.__nombre_area

    def set_nombre_area(self, nombre_area):
        self.__nombre_area = nombre_area

    def get_presupuesto(self):
        return self.__presupuesto

    def set_presupuesto(self, presupuesto):
        self.__presupuesto = presupuesto

    def generar_reporte(self):
        print(f"{self.__nombre_area} genero un reporte")

    def asignar_presupuesto(self):
        print(f"se asigno x cantidad del presupuesto, presupuesto actual{self.__presupuesto}")

    def mostrar_informacion_area(self):
        print(f"Nombre del Area: {self.__nombre_area},presupuesto: {self.__presupuesto}\n"
              f"departamento: {self.get_nombre_departamento()}, numero de empleados: {self.get_no_empleados()}")

