#It takes string data type as input
#for checking binary number consists only of 0 or 1
def binaryValidate(num):
    binVal = False
    digits = '01'
    for i  in num:
        if i in digits:
            binVal = True
        else:
            binVal = False
            break
    return binVal
# It returns boolean value
