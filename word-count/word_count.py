import re

def count_words(sentence):
    word_counts = {}
    words = normalize(sentence)

    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    return word_counts

def normalize(sentence):
    normalized_words = []
    words = re.split('[\s,_]', sentence)
    for word in words:
        normal_word = ''
        for char in word:
            if char == word[0] or char == word[-1]:
                if char.isalpha() or char.isnumeric():
                    normal_word += char
            elif char.isalpha() or char.isnumeric() or char == '\'':
                normal_word += char
        if normal_word != '':
            normalized_words.append(normal_word.lower())

    return normalized_words
