from typing import Generic, TypeVar, List, Optional

T = TypeVar('T')


class Queue(Generic[T]):
    queue: List[T]

    def __init__(self) -> None:
        self.queue = []

    def enqueue(self, value: T) -> None:
        self.queue.append(value)

    def dequeue(self) -> Optional[T]:
        return self.queue.pop(0) if self.size() > 0 else None

    def size(self) -> int:
        return len(self.queue)


class Stack(Generic[T]):
    stack: List[T]

    def __init__(self) -> None:
        self.stack = []

    def push(self, value: T) -> None:
        self.stack.append(value)

    def pop(self) -> Optional[T]:
        return self.stack.pop() if self.size() > 0 else None

    def size(self) -> int:
        return len(self.stack)
