#!/usr/bin/python3
"""Defines the text_indentation function."""


def text_indentation(text):
    """Print a text with 2 new lines after each ., ? and : character.

    Args:
        text (str): the text to print.

    Raises:
        TypeError: if text is not a string.
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    line = ""
    for char in text:
        if char == " " and line == "":
            continue
        line += char
        if char in ".?:":
            print(line.strip())
            print()
            line = ""
    if line.strip():
        print(line.strip())
