def selectionSort(array, size):
   
    for step in range(size - 1):
        min_idx = step

        for i in range(step + 1, size):
         
            # to sort in descending order, change > to < in this line
            # select the minimum element in each loop
            if array[i] < array[min_idx]:
                min_idx = i

        # put min at the correct position
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
    else: return False







    # if sorted_lower_word_1 == sorted_lower_word_2:
    #     return True
    # else: return False

    # for letra_1 in first_string:
    #     aux = False
    #     for letra_2 in second_string:
    #         if letra_1 == letra_2:
    #             aux = True
        
    #     if aux == False:
    #         return False
    
    # return True
            
            
# https://stackoverflow.com/questions/319426/how-do-i-do-a-case-insensitive-string-comparison
