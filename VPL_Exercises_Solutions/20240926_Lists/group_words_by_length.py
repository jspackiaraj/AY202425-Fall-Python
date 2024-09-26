
def group_words_by_length(words):
    length_dict = {}
    for word in words:
        length_dict.setdefault(len(word), []).append(word)
    return length_dict

if __name__ == '__main__':
    words = input("Enter a list of words separated by spaces: ").split()
    result = group_words_by_length(words)
    print(result)
