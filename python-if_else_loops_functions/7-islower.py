#!/usr/bin/env python3
def islower(c):
    """
    Checks if a character is lowercase.
    
    Args:
        c: The character to check.
        
    Returns:
        True if c is lowercase, False otherwise.
    """
    # ord('a') is 97 and ord('z') is 122
    if ord(c) >= 97 and ord(c) <= 122:
        return True
    else:
        return False
