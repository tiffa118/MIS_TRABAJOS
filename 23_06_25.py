t1 = float(input("temperatura dia 1: "))
t2 = float(input("temperatura dia 2: "))
t3 = float(input("temperatura dia 3: "))

promedio = (t1 + t2 + t3) /3

humedad = float(input("humedad actual (%): "))

if promedio > 30 and humedad < 40:
    print("riego alto:usar 10 litros.")
elif promedio > 25 and humedad < 60:
    print("riego medio:usar 5 litros.") 
else:
    print("riego bajo:usar 2 litros.")    
