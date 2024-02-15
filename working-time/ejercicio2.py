#2. Crear una lista con 5 elementos y luego aplica los siguientes
#accionables:
#↪ Imprimir el último elemento
#↪ Modificar el valor del tercer elemento
#↪ Agregar dos elementos
#↪ Eliminar algún elemento
#● Guardar en un archivo llamado ejercicio2.py

frutas = ["manzana", "naranja", "pera", "durazno","mandarina"]

ultimo_elemento = frutas[4]
print(ultimo_elemento)

frutas[2] = "uva"
print(frutas[2])

frutas.append("banana")
frutas.append("ciruela")

print(frutas)

elemento_eliminado = frutas.remove("naranja")

print(frutas)