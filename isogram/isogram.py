def is_isogram(string):
    charset = []
    for char in string.lower():
        if char in charset:
            return False
        if char.isalpha():
            charset.append(char)
    return True
