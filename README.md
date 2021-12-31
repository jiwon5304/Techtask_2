# 데이터구조 사전과제

## 데이터구조 코딩테스트 문제 (Queue, Stack)

## 필수사항

- python 3.8 이상

## 문제

### stack

1. 스택을 array 방식으로 push, pop, peek 기능 추가하기 (20점)

(자세한 내용은 stack/**init**.py 폴더안에 있습니다)

1. 테스트는 uniittest로 할 수 있는데 나머지 기능에 대한 테스트 코드도 구현하기 (10점)
    1. stack 폴더내에서 `python -m unittest`

### queue

1. 큐를 array 방식으로 enqueue, dequeue, front, back 기능 추가하기 (20점)

(자세한 내용은 queue/**init**.py 폴더안에 있습니다)

1. 테스트는 uniittest로 할 수 있는데 나머지 기능에 대한 테스트 코드도 구현하기 (10점)
    1. queue 폴더내에서 `python -m unittest`

### stack & queue

고정된 크기의 큐, 스택 구현하기. (각각 20점)

example)

```python
stack = Stack(10)

queue = Queue(10)
```

hint) 시작, 끝 배열 index를 활용

위와 같이 크기를 받아서 하도록 하고 기존에서 확장하거나 새로운 구현체로 만들어도 됩니다. 폴더만 각 queue, stack 폴더 내에 넣어주세요.

### 총합계

100점

### 추가 문제

1. Linked List를 구현하기 (50점)
linkedlist 폴더 내에 있는 파일로 시작해서 구현해주세요.
2. Linked List를 이용해서 Stack, Queue 구현하기 (100점)
(동일하게 위에 정의한 stack, queue의 method만 구현하면 됩니다)

## 테스트 실행 방법

- 최상위 폴더에서 `python -m unittest`

## 유의사항

- 제한시간 1시간 이내에 받은 이메일 주소로 첨부하여 답장해주세요.
- 이메일은 시험 시작 10분전에 보냅니다. 미리 내용을 숙지 후 시작해주세요.
- 첨부파일내에 있는 스켈레톤 코드를 잘 활용해주세요.
- 코드 제출 20분 후에 원격으로 코드 리뷰가 있습니다.
    - 회의 참여 링크 ⬇️
    
    [Meet](https://meet.google.com/nws-jjwm-vri)