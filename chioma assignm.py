import string

def is_pangram(s):
    alphabet = string.ascii_lowercase
    s = s.lower()
    print (alphabet)
    print (s)

    sentence = []

    for char in s:
        if char.letters() and char not in sentence:
            sentence.append(char)
    
    # Check if we found all 26 letters
    for letter in alphabet:
        if letter not in sentence:
            return False
    
    return True

is_pangram("The quick brown fox jumps over the lazy dog")

