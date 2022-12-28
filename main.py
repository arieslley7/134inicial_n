import pytest


def imprimir_oi(nome):
    print(f'Hi, {nome}')


def somar(num_a,num_b):
    return num_a + num_b


def subtrair(num_a, num_b):
    return num_a + num_b


def multiplicar (num_a , num_b):
    return num_a * num_b


def dividir (num_a , num_b):
    try:
        return num_a / num_b
    except ZeroDivisionError:
        return'Não dividiras por zero'


if __name__ == '__main__':
    imprimir_oi('ArieslleySilva')

    resultado = somar(5 ,8)
    print(f'A soma : {resultado}')






