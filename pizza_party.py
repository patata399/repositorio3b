#inicio
personas = 0
pizzas = 0
rebanadasxp = 0
rebanadas = 0
sobrante = 0
reabnadastotal = 0
print("cuantas personas vienen?")
personas = input()
print("cuantas pizzas tienes?")
pizzas = input()
print("de cuantas rebanadas?")
rebanadas = input()
rebanadastotal = rebanadas * pizzas
rebanadasxp = rebanadastotal / personas
sobrante = rebanadas - rebanadasxp
print("cada persona podra comer", rebanadasxp)
print("y sobraran", sobrante)
#fin