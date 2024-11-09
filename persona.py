class Persona:
    def __init__(self):
        self.__nombre_person = ""
        self.__apellido_person = ""
        self.__edad_person = 0




    #getters y setters

    def get_nombre_person(self):
        return self.__nombre_person

    def set_nombre_person(self, nombre_person):
        self.__nombre_person = nombre_person

    def get_apellido_person(self):
        return self.__apellido_person

    def set_apellido_person(self, apellido_person):
        self.__apellido_person = apellido_person

    def get_edad_person(self):
        return self.__edad_person
    def set_edad_person(self, edad_person):
        self.__edad_person = edad_person

    # metodos de persona
    def calcular_antiguedad(self):
        print("su antiguedad es de x años, y meses y z dias")
