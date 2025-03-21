class Stack:
    def __init__(self, stack: str = ''):
        self.stack = list(stack)

    def is_empty(self) -> bool:
        if len(self.stack) == 0:
            return True
        else:
            return False

    def push(self, elem) -> None:
        return self.stack.append(elem)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def size(self) -> int:
        return len(self.stack)

def balanced_sequence(sequence: str) -> bool:
    brackets = {')': '(', '}': '{', ']': '['}
    stack = Stack()
    for char in sequence:
        if char in brackets.values():  # Если это открывающая скобка
            stack.push(char)
        elif char in brackets.keys():  # Если это закрывающая скобка
            if stack.is_empty() or stack.peek() != brackets[char]:
                return False
            stack.pop()
    return stack.is_empty()

def test():
    stack = Stack('(((([{}]))))')
    assert balanced_sequence('(((([{}]))))')
    assert balanced_sequence('[([])((([[[]]])))]{()}')
    assert balanced_sequence('{{[()]}}')
    assert not balanced_sequence('}{}')
    assert not balanced_sequence('{{[(])]}}')
    assert not balanced_sequence('[[{())}]')
    assert not balanced_sequence('()((((((((((((((((((')
    print('Все тесты прошли успешно!')


if __name__ == '__main__':

    test()