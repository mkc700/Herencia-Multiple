from Area import Area
from Empleado import Empleado


class Director(Area,Empleado):
    def __init__(self):
        Area.__init__(self)
        Empleado.__init__(self)
        self.__region = ""
        self.__empleados = 0
        self.__presupuesto_asignado = 0

    #getters y setters
    def setEmpleados(self, empleados):
        self.__empleados = empleados
    def setPresupuesto_asignado(self, presupuesto_asignado):
        self.__presupuesto_asignado = presupuesto_asignado

    def getEmpleados(self):
        return self.__Empleados
    def getPresupuesto_asignado(self):
        return self.__presupuesto_asignado

    def setRegion(self, region):
        self.__region = region
    def getRegion(self):
        return self.__region

    def tomar_decision(self):
        print("acabo de tomar un decision el patron")

    def convocar_asamblea(self):
        print("mando a llamarnos el patron")

    def informacion_director(self):
        #ahorita que acabe las demas clases ya acompleto esta
        print(f"Nombre: {self.get_nombre_person()}"
              f"")