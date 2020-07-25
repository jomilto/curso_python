def con_break():
    for i in range(0, 10000):
        if i == 100:
            break # corta el ciclo
        print(i)


def con_continue():
    for contador in range(1000):
        if contador % 2 != 0:
            continue # ya no ejecuta las siguientes lineas del codigo y va a la siguiente vuelta
        print(contador)


def otra_continue():
    texto = input("Escribe un texto: ")
    for letra in texto:
        if letra == "o":
            break
        print(letra)


def run():
    # con_continue()
    # con_break()
    otra_continue()
    # pass


if __name__ == "__main__":
    run()