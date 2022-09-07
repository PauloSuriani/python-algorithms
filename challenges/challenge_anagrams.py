def selection_sort(array, size):
    for step in range(size - 1):
        min_idx = step

        for i in range(step + 1, size):

            if array[i] < array[min_idx]:
                min_idx = i

        (array[step], array[min_idx]) = (array[min_idx], array[step])


def ordena(lista):
    tamanho_da_lista = len(lista)
    lista_temporaria = [0] * tamanho_da_lista
    merge_sort(lista, lista_temporaria, 0, tamanho_da_lista - 1)


def merge_sort(lista, lista_temporaria, inicio, fim):
    if inicio < fim:
        meio = (inicio + fim) // 2
        merge_sort(lista, lista_temporaria, inicio, meio)

        merge_sort(lista, lista_temporaria, meio + 1, fim)

        merge(lista, lista_temporaria, inicio, meio + 1, fim)


def merge(lista, lista_temporaria, inicio, meio, fim):
    fim_primeira_parte = meio - 1
    indice_temporario = inicio
    tamanho_da_lista = fim - inicio + 1

    while inicio <= fim_primeira_parte and meio <= fim:
        if lista[inicio] <= lista[meio]:
            lista_temporaria[indice_temporario] = lista[inicio]
            inicio += 1
        else:
            lista_temporaria[indice_temporario] = lista[meio]
            meio += 1
        indice_temporario += 1

    while inicio <= fim_primeira_parte:
        lista_temporaria[indice_temporario] = lista[inicio]
        indice_temporario += 1
        inicio += 1

    while meio <= fim:
        lista_temporaria[indice_temporario] = lista[meio]
        indice_temporario += 1
        meio += 1

    for i in range(0, tamanho_da_lista):
        lista[fim] = lista_temporaria[fim]
        fim -= 1


def is_anagram(first_string, second_string):
    # case-insensitve
    lower_word_1 = first_string.lower()
    lower_word_2 = second_string.lower()

# ordenate
    a = list(lower_word_1)
    b = list(lower_word_2)
    # selectionSort(a, len(a))
    # selectionSort(b, len(b))
    ordena(a)
    ordena(b)

# comparison
    if a == b:
        return True
    else:
        return False

# https://www.programiz.com/dsa/selection-sort
# https://www.alura.com.br/artigos/algoritmo-mergesort-implementar-python?gclid=Cj0KCQjwguGYBhDRARIsAHgRm4-xKGDDxdMbwvaBqjiyVlWN4hAetnRchbeF4tIsngJaprW3xZ6q6m4aAnyPEALw_wcB
