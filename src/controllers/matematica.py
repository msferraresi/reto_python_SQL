import functools
from math import gcd

def MinimoComunMultiplo(listNumbers):
    numbersArr = [int(i) for i in listNumbers.split(',')]
    resultado = 0
    for num in numbersArr:
        resultado = gcd(resultado, num)
    return resultado

def Agregar(number):
    return int(number) + 1