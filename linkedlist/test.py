import unittest

from linkedlist.__init__ import LinkedList

class LinkedListTestCase(unittest.TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def test_append_node(self):
        l = LinkedList()
        l.append(5)
        l.append(3)
        l.append(8)
        l.append(4)
        
        # display method가 배열로 리턴을 한다면
        self.assertEqual(l.display(), [5,3,8,4])
        # 다른 방식으로 리턴하는 경우 그거에 맞춰서 테스트

    def test_insert_at_first(self):
        l = LinkedList()
        l.append(5)
        l.append(3)
        l.append(8)
        l.append(4)
        l.insert_at_first(0)
        l.insert_at_first(1)
        
        # display method가 배열로 리턴을 한다면
        self.assertEqual(l.display(), [1,0,5,3,8,4])
        # 다른 방식으로 리턴하는 경우 그거에 맞춰서 테스트

    def test_length(self):
        l = LinkedList()
        l.append(5)
        l.append(3)
        l.append(8)
        l.append(4)
        
        self.assertEqual(l.length(), 4)

    def test_remove_node(self):
        pass