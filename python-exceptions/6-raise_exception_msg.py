#!/usr/bin/python3
"""Defines a function that raises a NameError exception with a message."""


def raise_exception_msg(message=""):
    """Raise a NameError exception with a given message.

    Args:
        message (str): The message for the NameError exception.
    """
    raise NameError(message)
