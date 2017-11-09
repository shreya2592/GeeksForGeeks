# implement Stacks as an Array/List


#import maxsize from sys 

from sys import maxsize

def createStack():
    stack=[]
    return stack

def isEmpty(stack):
    return len(stack)==0

def push(stack, item):
    stack.append(item)
    print ("Item pushed to the stack : ",item)

def pop(stack):
    if isEmpty(stack):
        return str(-maxsize-1)
    return stack.pop()



stack = createStack()
push(stack, str(10))
push (stack, str(20))
push (stack, str(30))
print ("Element popped from the stack: "+ pop(stack))





