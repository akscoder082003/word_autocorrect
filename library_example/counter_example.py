from collections import Counter

word_list = ['a', 'b', 'a', 'c', 'b', 'a', 'd']
word_counts = Counter(word_list)

print(word_counts)
print(f"Duplicates of a is {word_counts['a']} and for b is {word_counts['b']} and for c is {word_counts['c']} and for d is {word_counts['d']}.")