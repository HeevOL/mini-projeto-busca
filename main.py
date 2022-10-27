import timeit
import random

from buscas import *

def printar():
    print("-------------------------")

def teste_desempenho_otimizado():
    if len(lista) < 128:
        busca_sequencial_ordenada(lista, valor_aleatorio())
    else:
        busca_binaria(lista, valor_aleatorio())


def teste_desempenho_sequencial():
    busca_sequencial_ordenada(lista, valor_aleatorio())


def teste_desempenho_binario():
    busca_binaria(lista, valor_aleatorio())


def valor_aleatorio():
    return random.randint(0, tamanho*2)
    


try:
    printar()
    tamanho = int(input("Digite o tamanho da lista: "))
    printar()
    qntd_testes = int(input("Digite quantas vezes deseja fazer o teste: "))
    printar()
    lista = list(range(tamanho))

    print()
    tempo_seq = timeit.timeit(stmt=teste_desempenho_sequencial, number=qntd_testes)
    print(f"Desempenho sequencial: {tempo_seq}, tempo médio de testes: {tempo_seq/qntd_testes}\n")

    tempo_bin = timeit.timeit(stmt=teste_desempenho_binario, number=qntd_testes)
    print(f"Desempenho binario: {tempo_bin}, tempo médio de testes: {tempo_bin/qntd_testes}\n")

    tempo_oti = timeit.timeit(stmt=teste_desempenho_otimizado, number=qntd_testes)
    print(f"Desempenho otimizado: {tempo_oti}, tempo médio de testes: {tempo_oti/qntd_testes}\n")

except:
    print("Os valores de tamanho e quantidade de teste devem ser inteiros positivos.")