
nombre = input("nombre del gladiador: ")
while not nombre.isalpha() or nombre == "":
    print("error: solo se permiten letras.")
    nombre = input("nombre del gladiador: ")

vida_jugador = 100
vida_enemigo = 100
pociones = 3
ataque_pesado = 15
ataque_enemigo = 12
juego_activo = True 
print("=== inicio del combate ===")
while vida_jugador > 0 and vida_enemigo > 0:
    print(f"\n{nombre} (hp: {vida_jugador}) vs enemigo (hp: {vida_enemigo}) | pociones: {pociones}")
    print("1. ataque pesado")
    print("2. rafaga veloz")
    print("3. curar")
    
    opcion = input("elija accion: ")
    
    
    while not opcion.isdigit() or (opcion != "1" and opcion != "2" and opcion != "3"):
        print("error: ingrese un numero valido (1, 2 o 3).")
        opcion = input("opcion: ")

    
    if opcion == "1":
        
        daño_final = float(ataque_pesado)
        if vida_enemigo < 20:
            daño_final = daño_final * 1.5
            print("!golpe critico!")
        
        vida_enemigo = vida_enemigo - int(daño_final)
        print(f"atacaste al enemigo por {daño_final} puntos de daño")

    elif opcion == "2":
       
        print(">> ¡inicias una rafaga de golpes!")
        for i in range(3):
            vida_enemigo = vida_enemigo - 5
            print("> golpe conectado por 5 de daño")

    elif opcion == "3":
        
        if pociones > 0:
            vida_jugador = vida_jugador + 30
            if vida_jugador > 100:
                vida_jugador = 100
            pociones = pociones - 1
            print(f"te has curado. vida actual: {vida_jugador}")
        else:
            print("¡no quedan pociones! perdiste el turno intentando curarte")

    
    if vida_enemigo > 0:
        vida_jugador = vida_jugador - ataque_enemigo
        print(f"¡el enemigo te ataco por {ataque_enemigo} puntos de daño!")


if vida_jugador > 0:
    print(f"\n¡VICTORIA! {nombre} ha ganado la batalla.")
else:
    print("\nDERROTA. Has caido en combate.")