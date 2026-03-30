nombre = input("coloque el nombre del cliente por favor: ")

while not nombre.isalpha() or nombre == "": 
    print("Error")
    nombre = input("coloque el nombre del cliente por favor: ")

cant_productos = input("cantidad de productos: ")

while not cant_productos.isdigit() or int(cant_productos) <= 0:
    print("Error")
    cant_productos = input("cantidad de productos: ")

cantidad = int(cant_productos)
total_bruto = 0
total_final = 0

for i in range(1, cantidad + 1):
    print(f"\n---Producto {i}---")
    
    precio_producto = input("Precio: ")
    while not precio_producto.isdigit():
        print("Error")
        precio_producto = input("Precio: ")

    precio = int(precio_producto)
    total_bruto += precio

    
    descuento = input("¿Tiene descuento (S/N)?: ").lower()
   
    while descuento != "s" and descuento != "n":
        print("Error")
        descuento = input("¿Tiene descuento (S/N)?: ").lower()

    
    if descuento == "s":
        precio_con_dto = precio * 0.90
        total_final += precio_con_dto
    else:
        total_final += precio


ahorro = total_bruto - total_final
promedio = total_final / cantidad

print("\n================================")
print(f"TICKET PARA: {nombre.upper()}")
print(f"Total sin descuentos: ${total_bruto}")
print(f"Total con descuentos: ${total_final:.2f}")
print(f"Ahorro total: ${ahorro:.2f}")
print(f"Promedio por producto: ${promedio:.2f}")
print("================================")