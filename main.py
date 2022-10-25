import timeit

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


def teste_desempenho():
    if length < 128:
        print(busca_sequencial_ordenada(lista, search))
    else:
        print(busca_binaria(lista, search))


def teste_desempenho_sequencial():
    lista_teste = list(range(tamanho))
    print(busca_sequencial_ordenada(lista_teste, search))


def teste_desempenho_binario():
    lista_teste = list(range(tamanho))
    print(busca_binaria(lista_teste, search))


op = None
while op != 'n':
    lista = []

    if op == 'a':
        tamanho = int(input("digite o tamanho da lista: "))
        search = int(input("Digite o valor a ser procurado: "))
        tempo = timeit.timeit(stmt=teste_desempenho_sequencial, number=1)
        print("desempenho sequencial: ", tempo)
        tempo = timeit.timeit(stmt=teste_desempenho_binario, number=1)
        print("desempenho binario: ", tempo)

    else: 
        data = input("Digite o valor inicial, tamanho e incremento: ").split()
        init = int(data[0])
        length = int(data[1])
        increment = int(data[2])

        for i in range(length):
            lista.append(init+(increment*i))

        search = int(input("Digite o valor q deseja procurar na lista: "))
        tempo = timeit.timeit(stmt=teste_desempenho, number= 1)
    
    print("Tempo de execução: ", tempo)
    tempo = timeit._Timer = 0
    op = input("continuar? 's' ou 'n': ")
