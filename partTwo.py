
# words.py
def print_upper_words(words):
    """Print each word on a separate line in uppercase."""
    for word in words:
        print(word.upper())

print_upper_words(["hello", "world", "python", "is", "awesome"])

# words.py
def print_upper_words(words):
    """
    Print each word on a separate line in uppercase.
    
    Args:
    words (list of str): List of words to print in uppercase.
    """
    for word in words:
        print(word.upper())

print_upper_words(["hello", "world", "python", "is", "awesome"])

# words.py
def print_upper_words(words):
    """
    Print each word on a separate line in uppercase if it starts with 'e'.
    
    Args:
    words (list of str): List of words to print in uppercase.
    """
    for word in words:
        if word.lower().startswith('e'):
            print(word.upper())


print_upper_words(["hello", "world", "elephant", "is", "awesome", "Everest"])

# words.py
def print_upper_words(words, must_start_with):
    """
    Print each word on a separate line in uppercase if it starts with any of the specified letters.
    
    Args:
    words (list of str): List of words to print in uppercase.
    must_start_with (set of str): Set of letters the words must start with to be printed.
    """
    for word in words:
        if word[0].lower() in must_start_with:
            print(word.upper())


print_upper_words(["hello", "hey", "goodbye", "yo", "yes"], must_start_with={"h", "y"})