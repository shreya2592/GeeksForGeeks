#implement Balanced parentheses: each opening symbol has a corrosponding closing symbol 


from Stack import Stack

def parChecker(symbolStr):
    s=Stack()
    BalancePar=True
    index=0

    while (index<len(symbolStr)):
        symbol=symbolStr[index]
        if symbol == '(':
            s.push(symbol)
        else:
            if s.isEmpty():
                BalancePar=False
            else:
                s.pop()

        index=index+1

    if BalancePar and s.isEmpty():
        return True
    else:
        return False


print(parChecker('((()))'))
print(parChecker('((())))'))
print(parChecker('(((()))'))
