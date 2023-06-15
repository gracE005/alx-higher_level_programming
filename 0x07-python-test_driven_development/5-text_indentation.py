#!/usr/bin/python3
"""
    A module that contains  a command that prints a text with two new lines after each of these characters: ., ? and :
"""


def text_indentation(text):
    """
        denoting specific characters: ., ? and : while indenting on two new lines 
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    begin = 0
    delimeters = [".", "?", ":"]
    for c in text:
        if c.isspace() and begin == 0:
            continue
        elif c in delimeters:
            print("{}\n\n".format(c), end="")
            begin = 0
            continue
        else:
            print("{}".format(c), end="")
            begin += 1
