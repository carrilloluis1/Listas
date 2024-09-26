lista_original = [1,4,5,6,7,6]

def cargar_valores(lista: list, total_agregar = 1) -> list:   
    
    '''Función que agrega nuevos datos a una lista ya existente
                    Recibe como parámetros: 
        lista y cantidad de datos que desea agregar'''

    agregar = [0] * total_agregar
    tipo_dato = type(lista[0])
    
    for i in range(total_agregar):
        dato = input("Que dato desea agregar?: ")
        
        if tipo_dato == int:
            agregar[i] = int(dato)
        elif tipo_dato == float:
            agregar[i] = float(dato)
        elif tipo_dato == str:
            agregar[i] = dato
        else:
            print("No es un tipo de dato valido")
            return lista

    lista_nueva = lista + agregar
    
    return lista_nueva

print(cargar_valores(lista_original))