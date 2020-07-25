def palindromo(palabra):
    palabra = palabra.replace(" ","")
    palabra = palabra.lower()
    return palabra == palabra[::-1]

# Función inicial
def run():
    palabra = input("Escribe una palabra: ")
    es_palidromo = palindromo(palabra)
    if es_palidromo:
        print("Es palindromo")
    else:
        print("No es palindromo")


# Punto de entrada para cargar el programa
if __name__ == '__main__':
    run()