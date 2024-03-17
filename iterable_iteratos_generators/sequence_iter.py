class SequenceIterator:
    """ iterator is a design pattern,
    here I have used iterator design pattern to create an Iterator class called
    SequenceIterator, it can act as an iterable (list, tuple, set), which can be iterated upon
    using loops in py"""

    def __init__(self, sequence):
        self._sequence = sequence
        self._index = 0

    def __iter__(self):
        """
         You can create an iterator that doesn’t define an .__iter__() method,
         in which case its .__next__() method will still work.
         However, you must implement .__iter__() if you want your iterator to work in for loops.
        This loop always calls .__iter__() to initialize the iterator.
        """
        return self

    def __next__(self):
        if self._index < len(self._sequence):  # it's like checking for OutOfBound exception
            item = self._sequence[self._index]
            self._index += 1
            return item
        else:
            raise StopIteration  # flow control for iteration is done by raising error lol


for item in SequenceIterator([1, 2, 3, 4, 5]):
    """Loop uses the __next__ method internally """
    print(item)
