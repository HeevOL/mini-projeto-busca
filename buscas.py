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


