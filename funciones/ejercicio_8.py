def verificar_tipo (lista_1: list):
    
    tipo = type(lista_1[0])
    tipo_igual = True
    
    for i in range(len(lista_1)):
    
        if type(lista_1[i]) != tipo :
            tipo_igual = False
            break

    if tipo_igual == True:
        print(f'El tipó de dato de la lista es {tipo}')
    else:    
        print('La lista contiene elementos de diferente tipo')
        for i in lista_1:
            print(f'El elemento {i} es de tipo: {type(i)}')
    

lista = [5,2,3,"Hola"]

verificar_tipo(lista)