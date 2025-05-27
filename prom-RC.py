def calcular_promedio(numeros):
    """
    Calcula el promedio de una lista de números.

    Parámetros:
    numeros (list of float or int): Lista de números a promediar.

    Retorna:
    float: El promedio de los números en la lista.

    Lanza:
    ValueError: Si la lista está vacía.
    """
    if not numeros:
        raise ValueError("La lista de números no puede estar vacía.")
    
    return sum(numeros) / len(numeros)
