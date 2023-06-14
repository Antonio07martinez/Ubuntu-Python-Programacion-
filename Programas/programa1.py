"""
    * Pide al usuario que ingrese un número inicial y un número final que delimiten el rango.
    * Crea un bucle que recorra cada número dentro del rango especificado.
    * Dentro del bucle, verifica si el número actual es primo o no.
    * Para determinar si un número es primo, puedes utilizar otro bucle que compruebe si el número es divisible por algún número entre 2 y su raíz cuadrada (ambos inclusive). Si se encuentra un divisor, el número no es primo.
    * Si el número actual es primo, imprímelo o guárdalo en una lista.
    * Al finalizar el bucle, muestra los números primos encontrados al usuario.
"""
def Primo(lista,resta):
    i = 0
    while()
    print(f"Lista de primos: {listaPrimos}")

def Cadena(numeroInicial, numeroFinal):
    if numeroFinal < numeroInicial: 
        print(f"Error de dato, tu número final debe ser mayor a tu numero inicial")
    else: 
        resta = numeroFinal - numeroInicial
        print(f"La diferenncia entre numero es: {resta}")
        i,lista = 0,[]
        while i <= resta:
            lista.append(numeroInicial)
            numeroInicial = numeroInicial+1
            i = i+1
        Primo(lista,resta)
        print(f"Lista {lista}")

        

Cadena(int(input("Coloca tu numero incial en entero: ")),int(input("Coloca tu numero final en entero: ")))
