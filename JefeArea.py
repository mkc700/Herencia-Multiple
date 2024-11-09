from Empleado import Empleado
from Area import Area


class JefeArea(Area,Empleado):
    def __init__(self):
        Area.__init__(self)
        Empleado.__init__(self)
        self.objetivo_area = ""

    #getter y setter
    def get_objetivo_area(self):
            return self.objetivo_area
    def set_objetivo_area(self, object_area):
            self.objetivo_area = object_area

    #metodos particulares
    def asignar_supervisor(self):
        print("el nuevo supervisor es x")
    def ccnvocar_reunion(self):
        print("llamando a la gente....")