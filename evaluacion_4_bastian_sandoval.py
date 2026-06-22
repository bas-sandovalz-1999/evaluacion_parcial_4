
def menu():
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Agregar estudiante")
    print("2. Buscar estudiante")
    print("3. Eliminar estudiante")
    print("4. Actualizar estados")
    print("5. Mostrar estudiantes")
    print("6. Salir")
    print("=====================================")

def validar_nombre(nombre):
    if nombre.strip() != "":
        return True
    else:
        return False
    
def validar_edad(edad: int):
    if edad > 0:
        return True
    else:
        return False
    
def validar_nota(nota: float):
    if 1.0 <= nota <= 7.0:
        return True
    else:
        return False

def agregar(lista):
    nombre = input("Ingrese el nombre del estudiante: ")
    if not validar_nombre(nombre):
        print("Nombre invalido")
        return
    try:
        edad = int(input("Ingrese la edad del estudiante: "))
        if not validar_edad(edad):
            print("Edad invalida, tiene que ser mayor a 0")
            return
    except ValueError:
        return "Error, debe ingresar un numero entero para la edad"
    
    try:
        nota = float(input("Ingrese la nota del estudiante: "))
        if not validar_nota(nota):
            print("Nota invalida, tiene que ser entre 1.0 y 7.0")
            return
    except ValueError:
        return "Error, debe ingresar un numero entre 1.0 y 7.0"
    
    aprobado = False
    estado = ""
    
    dictio = {
        "nombre":nombre.strip(),
        "edad":edad,
        "nota":nota,
        "aprobado":False,
        "estado":estado
        
    }
    
    lista.append(dictio)
  
def buscar(nombre_estudiante: str):
    posicion = 0
    for i in lista_estudiante:
        if i ["nombre"] == nombre_estudiante:
            print(f"Estudiante {nombre_estudiante} esta en la posicion {posicion+1}, de la lista")
            return posicion
        elif i ["nombre"] != nombre_estudiante:
            print("Nombre del estudiante no encontrado")
        posicion +=1

def eliminar(nombre_estudiante: str):
    posicion = 0
    for i in lista_estudiante:
        if i ["nombre"] == nombre_estudiante:
            lista_estudiante.pop(posicion)
            print(f"Estudiante: {nombre_estudiante}, eliminado de la lista")
        elif i ["nombre"] != nombre_estudiante:
            print("Nombre del estudiante no encontrado, no se puede eliminar de la lista")
        posicion +=1

def actualizar(lista):
    for i in lista:
        if i ["nota"] >= 4.0:
            lista[i]["aprobado"] = True
            lista[i]["estado"] = "Aprobado"
        else:
            lista[i]["aprobado"] = False
            lista[i]["estado"] = "Reprobado"

def mostrar(lista):
    print("Lista de estudiantes\n")
    for i in lista:
        print(f" Nombre: {i["nombre"]}\n",
              f"Edad: {i["edad"]}\n",
              f"Nota: {i["nota"]}\n",
              f"Estado: {i["estado"]}\n"
              )
    

lista_estudiante = []

while True:
    menu()
    try:
        opc = int(input("Ingrese la opcion que desea usar: "))
        if opc==1:
            agregar(lista_estudiante)
            
        elif opc==2:
            if len(lista_estudiante) == 0:
                print("No hay lista registrada")
            else:
                nombre = input("Ingrese el nombre del estudiante que quiere buscar: ").strip()
                buscar(nombre)
        
        elif opc==3:
            if len(lista_estudiante) == 0:
                print("No hay lista registrada")
            else:
                nombre = input("Ingrese el nombre del estudiante que quiere eliminar: ").strip()
                eliminar(nombre)
        
        elif opc==4:
            if len(lista_estudiante) == 0:
                print("No hay lista registrada")
            else:
                actualizar(lista_estudiante)
            
        elif opc==5:
            if len(lista_estudiante) == 0:
                print("No hay lista registrada")
            else:
                mostrar(lista_estudiante)
            
        elif opc==6:
            break
        
        elif opc==7:
            print(lista_estudiante)
    
        else:
            print("Opcion invalida")
    except:
        print("Ingrese un numero entero")
        
        