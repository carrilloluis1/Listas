nombres = ["Ana", "Luis", "Juan", "Sol", "Roberto", "Sonia", "Ulises", "Sofia", "Maria", "Pedro", "Antonio", "Eugenia", "Soledad", "Mario", "Maricela"]

edades = [23,45,34,23,46,23,45,67,37,68,25,55,45,27,43]

def busqueda_personas(edades: list):

    edad_menor = edades[0]

    for i in range(len(edades)):
        if edades[i] < edad_menor:
            edad_menor = edades[i]
        
        if edades[i] == edad_menor:
            print(f'{nombres[i]} tiene {edades[i]} años.')


busqueda_personas(edades)

