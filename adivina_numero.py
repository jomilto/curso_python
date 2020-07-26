import random


def run():
    numero_aleatorio = random.randint(1, 100)
    numero_usuario = int(input("Elige un número del uno al cien: "))
    while(numero_usuario != numero_aleatorio):
        if numero_usuario < numero_aleatorio:
            print("Elige un número es más grande")
        else: 
            print("Elige un número más pequeño")
        numero_usuario = int(input("Elige otro número: "))
    print("Ganaste!!")


if __name__ == "__main__":
    run()