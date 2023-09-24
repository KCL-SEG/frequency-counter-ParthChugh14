"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    for i in items:
        item = str(i)
        val = 1
        if item in frequencies:
            val = frequencies.get(item) + 1
        frequencies.update({item:val})
    return frequencies