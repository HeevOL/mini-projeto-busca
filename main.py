import timeit
import random

def busca_sequencial_ordenada(uma_lista, item_pesquisado):
    pos = 0
    encontrou = False
    parar = False
    tamanho_lista = len(uma_lista)
    while pos < tamanho_lista and not encontrou and not parar:
        if uma_lista[pos] == item_pesquisado:
            encontrou = True
        else:
            if uma_lista[pos] > item_pesquisado:
                parar = True
            else:
                pos = pos+1
    return encontrou


def busca_binaria(uma_lista, item_pesquisado):
    inicio = 0
    fim = len(uma_lista)-1
    encontrou = False
    while inicio<=fim and not encontrou:
        meio = (inicio + fim)//2
        if uma_lista[meio] == item_pesquisado:
            encontrou = True
        else:
            if item_pesquisado < uma_lista[meio]:
                fim = meio-1
            else:
                inicio = meio+1
    return encontrou


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
    tamanho = int(input("Digite o tamanho da lista: "))
    qntd_testes = int(input("Digite quantas vezes deseja fazer o teste: "))
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
