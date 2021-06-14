from gates import *
from conversion import *

#It takes int data type as input and stores value in a list

def binBitAdder(a,b):
    list = ["0","0","0","0","0","0","0","0"]
    i = 7
    carry = 0
    num = max(a,b)
    while(num>0):
        a1 = a%10
        b1 = b%10

        #sumAdder operation
        xorFirst = xorGate(a1,b1)
        sumAdder = xorGate(xorFirst,carry)

        #carryout operation
        andFirst = andGate(a1,b1)
        andSecond = andGate(xorFirst,carry)
        carry = xorGate(andFirst,andSecond)
        
        list[i] = str(sumAdder)
        i = i-1
        num = int(num/10)
        a = int(a/10)
        b = int(b/10)
    if i>=0:
        list[i] = str(carry)
    return "".join(list)


#Converting decimal number to 8-bit adder
# It takes int data type as input
def decBitAdder(a,b):
    decA = int(decToBin(a))
    decB = int(decToBin(b))
    decAdder = binBitAdder(decA,decB)
    return decAdder
