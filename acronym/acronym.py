import string

def abbreviate(words):
    acronym = ""
    words = words.translate(str.maketrans({'-': ' ', '_': ' '}))
    for i in range(len(words.split())):
        acronym += words.split()[i][0]
    return acronym.translate(str.maketrans('', '', string.punctuation)).upper()
