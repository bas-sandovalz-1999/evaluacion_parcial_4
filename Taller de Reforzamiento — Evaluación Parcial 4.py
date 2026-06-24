# Taller de Reforzamiento — Evaluación Parcial 4

lista_producto = []

def menu():
    while True:
        print("========== MENÚ PRINCIPAL ==========")
        print("1. Agregar producto")
        print("2. Buscar producto")
        print("3. Eliminar producto")
        print("4. Actualizar disponibilidad")
        print("5. Mostrar productos")
        print("6. Salir")
        print("=====================================")
        try:
            opc = int(input("Ingrese la opcion que desea realizar (1--2-3-4-5-6): "))
            if opc==1:
                agregar_producto(lista_producto)
            
            elif opc==2:
                buscar_producto(lista_producto)
            
            elif opc==3:
                eliminar_producto(lista_producto)
                
            elif opc==4:
                actualizar_producto(lista_producto)
            
            elif opc==5:
                mostrar_productos(lista_producto)
                
            elif opc==6:
                print("Saliendo del programa")
                break
            
            else:
                print("Opción inválida.")
                
        except ValueError:
            print("Error, ingrese una opcion valida en formato numero")


def agregar_producto(lista: list):
    nombre = input("Ingrese el nombre del producto: ").strip()
    if len(nombre)==0 or nombre.strip()=="":
        print("Nombre invalido, volviendo al menu")
        return
    
    if len(lista) > 0:
        for i in lista:
            if i["nombre"] == nombre:
                print("Producto ya registrado, ingrese otro producto, volviendo al menu")
                return
    
    try:
        stock = int(input("Ingrese la cantidad de unidades que hay en la bodega: "))
        if stock < 0:
            print("Debe ingresar una cantidad igual o mayor a 0, volviendo al menu: ")
            return
    except ValueError:
        print("Ingrese un valor valido para cantidad, volviendo al menu: ")
        return
    
    try:
        precio = float(input("Ingrese el precio del producto: "))
        if precio <= 0:
            print("Debe ingresar un precio mayor a 0, volviendo al menu")
            return
    except ValueError:
        print("Debe ingresar un precio valido, volviendo al menu")
        return
    
    disponible = False
    
    producto = {
        "nombre":nombre,
        "stock":stock,
        "precio":precio,
        "disponible":disponible
        }
    
    lista.append(producto)

def buscar_producto(lista: list):
    if len(lista) == 0:
        print("No hay productos registrados")
        return
    nombre_buscar = input("Ingrese el nombre del producto a buscar: ").strip()
    
    for i in lista:
        if i["nombre"] == nombre_buscar:
            print(f"Producto -{nombre_buscar}- encontrado: Cantidad: {i["stock"]}  Precio: {i["precio"]}")
            return i
    print(f"Producto -{nombre_buscar}- no encontrado")
    return

def eliminar_producto(lista: list):
    if len(lista) == 0:
        print("No hay productos registrados")
        return
    nombre_eliminar = input("Ingrese el producto a eliminar: ").strip()
    
    for i in lista:
        if i["nombre"] == nombre_eliminar:
            lista.remove(i)
            print(f"Producto {nombre_eliminar} eliminado de la bodega")
            return i
    print("Producto a eliminar no encontrado")
    return

def actualizar_producto(lista: list):
    if len(lista) == 0:
        print("No hay productos registrados")
        return
    print("Actualizando disponibilidad de los productos")
    for i in lista:
        if i["stock"] > 0:
            i["disponible"] = True
        else:
            i["disponible"] = False
    print("Estado de los productos actualizados")


def mostrar_productos(lista: list):
    if len(lista) == 0:
        print("No hay productos registrados")
        return
    else:
        for i in lista:
            print(f" [Nombre]: {i["nombre"]} - [Stock]: {i["stock"]} - [Precio]: {i["precio"]} [Estado]: {i["disponible"]}")
        
menu()
