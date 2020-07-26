def run():
    lista = ['hola',3,4.5,True]
    print(lista)
    lista.append("Buenas Tardes")
    print(lista)
    lista.pop(2)
    print(lista)
    print(lista[::-1])
    print(lista[1:3])


if __name__ == "__main__":
    run()