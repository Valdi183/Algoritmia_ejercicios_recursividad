"""
En este ejercicio, consideramos un conjunto de n fichas de colores. El objetivo es organizar las fichas en tres series de fichas 
del mismo color: primero fichas rojas, luego fichas verdes y después fichas azules.

El algoritmo utiliza una técnica conocida como "Algoritmo de bandera" y se basa en la idea de Dijkstra.

1. HIPÓTESIS:
-Las fichas están divididas en cuatro subconjuntos: Rojo (S1), Verde (S2), No ordenadas (S3) y Azul (S4).
-Las series S1, S2 y S4 ya están parcialmente organizadas, mientras que la serie S3 contiene las fichas que aún no se han colocado.
-Se establecen tres afirmaciones:
    (A1) : Las fichas de 1 hasta i (i ≥ 0) son de color Rojo.
    (A2) : Las fichas de i+1 hasta j (j ≥ i) son de color Verde.
    (A3) : Las fichas de k+1 hasta n (k < n) son de color Azul.

2. VARIANTE DE CONTROL
-La cantidad de fichas que todavía no se han colocado: k - j.

3. ALGORITMO DE PERMUTACIÓN:
-El algoritmo realiza permutaciones para organizar las fichas.
-Mueve una ficha desde la serie S3 (fichas sin ordenar) a la serie correspondiente (S1, S2 o S4) según su color.
-Realiza permutaciones hasta que todas las fichas estén ordenadas.
"""


"""
Este Mueve la ficha a la posición `j+1` en la serie de su color.
"""
def permutar(fichas, i, j, k, n):
    if k != j:
        color = fichas[j]  # Observar el color de la ficha en la posición j+1
        if color == 'R':
            # Si la ficha es roja, la intercambia con la ficha Verde que ocupa la posición i+1
            fichas[i], fichas[j] = fichas[j], fichas[i]
            permutar(fichas, i+1, j+1, k, n)
        elif color == 'V':
            # Si la ficha es verde, esta está en su lugar y la serie S2 se extiende desde i+1 hasta j+1
            permutar(fichas, i, j+1, k, n)
        elif color == 'B':
            # Si la ficha es Azul: la intercambia con la ficha de la posición k
            fichas[j], fichas[k] = fichas[k], fichas[j]
            permutar(fichas, i, j, k-1, n)

# Algoritmo principal
def bandera(fichas):
    n = len(fichas)
    permutar(fichas, 0, 0, n-1, n)
    return fichas

# Ejemplo de uso
fichas = list("VVRRRVBBVBRRRBBR")
ordenadas = bandera(fichas)
print("Fichas ordenadas:", "".join(ordenadas))