# 6 
limite_menor = int(input("Ingrese el limite menor: "))
limite_mayor = int(input("Ingrese el limite mayor: "))

def solicitar_numeros(limite_menor, limite_mayor):
    
    lista_numeros = [0] * 10
    
    for i in range (len(lista_numeros)):
        lista_numeros[i] = int(input("Ingrese el numero: "))
        while lista_numeros[i] < limite_menor or lista_numeros[i] > limite_mayor:
            lista_numeros[i] = int(input("error!! Reingrese el numero: "))
    
    return lista_numeros

#Llamada a la función

numeros_final = solicitar_numeros(limite_menor, limite_mayor)
print(f'La lista de los numeros correcto es: {numeros_final}')