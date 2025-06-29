temporada = input("temporada (baja,media,alta):")
presupuesto = float(input("presupuesto disponible:"))

if temporada == "baja":
    if presupuesto >=1300:
        print("viaje internacional.")
    elif presupuesto >= 800:
        print("viaje nacional.")
    elif presupuesto > 400:
        print ("viaje local.")
    else:
        print("debes quedarte en casa.") 
elif temporada ==" media":
    if presupuesto >= 800:
        print("viaje nacional.")
    elif presupuesto > 400:
        print("viaje local")
    else:
        print("debes quedarte en casa.")  
elif temporada =="alta":
    if presupuesto > 400:
        print("viaje local.") 
    else:
        ("debes quedarte en casa")   
else:
    print("puedes viajar")            
