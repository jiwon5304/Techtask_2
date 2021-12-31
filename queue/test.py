import unittest

from queue.__init__ import Queue

class QueueTestCase(unittest.TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def test_queue_enqueue(self):
        q = Queue()
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)
        q.enqueue(4)

        self.assertEqual(q.display(), [1,2,3,4])

    def test_stack_dequeue(self):
        pass

    def test_stack_front(self):
        pass

    def test_stack_back(self):
        pass