def run():
    lista = ['hola',3,4.5,True]
    print(lista)
    lista.append("Buenas Tardes")
    print(lista)
    lista.pop(2)
    print(lista)
    print(lista[::-1])
    print(lista[1:3])
    lista_final = lista + ["nueva lista", 5, 7, 29]
    print(lista_final)
    print(lista*5)
    # tuplas, se recorren mucho más rápidas,
    # pero son inmutables, no se pueden modificar
    tupla = (1,2,3,4,5)
    print(tupla)


if __name__ == "__main__":
    run()