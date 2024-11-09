from Empleado import Empleado
from Area import Area

class Gerente(Area,Empleado):
    def __init__(self):
        Area.__init__(self)
        Empleado.__init__(self)
        self.cargo = ""
        self.objetivo_estrategico = ""

    #getters y setters

    def get_cargo(self):
        return self.cargo
    def get_objetivo_estrategico(self):
        return self.objetivo_estrategico

    def set_cargo(self, cargo):
        self.cargo = cargo
    def set_objetivo_estrategico(self, objetivo):
        self.objetivo_estrategico = objetivo

    #metodos particulares
    def evaluar_empleados(self):
        print("se realiza la evaluacion de empleados")
    def dar_feedback(self):
        print("animo gente si se puede!")