
def create_unique_word_set(sentence):
    return set(sentence.split())

if __name__ == '__main__':
    user_input = input("Enter a sentence: ")
    result = create_unique_word_set(user_input)
    print(result)
