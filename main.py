from Director import Director
from Gerente import Gerente
from JefeArea import JefeArea

Patron = Director()

Patron.set_nombre_person("Manuel")
Patron.set_apellido_person("Carrasco")
Patron.set_edad_person(60)
#__________________________________________
Patron.setPuesto("Director")
Patron.setTurno("matutino")
Patron.setSueldo(45000)
#__________________________________________
Patron.set_nombre_area("Administrativa")
Patron.set_presupuesto(200000)
Patron.set_nombre_departamento("Administrativa general")
Patron.set_no_empleados(50)
#__________________________________________
Patron.setRegion("pachuca")
Patron.setPresupuesto_asignado(120000)



jefe = JefeArea()


jefe.set_nombre_person("Daniel")
jefe.set_apellido_person("Vargas")
jefe.set_edad_person(52)
#___________________________________
jefe.setPuesto("Jefe de area")
jefe.setTurno("mañana")
jefe.setSueldo(32000)
#__________________________________
jefe.set_nombre_area("Administrativa")
jefe.set_presupuesto(150000)
jefe.set_nombre_departamento("Administrativa general")
jefe.set_no_empleados(30)
#____________________________________
jefe.set_objetivo_area("mejorar el ambiente laboral")




jefecito = Gerente()

jefecito.set_objetivo_estrategico("llevar a esta empresa un buen nivel para que lo asciendan")

jefecito.set_nombre_person("Juan")
jefecito.set_apellido_person("Morales")
jefecito.set_edad_person(25)
#________________________________________
jefecito.setPuesto("Gerente")
jefecito.setTurno("matutino")
jefecito.setSueldo(45000)
#________________________________________
jefecito.set_nombre_area("Administrativa")
jefecito.set_presupuesto(200000)
jefecito.set_nombre_departamento("Administrativa general")
jefecito.set_no_empleados(15)
#___________________________________________
jefecito.set_objetivo_estrategico("Que los trabajadores entreguen un producto de calidad")


#_____________ Metodos____________________

print("Informacion de empleados")

print("\n")
Patron.mostrar_informacion_empleado()
print("\n")
jefe.mostrar_informacion_empleado()
print("\n")
jefecito.mostrar_informacion_empleado()
print("\n")

print("informacion por areas")

print("\n")
Patron.mostrar_informacion_area()
print("\n")
jefe.mostrar_informacion_area()
print("\n")
jefecito.mostrar_informacion_area()
