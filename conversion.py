# Binary and decimal function takes int data-type
# Converting Binary to Decimal

def binToDec(num):
    value = 0
    a = 0
    while num>0:
        value = value + 2**a*(num%10)
        num = int(num//10)
        a = a+1
    return value

# Converting Decimal to binary

def decToBin(num):
    list = ["0","0","0","0","0","0","0","0"]
    i = 7
    while num>0:
        value = num%2
        list[i] = str(value)
        num = int(num//2)
        i = i-1
    return"".join(list)

# It takes string data type
# converting binary number to 8-bit binary

def convert(string):
    eightBit=string
    if(len(string)!=8):
        for i in range(len(string),8):
            eightBit="0"+eightBit
    return eightBit
