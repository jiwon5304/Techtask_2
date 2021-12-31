import unittest

from stack.__init__ import Stack

class StackTestCase(unittest.TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def test_stack_push(self):
        s = Stack()
        s.push(1)
        s.push(2)
        s.push(3)
        s.push(4)

        self.assertEqual(s.display(), [1,2,3,4])

    def test_stack_pop(self):
        pass

    def test_stack_peek(self):
        pass