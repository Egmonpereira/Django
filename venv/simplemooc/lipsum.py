import random, os, lipsum #para obter 100 palavras aleatoriamente

def generate_lorem_ipsum(word_count=50):
    lorem_ipsum = (
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. "
        "Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor "
        "in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, "
        "sunt in culpa qui officia deserunt mollit anim id est laborum."
    )
    words = lorem_ipsum.split()
    return ' '.join(random.choices(words, k=word_count))


if __name__ == "__main__":
    os.system('clear')
    # Example usage
    print(generate_lorem_ipsum(100))

#    print(lipsum.generate_words(100)) #para obter 100 palavras aleatoriamente
#    print(lipsum.generate_sentences(3)) #para obter 3 frases aleatoriamente
