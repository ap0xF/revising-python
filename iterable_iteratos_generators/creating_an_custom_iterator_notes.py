"""The most generic use case of a Python iterator is to allow iteration over a stream of data
or a container data structure. Python uses iterators under the hood to support every operation
 that requires iteration, including for loops, comprehensions, iterable unpacking, and more.
 So, you’re constantly using iterators without being conscious of them"""

"""you can write at least three different types of custom iterators. You can have iterators that:

Take a stream of data and yield data items as they appear in the original data
Take a data stream, transform each item, and yield transformed items
Take no input data, generating new data as a result of some computation to finally yield the generated items
The first kind of iterator is what you’d call a classic iterator because it implements the original iterator pattern.
The second and third types of iterators take the pattern further by adding new capabilities 
and leveraging the power of iterators.

Note: The second and third types of iterators may bring to mind some techniques that sound similar to mapping 
and filtering operations from functional programming."""
