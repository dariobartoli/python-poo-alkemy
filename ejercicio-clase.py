#Consigna: ✍️
#Crear un pequeño programa que realice una función aritmética que permita al usuario ingresar datos por la terminal acorde a distintas opciones.  
#Para ellos debemos definir una función que reciba parámetros:
#Combinar funciones nativas y funciones definidas,
#condicionales, y bucles.
#Si el usuario ingresa el nro 1, realiza la acción A.
#Si el usuario ingresa el nro 2, realiza la acción B.

usuario = {
    "nombre": "Alan",
    "apellido": "Zalazar",
    "edad": 28,
    "dinero": 4569,
    "gastos": (453, 234, 234, 1234)
}



print("Hola, Para solicitar sus datos ingrese 1, para solicitar la suma de sus gastos en el mes ingrese 2")
numero = input("Por favor, ingrese el numero aqui: ")


def solicitarDatos(num):
    if(num == "1"):
        print("Tu informacion de usuario es la siguiente:")
        print(usuario.items())
    elif(num == "2"):
        gastos = usuario["gastos"]
        suma_gastos = 0
        for gasto in gastos:
            suma_gastos += gasto
        print(f'Tu total de gastos en el mes es de: {suma_gastos}')
    else:
        nuevo_numero =input("Numero ingresado incorrecto, intente nuevamente con 1 o 2: ")
        solicitarDatos(nuevo_numero)

        

solicitarDatos(numero)