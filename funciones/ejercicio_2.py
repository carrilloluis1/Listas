lista_edades = [26, 45, 33, 67, 53, 59, 19, 37, 41, 32]
lista_nombres =  ["Juan", "Matias", "Carla", "Susana", "Olivia", "Carlos", "Daniel", "Jimena", "Mariela", "Ignacio"]

#A
for i in range(len(lista_edades)):
    if i == 0:
        edad_maxima = lista_edades[i]
        nombre_maximo = lista_nombres[i]
        edad_minima = lista_edades[i]
        nombre_minimo = lista_nombres[i]
        
    elif lista_edades[i] > edad_maxima:
        edad_maxima = lista_edades[i]
        nombre_maximo = lista_nombres[i]
    
    elif lista_edades[i] < edad_minima:
        edad_minima = lista_edades[i]
        nombre_minimo = lista_nombres [i]

print(f'{nombre_maximo} es la persona con mayor edad {edad_maxima} años.')
print(f'{nombre_minimo} es la persona con menor edad {edad_minima} años.')

#B
for i in range(len(lista_edades)):
    if lista_edades[i] > 65:
        print('Encontramos uno mayor a 65 y termina el programa')
        break
    else:
        print('----------------')

else:
    print("No se encontraron mayores a 65")

#C
suma = 0
contador = 0

for i in range(len(lista_edades)):
    if lista_edades[i] < 40:
        continue
    
    suma += lista_edades[i]
    contador += 1

if contador != 0:
    promedio = suma / contador
else:
    promedio = 0

print(f'La media etaria para mayores de 40 es: {promedio}')