from src import string_utils, sorting_algos, search_algos, stats_lib

def text_processing_pipeline(words, target_word):
    # 1. String Utils: Convert all words to snake_case
    snake_case_words = [string_utils.to_snake_case(w) for w in words]
    
    # 2. String Utils: Filter out words that are not palindromes
    # Note: to_snake_case might introduce underscores, so palindrome check should handle that or we check original?
    # Let's check the snake_case version as per plan logic flow.
    palindromes = [w for w in snake_case_words if string_utils.is_palindrome(w)]
    
    # 3. Sorting: Sort the filtered list
    # merge_sort returns a new list
    sorted_palindromes = sorting_algos.merge_sort(palindromes)
    
    # 4. Search: Find the index of target_word (assumed to be in snake_case if passed correctly or we convert)
    # Let's assume target_word is passed in snake_case or we convert it.
    target_snake = string_utils.to_snake_case(target_word)
    index = search_algos.binary_search(sorted_palindromes, target_snake)
    
    # 5. Stats: Calculate the mean length of the sorted words
    lengths = [len(w) for w in sorted_palindromes]
    mean_length = stats_lib.mean(lengths)
    
    return index, mean_length
