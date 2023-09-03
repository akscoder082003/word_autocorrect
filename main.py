# Step 1: Data Preprocessing
import re  # for regular expressions
from collections import Counter
import numpy as np
import pandas as pd

# Implement the function process_data which
# 1) Reads in a corpus
# 2) Changes everything to lowercase
# 3) Returns a list of words.

w = []  # words
with open("sample_new.txt", 'r') as f:
    file_name_data = f.read()
    file_name_data = file_name_data.lower()
    w = re.findall('\w+', file_name_data)

v = set(w)  # vocabulary
print(f"The first 10 words in our dictionary are; \n{w[0:10]}")
print(f"The dictionary has {len(v)} words ")


# a get_count function that returns a dictionary of word versus frequency
def get_count(w):
    word_count_dict = {}
    for word in w:
        if word in word_count_dict:
            word_count_dict[word] += 1
        else:
            word_count_dict[word] = 1
    return word_count_dict


word_count = get_count(w)
print(f"There are {len(word_count)} key values pairs")


# implement get_prob function to calculate the probability that will appear if randomly selected from the dictionary.


def get_prob(word_count_dict):
    prob = {}
    m = sum(word_count_dict.values())
    for key in word_count_dict.keys():
        prob[key] = word_count_dict[key] / m
    return prob


# Now we implement 4 edit word functions
# DeleteLetter:removes a letter from a given word
def DeleteLetter(word):
    delete_list = []
    split_list = []
    for i in range(len(word)):
        split_list.append((word[0:i], word[i:]))
    for a, b in split_list:
        delete_list.append(a + b[1:])
    return delete_list


delete_word_1 = DeleteLetter(word="cans")
# print(DeleteLetter("trash"))


# SwitchLetter:swap two adjacent letters
def SwitchLetter(word):
    split_1 = []
    switch_1 = []
    for i in range(len(word)):
        split_1.append((word[0:i], word[i:]))
    switch_1 = [a + b[1] + b[0] + b[2:] for a, b in split_1 if len(b) >= 2]
    return switch_1


switch_word_1 = SwitchLetter(word="eta")
# print(SwitchLetter("trash"))


# replace_letter: changes one letter to another
def replace_letter(word):
    split_l = []
    replace_list = []
    for i in range(len(word)):
        split_l.append((word[0:i], word[i:]))
    alphabets = 'abcdefghijklmnopqrstuvwxyz'
    replace_list = [a + l + (b[1:] if len(b) > 1 else '') for a, b in split_l if b for l in alphabets]
    return replace_list


replace_1 = replace_letter(word='can')
# print(replace_letter("trash"))


# insert_letter: adds additional characters

def insert_letter(word):
    split_l = []
    insert_list = []
    for i in range(len(word) + 1):
        split_l.append((word[0:i], word[i:]))
    letters = 'abcdefghijklmnopqrstuvwxyz'
    insert_list = [a + l + b for a, b in split_l for l in letters]
    # print(split_1)
    return insert_list


# print(insert_letter("trash"))


# combining the edits
# switch operation optional
def edit_one_letter(word, allow_switches=True):
    edit_set1 = set()
    edit_set1.update(DeleteLetter(word))
    if allow_switches:
        edit_set1.update(SwitchLetter(word))
        edit_set1.update(insert_letter(word))
        return edit_set1


# edit two letters
def edit_two_letters(word, allow_switches=True):
    edit_set2 = set()
    edit_one = edit_one_letter(word, allow_switches=allow_switches)
    for w in edit_one:
        if w:
            edit_two = edit_one_letter(w, allow_switches=allow_switches)
            edit_set2.update(edit_two)
    return edit_set2


# get corrected word
def get_corrections(word, prob, vocab, n=2):
    suggested_word = []
    best_suggestion = []
    suggested_word = list(
        (word in vocab and word) or edit_one_letter(word).intersection(vocab) or edit_two_letters(word).intersection(
            vocab
        )
    )
    best_suggestion = [[s, prob[s]] for s in list(reversed(suggested_word))]
    return best_suggestion


my_word = input("Enter any word: ")
prob = get_prob(word_count)
tmp_corrections = get_corrections(my_word, prob, v, 2)
for i, word_prob in enumerate(tmp_corrections):
    print(f"word {i}: {word_prob[0]}, probability {word_prob[1]:.6f}")
