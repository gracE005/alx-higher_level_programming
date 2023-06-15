#!/usr/bin/python3
"""
A module that contains a command that prints a text with 2 new lines after each of these characters: ., ? and : 
"""


def text_indentation(text):
    """indent and separate text into "?", ":", "." with two new lines after each other
    Args:
        text: a string
    Returns:
        No return
    Raises:
        TypeError: If text is not a string
    """

    if type(text) is not str:
        raise TypeError("text must be a string")
    flag = 0
    a = 0
    while a < len(text):
        if flag == 0:
            if text[a] == ' ':
                a += 1
                continue
            else:
                flag = 1
        if flag == 1:
            if text[a] == '?' or text[a] == '.' or text[a] == ':':
                print(text[a])
                print()
                flag = 0
            else:
                if text[a + 1] == '\n':
                     a += 1
                     continue 
                print(text[a], end="")
           a += 1
