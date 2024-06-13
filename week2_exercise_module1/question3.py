import os

content = open("./week2_exercise_module1/P1_data.txt", "r").read()
content = content.replace("\n", " ")
process_content = content.lower()
words = process_content.split(" ")


def count_words(words):
    word_count = {}

    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count


result = count_words(words)
