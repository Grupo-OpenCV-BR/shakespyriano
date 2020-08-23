import numpy as np
from random import randint


def GenerateSwearing():
    listwords = open(r'DataSet.txt').read()
    liststopwords = open(r'StopWords.txt').read()

    corpus = listwords.split()

    def make_pairs(corpus):
        for i in range(len(corpus)-1):
            yield (corpus[i], corpus[i+1])
            
    pairs = make_pairs(corpus)

    word_dict = {}

    for word_1, word_2 in pairs:
        if word_1 in word_dict.keys():
            word_dict[word_1].append(word_2)
        else:
            word_dict[word_1] = [word_2]
    
    first_word = np.random.choice(corpus)

    while first_word.islower():
        first_word = np.random.choice(corpus)

    chain = [first_word]

    n_words = randint(5,7)

    for i in range(n_words):
        if np.random.choice(word_dict[chain[-1]]) in chain:
            n_words += 1
        else:
            chain.append(np.random.choice(word_dict[chain[-1]]))

    while True:
        if chain[-1].lower() in liststopwords:
            chain.remove(chain[-1])
        else:
            break

    if ' '.join(chain).title()[-1] in ['?','.','!']:
        return(' '.join(chain).title())

    elif ' '.join(chain).title()[-1] in [',']:
        return(' '.join(chain).title()[:-1] + '.')

    else:
        return(' '.join(chain) + '.')

