def selectionSort(array, size):
    for step in range(size - 1):
        min_idx = step

        for i in range(step + 1, size):

            if array[i] < array[min_idx]:
                min_idx = i

        (array[step], array[min_idx]) = (array[min_idx], array[step])


def is_anagram(first_string, second_string):
    # case-insensitve
    lower_word_1 = first_string.lower()
    lower_word_2 = second_string.lower()

# ordenate
    a = list(lower_word_1)
    b = list(lower_word_2)
    selectionSort(a, len(a))
    selectionSort(b, len(b))

# comparison
    if a == b:
        return True
    else:
        return False
