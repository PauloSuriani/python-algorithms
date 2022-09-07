def is_palindrome_recursive(word, low_index, high_index):
    if not word or word == '':
        return False

    # condição de parada:
    if low_index >= high_index:
        return True

    if word[low_index] == word[high_index]:
        return is_palindrome_recursive(word, low_index + 1, high_index - 1)
    else:
        return False
