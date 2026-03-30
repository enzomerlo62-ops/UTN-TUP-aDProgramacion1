
energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""
forzar_seguidos = 0

nombre_agente = input("nombre del agente: ")
while not nombre_agente.isalpha() or nombre_agente == "":
    print("error: nombre invalido")
    nombre_agente = input("nombre del agente: ")


while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3:
    
    
    if alarma == True and tiempo <= 3:
        print("sistema bloqueado por alarma y falta de tiempo")
        break

    print(f"\n--- estado: energia {energia} | tiempo {tiempo} | cerraduras {cerraduras_abiertas} ---")
    if alarma:
        print("!!! ALARMA ACTIVADA !!!")
    
    print("1. forzar cerradura (-20 energia, -2 tiempo)")
    print("2. hackear panel (-10 energia, -3 tiempo)")
    print("3. descansar (+15 energia, -1 tiempo)")
    
    opcion = input("elija accion: ")
    
    if not opcion.isdigit():
        print("error: ingrese un numero")
        continue

    if opcion == "1":
        forzar_seguidos = forzar_seguidos + 1
        
        
        if forzar_seguidos >= 3:
            energia = energia - 20
            tiempo = tiempo - 2
            alarma = True
            print("la cerradura se trabo por forzar demasiado. alarma activada")
        else:
            
            energia = energia - 20
            tiempo = tiempo - 2
            
            
            if energia < 40:
                print("riesgo de alarma detectado")
                n_riesgo = input("elija un numero del 1 al 3: ")
                while not n_riesgo.isdigit():
                    n_riesgo = input("error, elija un numero 1-3: ")
                
                if n_riesgo == "3":
                    alarma = True
                    print("activaste la alarma por falta de precision")
            
            
            if alarma == False:
                cerraduras_abiertas = cerraduras_abiertas + 1
                print("cerradura abierta con exito")

    elif opcion == "2":
        forzar_seguidos = 0 
        energia = energia - 10
        tiempo = tiempo - 3
        
        
        print("hackeando sistema...")
        for i in range(1, 5):
            codigo_parcial = codigo_parcial + "A"
            print(f"progreso: {codigo_parcial}")
            
        if len(codigo_parcial) >= 8:
            cerraduras_abiertas = cerraduras_abiertas + 1
            codigo_parcial = "" 
            print("hackeo exitoso, cerradura abierta")

    elif opcion == "3":
        forzar_seguidos = 0 
        tiempo = tiempo - 1
        
        
        if alarma == True:
            energia = energia + 5 
            print("descansas poco por el ruido de la alarma")
        else:
            energia = energia + 15
            print("has recuperado energia")
            
        
        if energia > 100:
            energia = 100
            
    else:
        print("opcion no valida")


if cerraduras_abiertas == 3:
    print(f"\nfelicidades agente {nombre_agente}, entraste a la boveda. VICTORIA")
elif energia <= 0:
    print("\nte quedaste sin energia. DERROTA")
elif tiempo <= 0:
    print("\nse acabo el tiempo. DERROTA")
else:
    print("\nno pudiste abrir la boveda a tiempo. DERROTA")