
def count_word_occurrences(sentence):
    word_count = {}
    words = sentence.split()
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    return word_count

if __name__ == '__main__':
    user_input = input("Enter a sentence: ")
    result = count_word_occurrences(user_input)
    print(result)
