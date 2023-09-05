"""Functions for creating, transforming, and adding prefixes to strings."""


def add_prefix_un(word):
    """Take the given word and add the 'un' prefix.

    :param word: str - containing the root word.
    :return: str - of root word prepended with 'un'.
    """
    # Adding the 'un' prefix with the root word
    negative_word = 'un' + word
    # Returning the newly created word
    return negative_word


def make_word_groups(vocab_words):
    """Transform a list containing a prefix and words into a string with the prefix followed by the words with prefix prepended.

    :param vocab_words: list - of vocabulary words with prefix in first index.
    :return: str - of prefix followed by vocabulary words with
            prefix applied.

    This function takes a `vocab_words` list and returns a string
    with the prefix and the words with prefix applied, separated
     by ' :: '.

    For example: list('en', 'close', 'joy', 'lighten'),
    produces the following string: 'en :: enclose :: enjoy :: enlighten'.
    """
    # The prefix to be added on other elements
    prefix = vocab_words[0]
    # Storing the words that need to have prefix applied
    words_to_be_prefixed = vocab_words[1:]
    # Storing the new list of words
    prefixed_words = []
    # Iterating through the list of words to be "prefixed"
    for element in words_to_be_prefixed:
        # Adding the asked prefix to the word
        prefixed_word = prefix + element
        # Adding the prefixed words to the list
        prefixed_words.append(prefixed_word)
    # Adding back the first index(converted into an element) from the original list 
    complete_list = [prefix] + prefixed_words
    # Returning the string separated with ' :: '
    resulting_string = ' :: '.join(complete_list)
    # Returning the desired string
    return resulting_string
        
def remove_suffix_ness(word):
    """Remove the suffix from the word while keeping spelling in mind.

    :param word: str - of word to remove suffix from.
    :return: str - of word with suffix removed & spelling adjusted.

    For example: "heaviness" becomes "heavy", but "sadness" becomes "sad".
    """
    # Removing the "ness" sufix using slice notation
    unsuffixed_word = word[:-4]
    # Checking if the fifth index from the back is "i"
    if word[-5] == 'i':
        # Changing the word's fifth index from the back to be "y"
        unsuffixed_word = word[:-5] + 'y'
    # Returning the appropriate the word with their suffix removed
    return unsuffixed_word


def adjective_to_verb(sentence, index):
    """Change the adjective within the sentence to a verb.

    :param sentence: str - that uses the word in sentence.
    :param index: int - index of the word to remove and transform.
    :return: str - word that changes the extracted adjective to a verb.

    For example, ("It got dark as the sun set.", 2) becomes "darken".
    """
    # Storing the suffix
    suffix = 'en'
    # Splitting the whole string into separate elements of a list
    splitted_sentence = sentence.split(' ')
    # Variable to hold the adjective to verb 
    changed_word = splitted_sentence[index] + suffix
    # Checking the value of the index 
    if index == -1:
        # Adding the suffix to the adjective at the end of the sentence
        changed_word = splitted_sentence[index][:-1] + suffix
    # Returning the result of changing adjective to a verb
    return changed_word
