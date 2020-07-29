import string

def is_pangram(s):
    s = s.lower()
    for letter in string.ascii_lowercase:
        if s.count(letter) == 0:
            return False
    return True
