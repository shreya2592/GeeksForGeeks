# Program to convert  a decimal number to a binary number

from Stack import Stack

def decToBin(num):
    s=Stack()
    while num!=0:
        rem=num%2
        s.push(rem)
        num=num//2

    binString=""
    while not s.isEmpty():
        binString=binString+str(s.pop())


    return binString


print(decToBin(42))

