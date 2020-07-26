import random
# import string
# caracteres_con_import_string = string.digits + string.ascii_lowercase + string.ascii_uppercase

def generar_password():
    # Código ascii
    # numeros del 48 al 57
    numeros = tuple(range(48,58))
    # mayúsculas del 65 al 90
    mayusculas = tuple(range(65, 91))
    # minúsculas del 97 al 122
    minusculas = tuple(range(97, 123))

    caracteres_disponibles = numeros + mayusculas + minusculas
    password = []
    
    for i in range(16):
        codigo_ASCII_aleatorio = random.choice(caracteres_disponibles)
        password.append(chr(codigo_ASCII_aleatorio))
    
    password = ''.join(password)

    return password


def run():
    password = generar_password()
    print('Tu nuevo password es: ' + password)


if __name__ == "__main__":
    run()