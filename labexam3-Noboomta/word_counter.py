from typing import Any, Iterator, Union, Optional, List, Collection

# TODO 1. Add type hints to the class and method def statements.
#         If multiple type hints apply choose the most descriptive one.
# TODO 2. Improve the code for __contains__

class WordCounter:
    """Keep a count of occurrences of different words.
    
    >>> wc = WordCounter()
    >>> wc.add_word('apple')
    >>> wc.add_word('pear')
    >>> wc.add_word('apple')
    >>> wc['apple']
    2
    >>> wc['pear']
    1
    >>> 'banana' in wc
    False
    >>> 'Apple' in wc
    True
    >>> for fruit in wc: print(fruit)
    apple
    pear
    >>> wc.add_word('grape')
    >>> len(wc)
    3
    """

    def __init__(self) -> None:
        self.words = {}
     
    def add_word(self, word: str) -> None:
        """Add a count for a word."""
        word = word.lower()
        if self.__contains__(word):
            self.words[word] += 1
        else:
            self.words[word] = 1

    def __contains__(self, word: str) -> bool:
        """Test if a word has been added to this word counter."""
        word = word.lower()
        for w in self.words:
            if word == w:
                return True
        return False

    def __getitem__(self, key: int) -> int:
        """Get how many times a word has been added.

        Raises KeyError if key is not in this WordCounter."""
        return self.words[key]

    def __len__(self) -> int:
        """Return the number of distinct words in this WordCounter."""
        return len(self.words)

    def __iter__(self) -> Iterator:
        """Return an iterator for the words in this WordCounter."""
        return iter(self.words.keys())
