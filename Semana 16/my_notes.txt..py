# Programa para crear, escribir y leer un archivo de texto
# Autor: Yoshira Noa
# Fecha: 04/04/2025

def main():
    # 1. Crear un nuevo archivo y escribir notas personales
    print("Creando y escribiendo en el archivo 'my_notes.txt'...")

    # Abrimos el archivo en modo escritura ('w')
    # Si el archivo no existe, se creará automáticamente
    with open('my_notes.txt', 'w') as archivo:
        # Escribimos al menos tres líneas de notas personales
        archivo.write("Nota 1: Recordar comprar ingredientes para la cena del viernes.\n")
        archivo.write("Nota 2: Llamar al doctor para confirmar la cita del próximo mes.\n")
        archivo.write("Nota 3: Revisar el informe final antes de enviarlo al cliente.\n")

    print("Archivo creado exitosamente.\n")

    # 2. Leer el archivo línea por línea
    print("Leyendo el contenido del archivo 'my_notes.txt':")

    # Abrimos el archivo en modo lectura ('r')
    with open('my_notes.txt', 'r') as archivo:
        # Leemos el contenido línea por línea
        linea = archivo.readline()
        contador = 1

        # Mientras haya líneas para leer
        while linea:
            print(f"Línea {contador}: {linea.strip()}")
            linea = archivo.readline()
            contador += 1

    print("\n¡Operaciones completadas con éxito!")


# Ejecutamos la función principal
if __name__ == "__main__":
    main()