def capitalize_title(cap_title):
    return cap_title.title()

def check_sentence_ending(sentence):
    return sentence.endswith(".")

def clean_up_spacing(sentence):
    return sentence.strip()

def replace_word_choice(sentence, old_word, new_word):
    '''
    :param sentence: str a sentence to replace words in.
    :param new_word: str replacement word
    :param old_word: str word to replace
    :return:  str input sentence with new words in place of old words
    '''
    return sentence.replace(old_word, new_word)

def main():
    result1 = capitalize_title("my hobbies")
    print(result1)
    
    result2 = check_sentence_ending("I like to hike, bake, and read.")
    print(result2)
    
    result3 = clean_up_spacing(" I like to go on hikes with my dog.  ")
    print(result3)
    
    result4 = replace_word_choice("I bake good cakes.", "good", "amazing")
    print(result4)

main()
    