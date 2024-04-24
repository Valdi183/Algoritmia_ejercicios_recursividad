"""
El primer ejercicio trata de un algoritmo que implementa la busqueda recursiva en una lista ordenada, en este caso una 'tabla'
para encontrar un elemento especifico, en este caso el elemento 't'.
"""

"""
Esta es la función principal, que toma como entrada una lista de elementos llamada tabla y un elemento t que decide el usuario
(la tabla  que toma como entrada es una lista de elementos cualquiera, que en este caso esta definida de forma global con elementos
que van del 1 al 10. Pero el algoritmo esta hecho para cualquier numero de elementos, por eso se nombran a los elementos como i o
j...) La función devuelve la posición que ocupa el elemento en la tabla. si no se encontrase, devolveria la posición 'None'
"""
def dicotomia(tabla,t):
    # Esta funcion dentro de la funcion principal, es la que realiza la busqueda de forma recursiva
    def dicotomia_recursiva(tabla, t, i, j):
        if i > j:
            return None
        else:
            m = (i + j) // 2
            if tabla[m] == t:
                return m
            elif tabla[m] < t:
                # t ∉ tabla[i..m–1] => tabla[m+1] ≤ t ≤ tabla[j] ----- Seria el planteamiento del algoritmo en pseudocodigo
                return dicotomia_recursiva(tabla, t, m + 1, j)
            else:
                # t ∉ tabla[m+1..j] => tabla[i] ≤ t ≤ tabla[m–1]  ----- Seria el planteamiento del algoritmo en pseudocodigo
                return dicotomia_recursiva(tabla, t, i, m - 1)

    # Verifica si t esta en el rango de búsqueda
    if tabla[0] <= t <= tabla[-1]:
        return dicotomia_recursiva(tabla, t, 0, len(tabla) - 1)
    else:
        return None  # Cuando el elemento no se encuentra

# Ejemplo de uso (elaborado para una tabla de 10 elementos)
tabla = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
t = int(input("Introduzca un numero entero del 1 al 10: "))
indice = dicotomia(tabla, t)
print(f"El valor {t} se encuentra en la posición {indice} de la tabla.")