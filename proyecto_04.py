import json
class Libro:
    def __init__(self,titulo,autor,disponible=True):
        self.titulo = titulo
        self.autor = autor
        self.disponible = disponible

    def mostrar(self):
        estado = "Disponible" if self.disponible else "Prestado"
        print(f"Título: {self.titulo} | Autor: {self.autor} | Estado: {estado}")

class Biblioteca:
    def __init__(self):
        try:
            with open("libros.json", "r") as archivo:
                datos = json.load(archivo)
                self.libros = [
                    Libro(d["titulo"], d["autor"], d["disponible"])
                    for d in datos
                ]
        except FileNotFoundError:
            self.libros = []

    def guardar(self):
        datos = []
        for libro in self.libros:
                datos.append({
                    "titulo": libro.titulo,
                    "autor": libro.autor,
                    "disponible": libro.disponible
        })
        with open("libros.json", "w") as archivo:
            json.dump(datos, archivo)

    def agregar_libro(self):
        titulo = input("Ingrese el título: ").lower()
        autor = input("Ingrese el autor: ")

    
        for libro in self.libros:
            if libro.titulo.lower() == titulo:
                print("Ese libro ya existe.")
                return

    
        self.libros.append(Libro(titulo, autor))
        self.guardar()
        print("Libro guardado.")
        
    def mostrar_libros(self):

        if not self.libros:
            print("No hay libros registrados.")
        else:
            for i, libro in enumerate(self.libros, 1):
                print(f"{i}. ", end="")
                libro.mostrar()

    def prestar_libro(self):

        self.mostrar_libros()
        try:
            opcion = int(input("Número del libro: ")) - 1
            libro = self.libros[opcion]

            if not libro.disponible:
                print("El libro ya está prestado.")
            else:
                libro.disponible = False
                self.guardar()
                print("Libro prestado.")
        except (ValueError, IndexError):
            print("Opción no válida.")

    def devolver_libro(self):

        self.mostrar_libros()
        try:
            opcion = int(input("Número del libro: ")) - 1
            libro = self.libros[opcion]

            if libro.disponible:
                print("El libro no está prestado.")
            else:
                libro.disponible = True
                self.guardar()
                print("Libro devuelto.")
        except (ValueError, IndexError):
            print("Opción no válida.")
            
biblioteca = Biblioteca()

while True:
    print("\n===== BIBLIOTECA =====")
    print("1. Ver todos los libros")
    print("2. Agregar libro")
    print("3. Prestar libro")
    print("4. Devolver libro")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        biblioteca.mostrar_libros()
    elif opcion == "2":
        biblioteca.agregar_libro()
    elif opcion == "3":
        biblioteca.prestar_libro()
    elif opcion == "4":
        biblioteca.devolver_libro()
    elif opcion == "5":
        print("Datos guardados. ¡Hasta luego!")
        break
    else:
        print("Opción inválida, intente nuevamente.")