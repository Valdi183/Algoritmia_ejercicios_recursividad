"""
Este ejercicio contiene un script con una serie de algoritmos para analizar si una palabra es o no un palindromo
para ello, hay varios algoritmos que se encargan de transformar cualquier cadena, y posteriormente analizarla y
de esta forma poder concluis si se trata de un palindromo o no.
"""

"""
Este primer algoritmo recibe una cadena de caracteres (str) como entrada, y el algoritmo itera sobre esa cadena de caracteres
para verificar si los caracteres son alfanumericos o no. Aquellos que lo sean, seran alamcenados en la nueva cadena que es la
salida del algoritmo.
"""
def alfanumerico(ca):
    return ''.join(caracter for caracter in ca if caracter.isalnum())

"""
Este otro algoritmo recibe una cadena de caracteres como entrada al igual que la anterior, y la intención, es transformar los caracteres
acentuados y sustituirlos por los caracteres sin acentuar. El algoritmo devuelve la cadena resultante tras haber sustituido los caracteres
acentuados, por estos mismos sin acentuar
"""
def sin_acento(ca):
    MAYUSCULAS_ACCENTUADAS = 'ÁÉÍÓÚÜ'
    MAYUSCULAS = 'AEIOUU'
    
    return ''.join(MAYUSCULAS[MAYUSCULAS_ACCENTUADAS.find(caracter)] if caracter in MAYUSCULAS_ACCENTUADAS else caracter for caracter in ca)

"""
Este ultimo algoritmo, toma como entrada las cadenas de caracteres ( las frases definidas a continuación de forma global) y utiliza 
el .uuper() para convertir en mayusculas, y llama resto de algoritmos definidos para terminar de transformar la palabra. De esta forma,
si al darla la vuelta a los caracteres, estos coinciden con los caracteres originales, verificamos que estamos ante un palindromo.
El algortimo devuelve un booleano: 'True' si es palindromo, 'False' si no lo es.
"""
def palindromo(frase):
    ca = frase.upper() 
    ca = alfanumerico(ca)  
    ca = sin_acento(ca) 
    return ca == ca[::-1]  


# Ejemplo de uso con las frases dadas
frases = [
    "Dábale arroz a la zorra el abad",
    "Logré ver gol",
    "Salas",
    "1754571",
    "10000000000000000001",
    "Oso",
    "Palíndromo",
    "Osaba"
]
# Muestra en pantalla que palabras son palindromos y cuales no lo son
for frase in frases:
    if palindromo(frase):
        print(f'"{frase}" es un palíndromo.')
    else:
        print(f'"{frase}" no es un palíndromo.')