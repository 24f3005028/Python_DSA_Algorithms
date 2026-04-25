"""
STACK
Implementing Stack class:   -   LIFO -  Last in First Out
    Data members: List of Integers
    Functions: constructor __init__(), isEmpty(), push(), pop() and __str__()
"""
class Stack:
    def __init__(self):
        self.stack = []
    def isEmpty(self):
        return self.stack == []
    def push(self, v):
        self.stack.append(v)
    def pop(self):
        v = None
        if not self.isEmpty():
            v = self.stack.pop()
        return v
    def __str__(self):
        return str(self.stack)
    
st = Stack()
st.push(10)
st.push(50)
st.push(30)
st.push(20)
st.push(80)
st.push(100)
print(st)
print(st.pop())
print(st.pop())