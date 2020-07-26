def run():
    mi_diccionario = {
        'clave1': 1,
        'clave2': 2,
        'clave3': 3
    }
    print(mi_diccionario)
    print(mi_diccionario['clave1'])

    poblacion_paises = {
        'Argentina': 44938712,
	    'Brasil': 210147125,
	    'Colombia': 50372424 
    }

    # keys() o values() para obtener lo que se necesite
    # items cuando se necesiten los dos
    for pais, poblacion in poblacion_paises.items():
        print(pais + " -> " + str(poblacion) + " habitantes")

if __name__ == "__main__":
    run()