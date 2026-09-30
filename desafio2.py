'''
Desafío B: Lista de promedios acumulados 
Se tiene una lista de calificaciones. Se debe recorrer con un for, acumular la suma en una variable, y guardar en una nueva lista el promedio acumulado (suma dividida entre la cantidad de elementos vistos hasta ese momento) en cada paso. Con notas = [10, 6, 8], la salida esperada es: 
[10.0, 8.0, 8.0]
 Código a completar: 
'''

notas = [10, 6, 8]
promedios = []
suma = 0

for i, nota in enumerate(notas):
    suma += nota
    promedios.append(suma / (i + 1))

print(promedios)
 	 
