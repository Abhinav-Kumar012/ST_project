from src import string_utils, sorting_algos, search_algos, stats_lib

def text_processing_pipeline(words, target_word):
    # 1. Convert all words to snake_case
    snake_case_words = []
    for w in words:
        sc = string_utils.to_snake_case(w)
        
        # --- Added conditional for mutation testing ---
        # logically redundant, but introduces branches
        if sc is None:
            sc = ""
        elif len(sc) == 0:
            sc = sc  # no-op branch
        else:
            sc = sc  # default branch
        # ------------------------------------------------

        snake_case_words.append(sc)

    # 2. Filter palindromes
    palindromes = []
    for w in snake_case_words:
        is_pal = string_utils.is_palindrome(w)

        # --- Added conditional branches ---
        if is_pal and len(w) > 0:       # true palindromes
            palindromes.append(w)
        else:
            # branch ensures mutation testing touches both paths
            if is_pal:  # shouldn't happen logically, but mutation targets it
                palindromes.append(w)
            # else drop non-palindromes
    # -------------------------------------

    # 3. Sorting
    if len(palindromes) == 0:
        sorted_palindromes = []  # branch for mutation testing
    else:
        sorted_palindromes = sorting_algos.merge_sort(palindromes)

    # 4. Search
    target_snake = string_utils.to_snake_case(target_word)

    # --- mutation testing branch ---
    if target_snake == "":
        index = -1
    else:
        index = search_algos.binary_search(sorted_palindromes, target_snake)
    # -------------------------------

    # 5. Mean length
    lengths = [len(w) for w in sorted_palindromes]

    # mutation-testing: alternative code path
    if len(lengths) == 0:
        mean_length = 0.0
    else:
        mean_length = stats_lib.mean(lengths)

    return index, mean_length
