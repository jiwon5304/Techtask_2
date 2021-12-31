'''
    Linked List 구현하기
'''
from typing import Union

InputType = Union[int, str, float]

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def append(self, data) -> None:
        node = Node(data)

        # TODO
        # 가장 뒤에 새로운 data를 이어 붙여주세요
        pass

    def display(self):
        # TODO
        # 처음(head)부터 끝까지 출력 해주세요
        # 출력 방식은 자유
        pass

    def insert_at_first(self, data) -> None:
        # TODO
        # 가장 처음에 data를 넣고 나머지는 그 뒤에 붙여지도록 하세요
        pass

    def delete_node_by_data(self, data) -> None:
        # TODO
        # 처음부터 찾으며 Node의 data가 input data와 일치하면 해당 노드 삭제
        pass

    def length(self) -> int:
        # TODO
        # linked list에 있는 data의 개수를 리턴하는 함수
        return 0