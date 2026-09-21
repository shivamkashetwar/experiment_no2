stack=[]

def push(item):
    stack.append(item)
    print(item,"pushed")

def pop():
    if len(stack)==0:
        print(item,"stack is underflow")
    else:
        item=stack.pop()
        print(item,"poped")

def peek():
    if len(stack)==0:
        print("stack is peek")
    else:
        print(stack[-1],"peek of the stack")

def is_empty():
    if len(stack)==0:
        print("stack is empty")
    else:
        print("satck is not empty")

def size():
    print("Stack size:", len(stack))

def display():
    if len(stack)==0:
        print("stack is empty")
    else:
        print("stack:",stack)


def search(item):
    if item in stack:
        print(item, "found")
    else:
        print(item, "not found")

def clear():
    stack.clear()
    print(stack,"satck is clear")


push(10)
push(20)
push(30)

display()
peek()
size()
search(20)

pop()
display()

is_empty()

clear()
display()
