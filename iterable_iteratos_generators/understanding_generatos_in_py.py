"""
Generator functions are special types of functions that allow you to create iterators using a functional style.
Unlike regular functions, which typically compute a value and return it to the caller,
generator functions return a generator iterator that yields a stream of data one value at a time.
"""

"""
Note: In Python, you’ll commonly use the term generators to collectively refer to two separate concepts: 
the generator function and the generator iterator. The generator function is the function that you define using the yield statement.
The generator iterator is what this function returns.
"""

"""
A generator function returns an iterator (generator iterator) that supports the iterator protocol out of the box. 
So, generators are also iterators.
"""


# generator function equivalent of SequenceIterator

def sequence_generator(sequence):
    for item in sequence:
        yield item ** 2  # item is an iterator


returned_iterator = sequence_generator(range(1, 10))

print(returned_iterator)

for i in returned_iterator:
    print(i)

"""generators are efficient tool to create function-based-iterator"""

"""Check out generator expression in next code file, it's sexy af,
looks just like list comprehension, [] has been replaced by ()"""