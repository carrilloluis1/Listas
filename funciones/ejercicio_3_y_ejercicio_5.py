cantidad_encuestados = input('Cuantos encuestas realizaras?: ')
cantidad_encuestados = int(cantidad_encuestados)

lista_nombres = [0] * cantidad_encuestados
lista_sexo = [0] * cantidad_encuestados
lista_horas = [0] * cantidad_encuestados
lista_ingreso_semanal = [0] * cantidad_encuestados

for i in range(cantidad_encuestados):
    lista_nombres[i] = input(f'Ingrese el nombre del encuestado numero {i + 1}: ')
    lista_sexo[i] = input(f'Ingrese el sexo del encuestado numero {i + 1}: ')
    lista_horas[i] = input(f'Ingrese las horas trabajadas del encuestado numero {i + 1}: ')
    lista_ingreso_semanal[i] = input(f'Ingrese el ingreso semanal del encuestado numero {i + 1}: ')

print(f'{lista_nombres} -- {lista_sexo} -- {lista_horas} -- {lista_ingreso_semanal}')

#5.
lista = input("Que lista desea modificar?: ")
posicion = int(input("En que posición esta el dato que desea modificar: "))
dato_nuevo = input("Que dato desea agregar?: ")

def modificar_listas(lista: list, posicion: int, dato_nuevo):
    lista[posicion] = dato_nuevo
    return lista

print(lista)
print(modificar_listas(lista,posicion,dato_nuevo))