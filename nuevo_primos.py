# Descartamos números de Carmichael (numeros compuestos por otros números primos)
def comprobacion(numero):
    for i in range(1, 1000000):
        fermat = (2 ** (i - 1)) % i
        if fermat == 1:
            division = int(numero/i)
            resto = numero % i
            if division <= i:
                return True
            if resto == 0:
                return False


# Por teorema de Fermat para números primos
def es_primo(numero):
    fermat = (2 ** (numero - 1)) % numero
    if fermat == 1 or numero == 2:
        return comprobacion(numero)
    else:
        return False


def run():
    numero = int(input("Escribe un número entero: "))
    if es_primo(numero):
        print("Es primo")
    else:
        print("No es primo")

    # encuentra hasta el 9497 en un for del 1 al 9,498
    # preguntando si es primo hasta ahora con el 990,000,023


if __name__ == "__main__":
    run()