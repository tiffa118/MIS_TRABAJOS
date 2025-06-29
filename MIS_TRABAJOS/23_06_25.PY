categoria = int(input (" ingrese la categoria "))
sueldo = float (input("ingrese el sueldo actual "))

if categoria == 1:
    aumento = sueldo *0.20
elif categoria == 2:
    aumento = sueldo*0.15
elif categoria == 3:
    aumento = sueldo*0.10
elif categoria == 4:
    aumento = sueldo*0.05
else: 
    aumento = 0

if  aumento > 0:
    nuevoSueldo = sueldo + aumento
    print("categoria:",categoria)
    print("el nuevo sueldo es:",nuevoSueldo)

else:
    print("categoria no valido.sueldo sin cambio:", sueldo)