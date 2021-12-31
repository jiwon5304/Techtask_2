'''
    Queue 구현하기

    - enqueue: queue에 값을 넣는다
    - dequeue: queue에서 첫번쨰 값을 빼낸다
    - display: 현재 가지고 있는 큐를 보여준다
    - front: 제일 앞에 있는 값을 보여준다
    - back: 제일 뒤에 있는 값을 보여준다
'''
from typing import Union

InputType = Union[int, str, float]

class Queue:
    def __init__(self) -> None:
        self.queue: list[InputType] = []

    def enqueue(self, data: InputType) -> None:
        pass

    def dequeue(self) -> None:
        pass

    def display(self) -> list[InputType]:
        return self.queue

    def front(self) -> InputType:
        pass

    def back(self) -> InputType:
        pass
