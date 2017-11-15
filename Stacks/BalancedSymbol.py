# Implement balanced symbols --- for each ({[ there should be })]


from Stack import Stack

def parChecker(symbolStr):
    index=0
    BalancedPar=True
    s=Stack()

    while index<len(symbolStr) :

        symbol=symbolStr[index]

        if symbol in '([{':
            s.push(symbol)
        else:
            if s.isEmpty():
                BalancedPar=False
            else:
                top=s.pop()
                if not matchSymbol(top, symbol):
                    BalancedPar=False
        index=index+1
    if BalancedPar and s.isEmpty():
        return True
    else:
        return False


def matchSymbol(symbol1, symbol2):
    openers='({['
    closers=')}]'
    return openers.index(symbol1)== closers.index(symbol2)


print(parChecker('{{([][])}()}'))
print(parChecker('[{()]'))


