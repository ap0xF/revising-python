"""
The collections.abc module includes an abstract base class (ABC) called Iterator.
You can use this ABC to create your custom iterators quickly
"""
from collections.abc import Iterator

class SequenceIterator(Iterator):
    def __init__(self, sequence):
        self._sequence = sequence
        self._index = 0

    def __next__(self):
        if self._index < len(self._sequence):
            item = self._sequence[self._index]
            self._index = self._index + 1
            return item
        else:
            raise StopIteration
