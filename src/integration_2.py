from src import string_utils, sorting_algos, search_algos, stats_lib


def text_processing_pipeline(words, target_word):
    snake_case_words = []
    for w in words:
        sc = string_utils.to_snake_case(w)

        if sc is None:
            sc = ""
        elif len(sc) == 0:
            sc = sc
        else:
            sc = sc

        snake_case_words.append(sc)

    palindromes = []
    for w in snake_case_words:
        is_pal = string_utils.is_palindrome(w)

        if is_pal and len(w) > 0:
            palindromes.append(w)
        else:
            if is_pal:
                palindromes.append(w)

    if len(palindromes) == 0:
        sorted_palindromes = []
    else:
        sorted_palindromes = sorting_algos.merge_sort(palindromes)

    target_snake = string_utils.to_snake_case(target_word)

    if target_snake == "":
        index = -1
    else:
        index = search_algos.binary_search(sorted_palindromes, target_snake)

    lengths = [len(w) for w in sorted_palindromes]

    if len(lengths) == 0:
        mean_length = 0.0
    else:
        mean_length = stats_lib.mean(lengths)

    return index, mean_length
