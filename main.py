import timeit
import random
from math import floor
from buscas import *

def printar():
    print("-------------------------------------------------")


def teste_desempenho_hibrido():
    for valor in valores:
        if len(lista) <= 128:
            busca_sequencial_ordenada(lista, valor)
        else:
            lista_fatiada = busca_binaria(lista, valor, hibrida=128)
            if isinstance(lista_fatiada, list):
                busca_sequencial_ordenada(lista_fatiada, valor) 


def teste_desempenho_sequencial():
    for valor in valores:
        busca_sequencial_ordenada(lista, valor)


def teste_desempenho_binario():
    for valor in valores:
        busca_binaria(lista, valor)


def valores_aleatorios():
    valores = []
    for i in range(qntd_testes):
        valores.append(random.randint(0, floor(tamanho*1.25)))
    return valores


try:
    printar()
    tamanho = int(input("Digite o tamanho da lista: "))
    printar()
    qntd_testes = int(input("Digite quantas vezes deseja fazer o teste: "))
    printar()
    lista = list(range(tamanho))
    valores = valores_aleatorios()

    print()
    tempo_seq = timeit.timeit(stmt=teste_desempenho_sequencial, number=1)
    print(f"Desempenho sequencial: {tempo_seq:.6f} segundos, tempo médio: {(tempo_seq/qntd_testes):.6f} segundos.\n")

    tempo_bin = timeit.timeit(stmt=teste_desempenho_binario, number=1)
    print(f"Desempenho binário: {tempo_bin:.6f} segundos, tempo médio: {(tempo_bin/qntd_testes):.6f} segundos.\n")

    tempo_hib = timeit.timeit(stmt=teste_desempenho_hibrido, number=1)
    print(f"Desempenho híbrido: {tempo_hib:.6f} segundos, tempo médio: {(tempo_hib/qntd_testes):.6f} segundos.\n")

except:
    print("Os valores de tamanho e quantidade de teste devem ser inteiros positivos.")