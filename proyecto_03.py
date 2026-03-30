contactos = []

def ver_contactos():
    if len(contactos) == 0:
        print("No hay contactos guardados")
        return
    
    for i, contacto in enumerate(contactos):
        print(f"{i + 1}. Nombre: {contacto['nombre']} Telefono: {contacto['telefono']} Email: {contacto['email']}")

def agregar_contacto():
    nombre = input("ingrese el nombre del contacto agregar: ").lower()
    
    for contacto in contactos:
        if contacto["nombre"] == nombre:
            print(f"El contacto '{nombre}' ya existe.")
            return  # cancela, vuelve al menú
    
    # si llegó aquí es porque no encontró el nombre
    telefono = input("Teléfono: ")
    email = input("Email: ").lower()
    contactos.append({"nombre": nombre, "telefono": telefono, "email": email})
    print(f"Contacto '{nombre}' guardado correctamente.")

def buscar_contacto():
    contacto_buscar = input("ingrese el nombre del contacto que quiere buscar: ").lower()
    encontrado = False

    for contacto in contactos:
        if contacto["nombre"] == contacto_buscar:
            print(f"Nombre: {contacto['nombre']}")
            print(f"Telefono: {contacto['telefono']}")
            print(f"Email: {contacto['email']}")
            encontrado = True 
            break
    
    


    if not encontrado:
        print("Contacto no encontrado")  
        
    
def eliminar_contacto():
    contacto_eliminar = input("ingrese el nombre del contacto que quiere eliminar: ").lower()
    encontrado = False
    for contacto in contactos:
        if contacto["nombre"] == contacto_eliminar:
            contactos.remove(contacto)
            print("Contacto eliminado")
            encontrado = True
            break
     
    if not encontrado:
        print("Contacto no encontrado")  
        
    
while True:
    print()
    print("===== GESTOR DE CONTACTOS =====")
    print("1. Ver todos los contactos")
    print("2. Agregar contacto")
    print("3. Buscar contacto")
    print("4. Eliminar contacto")
    print("5. Salir")

    opcion = int(input("ingrese su opcion: "))

    if opcion == 1:
        print("CONTACTOS")
        ver_contactos()
    elif opcion == 2:
        print("AGREGAR CONTACTO")
        agregar_contacto()
    elif opcion == 3:
        print("BUSCAR CONTACTO")
        buscar_contacto()     
    elif opcion == 4:
        print("ELIMINAR CONTACTO")
        eliminar_contacto()
    elif opcion == 5:
        print("saliendo del programa, gracias...")
        break
    else:
        print("opcion no validad intenta de nuevo")