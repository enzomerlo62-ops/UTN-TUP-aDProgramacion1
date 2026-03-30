usuario_guardado = "alumno"
clave_guardada = "python123"

intentos = 1
ingreso_exitoso = False

while intentos <= 3:
    print(f"--- Intento {intentos} de 3 ---")
    usuario_ingresado = input("Usuario: ")
    clave_ingresada = input("Clave: ")
    
    if usuario_ingresado == usuario_guardado and clave_ingresada == clave_guardada:
        print("Acceso concedido.")
        ingreso_exitoso = True
        break
    else:
        print("Error: credenciales inválidas.")
        intentos = intentos + 1

if ingreso_exitoso == False:
    print("Cuenta bloqueada")
else:
    opcion = ""
    while opcion != "4":
        print("\n1. Ver estado de inscripción")
        print("2. Cambiar clave")
        print("3. Mostrar mensaje ")
        print("4. Salir")
        
        opcion = input("Opción: ")
        
        if not opcion.isdigit():
            print("Error.")
        elif opcion == "1":
            print("inscripto")
        elif opcion == "2":
            nueva_clave = input("Nueva clave: ")
            while len(nueva_clave) < 6:
                print("Error: mínimo 6 caracteres.")
                nueva_clave = input("nueva clave: ")
            
            confirmacion = input("confirme la clave: ")
            if nueva_clave == confirmacion:
                clave_guardada = nueva_clave
                print("clave cambiada.")
            else:
                print("Error.")
        elif opcion == "3":
            
            print("no te rindas, si te recibis podes cobrar por hackear cuentas de insta.")
            
        elif opcion == "4":
            print("saliendo")
        else:
            print("Error.")