"""Viterbi Algorithm for inferring the most likely sequence of states from an HMM.

Eric Rios Soderman & Wafiakmal Miftah, 2022
"""

import nltk
import numpy as np
from viterbi import viterbi

# Importing Training Corpus (The Big Corpus)
training_corpus = nltk.corpus.brown.tagged_sents(tagset="universal")[:10000]
training_corpus_lower = [
    [(word.lower(), tag) for word, tag in sent] for sent in training_corpus
]
trainlist = []
for i in training_corpus_lower:
    for j in i:
        trainlist.append(j)
        pass
    pass

# Grabbing words
corplist_words = [(tag[0]) for tag in trainlist]

# Grabbing tag
corplist_tag = [tag[1] for tag in trainlist]

# Checking unique words in corpus
corplist_words_set = list(set(corplist_words))
corplist_words_set.append("UNK")  # Adding Unknown Words

# Checking unique tag in corpus
corplist_tag_set = list(set(corplist_tag))

# Importing Test Sentences
test_corpus = nltk.corpus.brown.tagged_sents(tagset="universal")[10150:10151]
test_corpus_lower = [
    [(word.lower(), tag) for word, tag in sent] for sent in test_corpus
]
testlist = []
for a in test_corpus_lower:
    for b in a:
        testlist.append(b)
        pass
    pass
testlist_words = [tag[0] for tag in testlist]

# Editing Input from string to number | Based on unique list of words
numbered_input = []
for word in testlist_words:
    if word not in corplist_words_set:
        numbered_input.append(len(corplist_words_set))
        pass
    else:
        numbered_input.append((corplist_words_set.index(word)))
        pass
    pass

# Function to help emission / observation matrix
def word_tag(w1, w2, corpus=trainlist):
    dictword = []
    dictall = []
    for i in corpus:
        if i[0] == w1:
            dictall.append(i)
            pass
        else:
            pass
        pass
    if len(dictall) == 0:
        dictall.append(1)
        dictword.append(1)
        pass
    else:
        for j in dictall:
            if j[1] == w2:
                dictword.append(j)
                pass
            else:
                pass
            pass
    return (len(dictword), len(dictall))


# Create the emission matrix
words_matrix = np.ones((len(corplist_words_set), len(corplist_tag_set)), dtype="float32")

prob_matrix = np.zeros((len(corplist_words_set), len(corplist_tag_set)), dtype='float32')
for a, t1 in enumerate(corplist_words_set):
    for b, t2 in enumerate(corplist_tag_set):
        prob_matrix[a, b] = words_matrix[a, b] / np.sum(words_matrix[a, :])

# Function to help transition matrix
def t2_given_t1(t2, t1, corpus=trainlist):
    tags = []
    for i in corpus:
        tags.append(i[1])
    count_t1 = len([t for t in tags if t == t1])
    count_t2_t1 = 0
    for index in range(len(tags) - 1):
        if tags[index] == t1 and tags[index + 1] == t2:
            count_t2_t1 += 1
    return (count_t2_t1, count_t1)


# Making pos matrix
tags_matrix = np.ones((len(corplist_tag_set), len(corplist_tag_set)), dtype="float32")
for i, t1 in enumerate(corplist_tag_set):
    for j, t2 in enumerate(corplist_tag_set):
        tags_matrix[i, j] = t2_given_t1(t2, t1)[0] / t2_given_t1(t2, t1)[1]
        pass
    pass

# Function to help pi
def help_pi(pi1, raw_corpus=training_corpus_lower):
    adding = 0
    for items in raw_corpus:
        if items[0][0] == pi1:
            adding += 1
            pass
        else:
            pass
        pass
    return adding / len(raw_corpus)


# Create Initial State Prob
pi = np.ones(len(corplist_words_set), dtype="float32")
num = 0
for item in corplist_words_set:
    pi[num] = help_pi(item)
    num += 1
    pass

viterbi(numbered_input, pi, tags_matrix, prob_matrix)
