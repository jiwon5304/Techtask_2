'''
    Stack 구현하기

    - push: stack에 값을 넣는다
    - pop: stack에서 마지막 값을 빼낸다 (제거한다)
    - peek: stack에서 마지막 값을 리턴한다.
'''
from typing import Union

InputType = Union[int, str, float]

class Stack:
    def __init__(self) -> None:
        self.stack: list[InputType] = []

    def push(self, data: InputType) -> None:
        self.stack.append(data)
        return self.stack

    def pop(self) -> None:
        self.stack.pop()
        return self.stack

    def display(self) -> list[InputType]:
        return self.stack

    def peek(self) -> InputType:
        return self.stack[-1]



