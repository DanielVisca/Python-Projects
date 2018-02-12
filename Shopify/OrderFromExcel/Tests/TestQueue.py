from API import Queue
import unittest


class TestQueue(unittest.TestCase):
    """
    Design Note: Checking two may be redundant
    """

    def test_add(self):
        queue = Queue()

        # 1 addition
        queue.add(1)
        self.assertEqual(queue._data[0], 1)

        # 2 additions
        queue.add(2)
        queue.add(3)
        self.assertEqual(queue._data[1], 2)
        self.assertEqual(queue._data[2], 3)

    def test_remove(self):
        queue = Queue()

        # remove one
        queue.add(1)
        self.assertEqual(queue.remove() ,1)
        self.assertEqual(queue._data, [])

        # remove two
        queue.add(1)
        queue.add(2)
        self.assertEqual(queue.remove(), 1)
        self.assertEqual(queue._data, [2])
        self.assertEqual(queue.remove(), 2)
        self.assertEqual(queue._data, [])

    def test_is_empty(self):
        q = Queue()
        self.assertTrue(q.is_empty())
        q.add(1)
        self.assertFalse(q.is_empty())


if __name__ == '__main__':
    # Currently not running
    unittest.main()