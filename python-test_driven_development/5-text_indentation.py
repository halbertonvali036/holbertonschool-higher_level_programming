"""Module for text_indentation function.

Provides a function that prints text with 2 new lines
after each occurrence of '.', '?', or ':'.
"""


def text_indentation(text):
    """Prints a text with 2 new lines after each '.', '?', and ':'.

    Leading and trailing spaces on each printed line are removed.
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    c = 0
    while c < len(text) and text[c] == ' ':
        c += 1

    while c < len(text):
        print(text[c], end="")
        if text[c] in ".?:":
            print("\n")
            c += 1
            while c < len(text) and text[c] == ' ':
                c += 1
            continue
        c += 1
