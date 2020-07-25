# Descartamos números de Carmichael
def comprobacion(numero):
    for i in range(1, 100):
        fermat = (2 ** (i - 1)) % i
        if fermat == 1:
            division = int(numero/i)
            resto = numero % i
            if resto == 0:
                return False
            if division <= i:
                return True


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


if __name__ == "__main__":
    run()