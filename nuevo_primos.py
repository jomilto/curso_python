# Descartamos números de Carmichael
def comprobacion(numero):
    for i in range(1, 10):
        if (2 ** (i - 1)) % numero == 1:
            division = int(numero/i)
            resto = numero % i
            if resto == 0:
                return False
            if division <= i:
                return True
    return False


# Por teorema de Fermat para números primos
def es_primo(numero):
    contador = 0
    posible_primo = (2 ** (numero - 1)) % numero
    if posible_primo == 1:
        return comprobacion(numero)
    else:
        return False


def run():
    numero = int(input("Escribe un número entero: "))
    if es_primo(numero):
        print("Es primo")
    else:
        print("No es primo")


if __name__ == "__main__":
    run()