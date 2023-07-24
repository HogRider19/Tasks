"""
    Write a program that performs a search for solutions to a word game. The goal of the game is to find sets of five words that share a vowel alternation.
    E.g., one solution to the game might be the words
"""

def find_solutions(words):
    words = set(words)
    solutions = set()
    
    for word in words:
        for i, c in enumerate(word):
            if c in 'aeiou':
                variations = frozenset( ''.join(word[:i] + v + word[i+1:]) for v in 'aeiou' )
                if variations <= words:
                    solutions.add(variations)
    
    return sorted(sorted(s) for s in solutions)