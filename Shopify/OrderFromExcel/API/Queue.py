class Queue:
    """
    FIFO (first in first out)
    """

    def __init__(self):
        """
        Create and initialize a new queue self.

        :return: NoneType
        """
        self._data = []

    def add(self, prod):
        """
        Add prod at the back of this queue.

        :param prod:
        :return: NoneType
        """
        self._data.append(prod)

    def remove(self):
        """
        Remove and return front object from self.

        :return: Object

        >>> q = Queue()
        >>> q.add("bath bombs")
        >>> q.add("babel fish")
        >>> q.remove()
        "bath bombs"
        """
        return self._data.pop(0)

    def is_empty(self):
        """
        Return True when queue self is empty, False otherwise.

        :return: bool

        >>> q = Queue()
        >>> q .add("Ray Banz")
        >>> q.is_empty()
        False
        >>> q.remove()
        "Ray Banz"
        >>> q.is_empty()
        True
        """
        return self._data == []


"""
#Personal Note: remember what this is for and if it is necessary or looks good
if __name__ == '__main__':
    import doctest
    doctest.testmod()
"""
