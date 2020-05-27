#Mostrar en pantalla la cantidad de meses transcurridos desde la fecha de nacimiento de un usuario.

from datetime import date
from datetime import datetime
now = datetime.now()

print("Calculadora de Meses de Nacimiento")
print("Ingrese su fecha de nacimiento en números")
dia_nac = int(input("ingrese su día de nacimiento\n"))
mes_nac = int(input("ingrese su mes de nacimiento\n"))
year_nac = int(input("ingrese su año de nacimiento\n"))

#Calcula cuanto meses de vida tiene en el año que nacio
calculo_mes = 12 - mes_nac
21
#Calcula meses de vida del año en curso
meses_year_en_curso = int(now.month)

#Calcula los años menos el año que nacio y el año en curso
year_vida = (int((now.year)) - year_nac) - 2

#Calcula Meses de Vida
meses_vida = (year_vida * 12 ) + calculo_mes + meses_year_en_curso

print("Tienes {} meses de vida".format(meses_vida))