operador = input("nombre del operador: ")
while not operador.isalpha() or operador == "":
    print("error")
    operador = input("nombre del operador: ")

lunes1 = ""
lunes2 = ""
lunes3 = ""
lunes4 = ""

martes1 = ""
martes2 = ""
martes3 = ""
opcion = ""
while opcion != "5":
    print("\n--- agenda de turnos ---")
    print("1. reservar")
    print("2. cancelar")
    print("3. ver dia")
    print("4. resumen")
    print("5. salir")
    
    opcion = input("elija opcion: ")
    
    if not opcion.isdigit():
        print("error: ingrese un numero")
        continue

    if opcion == "1":
        dia = input("dia (1=lunes, 2=martes): ")
        if dia == "1" or dia == "2":
            paciente = input("nombre del paciente: ")
            while not paciente.isalpha() or paciente == "":
                print("error")
                paciente = input("nombre del paciente: ")
            
            if dia == "1":
            
                if paciente == lunes1 or paciente == lunes2 or paciente == lunes3 or paciente == lunes4:
                    print("el paciente ya tiene turno ese dia")
                elif lunes1 == "": lunes1 = paciente
                elif lunes2 == "": lunes2 = paciente
                elif lunes3 == "": lunes3 = paciente
                elif lunes4 == "": lunes4 = paciente
                else: print("no hay mas cupos para el lunes")
            
            else: 
                if paciente == martes1 or paciente == martes2 or paciente == martes3:
                    print("el paciente ya tiene turno ese dia")
                elif martes1 == "": martes1 = paciente
                elif martes2 == "": martes2 = paciente
                elif martes3 == "": martes3 = paciente
                else: print("no hay mas cupos para el martes")
        else:
            print("dia invalido")

    elif opcion == "2":
        dia = input("dia para cancelar (1 o 2): ")
        paciente = input("nombre del paciente a borrar: ")
        if dia == "1":
            if lunes1 == paciente: lunes1 = ""
            elif lunes2 == paciente: lunes2 = ""
            elif lunes3 == paciente: lunes3 = ""
            elif lunes4 == paciente: lunes4 = ""
            else: print("no se encontro al paciente")
        elif dia == "2":
            if martes1 == paciente: martes1 = ""
            elif martes2 == paciente: martes2 = ""
            elif martes3 == paciente: martes3 = ""
            else: print("no se encontro al paciente")

    elif opcion == "3":
        dia = input("ver agenda (1=lunes, 2=martes): ")
        if dia == "1":
            print(f"1. {lunes1 if lunes1 != '' else '(libre)'}")
            print(f"2. {lunes2 if lunes2 != '' else '(libre)'}")
            print(f"3. {lunes3 if lunes3 != '' else '(libre)'}")
            print(f"4. {lunes4 if lunes4 != '' else '(libre)'}")
        elif dia == "2":
            print(f"1. {martes1 if martes1 != '' else '(libre)'}")
            print(f"2. {martes2 if martes2 != '' else '(libre)'}")
            print(f"3. {martes3 if martes3 != '' else '(libre)'}")

    elif opcion == "4":
        
        ocu_l = 0
        if lunes1 != "": ocu_l = ocu_l + 1
        if lunes2 != "": ocu_l = ocu_l + 1
        if lunes3 != "": ocu_l = ocu_l + 1
        if lunes4 != "": ocu_l = ocu_l + 1
        
        
        ocu_m = 0
        if martes1 != "": ocu_m = ocu_m + 1
        if martes2 != "": ocu_m = ocu_m + 1
        if martes3 != "": ocu_m = ocu_m + 1
        
        print(f"lunes: {ocu_l} ocupados, {4 - ocu_l} libres")
        print(f"martes: {ocu_m} ocupados, {3 - ocu_m} libres")
        
        if ocu_l > ocu_m:
            print("el dia con mas turnos es el lunes")
        elif ocu_m > ocu_l:
            print("el dia con mas turnos es el martes")
        else:
            print("hay empate en la cantidad de turnos")
print(f"sistema cerrado por {operador}")