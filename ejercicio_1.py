"""
El primer ejercicio trata de un algoritmo que implementa la busqueda recursiva en una lista ordenada, en este caso una 'tabla'
para encontrar un elemento especifico, en este caso el elemento 't'.
"""

def dicotomia(tabla,t):
    def dicotomia_recursiva(tabla, t, i, j):
        if i > j:
            return None
        else:
            m = (i + j) // 2
            if tabla[m] == t:
                return m
            elif tabla[m] < t:
                # t ∉ tabla[i..m–1] => tabla[m+1] ≤ t ≤ tabla[j] 
                return dicotomia_recursiva(tabla, t, m + 1, j)
            else:
                # t ∉ tabla[m+1..j] => tabla[i] ≤ t ≤ tabla[m–1] 
                return dicotomia_recursiva(tabla, t, i, m - 1)

    # Verificar si t está en el rango de búsqueda
    if tabla[0] <= t <= tabla[-1]:
        return dicotomia_recursiva(tabla, t, 0, len(tabla) - 1)
    else:
        return None  # AUSENTE
    
# Ejemplo de uso
tabla = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
t = 7
print(dicotomia(tabla, t))  # Salida: 6
