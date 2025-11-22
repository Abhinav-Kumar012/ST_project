def is_palindrome(s):
    """Checks if a string is a palindrome."""
    if not isinstance(s, str):
        return False
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    return cleaned == cleaned[::-1]

def is_anagram(s1, s2):
    """Checks if two strings are anagrams."""
    if not isinstance(s1, str) or not isinstance(s2, str):
        return False
    
    cleaned1 = ''.join(c.lower() for c in s1 if c.isalnum())
    cleaned2 = ''.join(c.lower() for c in s2 if c.isalnum())
    
    return sorted(cleaned1) == sorted(cleaned2)

def levenshtein_distance(s1, s2):
    """Calculates the Levenshtein edit distance between two strings."""
    if not isinstance(s1, str) or not isinstance(s2, str):
        return None
        
    if len(s1) < len(s2):
        return levenshtein_distance(s2, s1)

    if len(s2) == 0:
        return len(s1)

    previous_row = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row
    
    return previous_row[-1]

def to_camel_case(s):
    """Converts snake_case string to CamelCase."""
    if not isinstance(s, str):
        return None
        
    components = s.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])

def to_snake_case(s):
    """Converts CamelCase string to snake_case."""
    if not isinstance(s, str):
        return None
        
    import re
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', s)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()

def count_vowels(s):
    """Counts the number of vowels in a string."""
    if not isinstance(s, str):
        return 0
        
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)

def reverse_words(s):
    """Reverses the order of words in a string."""
    if not isinstance(s, str):
        return None
        
    words = s.split()
    return ' '.join(reversed(words))

def longest_common_substring(s1, s2):
    """Finds the longest common substring between two strings."""
    m = [[0] * (1 + len(s2)) for _ in range(1 + len(s1))]
    longest, x_longest = 0, 0
    
    for x in range(1, 1 + len(s1)):
        for y in range(1, 1 + len(s2)):
            if s1[x - 1] == s2[y - 1]:
                m[x][y] = m[x - 1][y - 1] + 1
                if m[x][y] > longest:
                    longest = m[x][y]
                    x_longest = x
            else:
                m[x][y] = 0
                
    return s1[x_longest - longest: x_longest]
