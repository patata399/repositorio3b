anio_actual = 2021
print("cual es tu edad")
edad_actual = int(input())
print("a que edad deseas retirarte?")
edad_de_retiro = int(input())
anios_para_retiro = edad_de_retiro - edad_actual
anio_de_retiro = anio_actual + anios_para_retiro
print("tienes", anios_para_retiro, "años antes de que te puedas retirar")
print("lo podras ahcer en el año", anio_de_retiro)