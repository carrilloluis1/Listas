lista_horarios = [ 10, 15, 33, 8, 45, 16, 90, 19, 43, 54, 9, 32, 15, 6, 50, 19, 26, 65, 10, 18 ]
suma_total = 0

#A:
#Encuentro el 20% del total de datos de la lista
porcentaje_mayor = (len(lista_horarios) * 20) // 100

#Incializo la lista
lista_mayor = [0] * porcentaje_mayor

#Encuentro los 4 mayores de la lista
for i in range(porcentaje_mayor):
    
    for j in range(len(lista_horarios)):
        
        if i > 0 and lista_horarios[j] >= lista_mayor[i-1]:
            continue
        
        elif lista_horarios[j] > lista_mayor[i]:
            lista_mayor[i] = lista_horarios[j]

#Realizo la suma para el promedio 
for i in range(len(lista_mayor)):
    suma_total += lista_mayor[i]

#Saco el promedio
if porcentaje_mayor != 0:
    promedio = suma_total / porcentaje_mayor
else:
    promedio = 0

print(f'El promedio del 20% es: {promedio}')

#B:
suma_total = 0
for i in range(len(lista_horarios)):
    suma_total += lista_horarios[i]

promedio_total = suma_total / len(lista_horarios)
print(f'El promedio total es: {promedio_total}')

#C:
for i in lista_horarios:
    contador = 0
    for j in range(len(lista_horarios)):
        if i == lista_horarios[j]:
            contador += 1
    if contador > 1:
        print(f'El numero {i} se repite')

#D:
producto = 1
for i in lista_horarios:
    producto *= i

media_geometrica = (producto) ** 1/2

print(media_geometrica)

#E:
def recorrer_ascendente(lista_horarios):
    for i in range(len(lista_horarios)):
        print(lista_horarios[i])

def recorrer_descendente(lista_horarios):
    for i in range(len(lista_horarios)-1 , -1 , -1):
        print(lista_horarios[i])

recorrer_ascendente(lista_horarios)
recorrer_descendente(lista_horarios)