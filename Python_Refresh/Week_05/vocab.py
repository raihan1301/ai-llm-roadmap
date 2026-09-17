def add_prefix_un(word):
    return "un" + word

def make_word_groups(vocab_words):  # vocab word is list and 1st word in list is prefix to use
    """
    :param vocab_words: list of vocabulary words with a prefix.
    :return: str of prefix followed by vocabulary words with
    prefix applied, separated by ' :: '.
 
    This function takes a `vocab_words` list and returns a string
    with the prefix  and the words with prefix applied, separated
    by ' :: '.
    """
    return (" :: " + vocab_words[0]).join(vocab_words)

def remove_suffix_ness(word):
    """
 
    :param word: str of word to remove suffix from.
    :return: str of word with suffix removed & spelling adjusted.
 
    This function takes in a word and returns the base word with `ness` removed.
    """
    updated_word = word[:-4]

    if updated_word.endswith("i"):
        updated_word = word[:-1] + "y"


    return updated_word

def adjective_to_verb(sentence, index):
    """
 
    :param sentence: str that uses the word in sentence
    :param index:  index of the word to remove and transform
    :return:  str word that changes the extracted adjective to a verb.
 
    A function takes a `sentence` using the
    vocabulary word, and the `index` of the word once that sentence
    is split apart.  The function should return the extracted
    adjective as a verb.
    """
    return sentence.split()[index].strip(".")+'en'


def main():
    result1 = add_prefix_un("happy")
    print(result1)

    result2 = make_word_groups(['pre', 'serve', 'dispose', 'position'])
    print(result2)

    result3 = remove_suffix_ness("sadness")
    print(result3)

    result4 = adjective_to_verb('It got dark as the sun set.', 2)
    print(result4)

main()