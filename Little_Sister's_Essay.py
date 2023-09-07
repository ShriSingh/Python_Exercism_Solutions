"""Functions to help edit essay homework using string manipulation."""


def capitalize_title(title):
    """Convert the first letter of each word in the title to uppercase if needed.

    :param title: str - title string that needs title casing.
    :return: str - title string in title case (first letters capitalized).
    """
    # Storing the parameter input in a variable
    input_string = title
    # Using the title() to capitalize the first letter of each word
    output_string = input_string.title()
    # Returning the output
    return output_string


def check_sentence_ending(sentence):
    """Check the ending of the sentence to verify that a period is present.

    :param sentence: str - a sentence to check.
    :return: bool - return True if punctuated correctly with period, False otherwise.
    """
    # Using the endswith() function to check whether the string ends with a period
    proof_read_sentence = sentence.endswith('.')
    # Checks whether the string ends in a period or not
    if proof_read_sentence is True:
        # Returns True if the sentence ends in a period
        return True
    # Returns False if the sentence doesn't end in a period
    return False


def clean_up_spacing(sentence):
    """Verify that there isn't any whitespace at the start and end of the sentence.

    :param sentence: str - a sentence to clean of leading and trailing space characters.
    :return: str - a sentence that has been cleaned of leading and trailing space characters.
    """
    # Stores the parameter in a variable
    input_line = sentence
    # Applies the strip() to remove the whitespaces from the sentence
    cleaned_up_line = input_line.strip()
    # Returns the resulting variable
    return cleaned_up_line


def replace_word_choice(sentence, old_word, new_word):
    """Replace a word in the provided sentence with a new one.

    :param sentence: str - a sentence to replace words in.
    :param old_word: str - word to replace.
    :param new_word: str - replacement word.
    :return: str - input sentence with new words in place of old words.
    """
    # Applying the .replace() to swap the present old word with the entered new word
    output_phrase = sentence.replace(old_word, new_word)
    # Returning the varaible after the operation
    return output_phrase
