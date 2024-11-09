
class Departamento:
    def __init__(self):
        self.__nombre_departamento = ''
        self.__no_empleados = 0

    #getters y setters
    def get_nombre_departamento(self):
        return self.__nombre_departamento

    def set_nombre_departamento(self, nombre_departamento):
        self.__nombre_departamento = nombre_departamento

    def get_no_empleados(self):
        return self.__no_empleados

    def set_no_empleados(self, no_empleados):
        self.__no_empleados = no_empleados

    # metodos de departamento
    def agregar_empleado(self):
        self.__no_empleados += 1

    def quitar_empleado(self):
        self.__no_empleados -= 1