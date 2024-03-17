class SquareIter:
    def __init__(self, sequence):
        self._sequence = sequence
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            if self._index < len(self._sequence):
                for item in self._sequence:
                    return item ** 2
        except StopIteration:
            pass


sq_obj = SquareIter(range(1, 1000))
for i in range(0, 10):
    print(next(sq_obj))
