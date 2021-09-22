print("Que operacion quieres hacer?")
entrada = input()
print("dame el primer numero")
num1 = float(input())
print("dame el segundo numero")
num2 = float(input())
resultado = 0
if entrada == "suma":
  resultado = num1 + num2
elif operacion == "resta" :
  resultado = num1 - num2
print("el resultado de la", entrada, "es", resultado)
