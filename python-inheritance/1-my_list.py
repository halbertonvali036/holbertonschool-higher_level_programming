#!/usr/bin/python3
"""Defines a class MyList that inherits from list."""


class MyList(list):
    """Subclass of list with additional utility methods."""

    def print_sorted(self):
        """Prints the list in ascending sorted order without modifying it."""
        print(sorted(self))
