from adder import *
from validation import *
from conversion import *
# It is the main function to carry out all operations
def main():
    print('''                      Welcome to the 8-bit Adder Program
              -------------Developed by Sujan Thapa-------------''')
    flag = False
    while (not flag):
        # Taking suitable data type from user
        dataType = input("Enter d or D for decimal and Enter b or B for binary: ")
        if dataType in ["d","D"]:
            print('''
                        +-------------------------------------------+
                        |               Information                 |
                        +-------------------------------------------+
                        |   You have selected Decimal number System |
                        +-------------------------------------------+
                        |     Enter number ranging from  0-255      |
                        +-------------------------------------------+

                        ''')
            while(not flag):
                try:
                    dec1 = int(input("Enter first decimal number: "))
                    if dec1>255:
                        print('''
                        +-------------------------------------------+
                        |                  ERROR                    |
                        +-------------------------------------------+
                        |   Do not enter number greater than 255    |
                        +-------------------------------------------+

                        ''')
                    elif dec1<0:
                        print('''
                        +-------------------------------------------+
                        |                  ERROR                    |
                        +-------------------------------------------+
                        |        Do not enter negative number       |
                        +-------------------------------------------+

                        ''')
                    else:
                        break
                except:
                    # showing proper message after finding error
                    print('''
                        +------------------------------------------------+
                        |                     ERROR                      |
                        +------------------------------------------------+
                        | No special characters and empty spaces allowed |
                        +------------------------------------------------+

                        ''')
                    flag = False
            while(not flag):
                try:
                    dec2 = int(input("Enter second decimal number: "))
                    if dec2>255:
                        print('''
                        +-------------------------------------------+
                        |                  ERROR                    |
                        +-------------------------------------------+
                        |   Do not enter number greater than 255    |
                        +-------------------------------------------+

                        ''')
                        continue
                    dec_sum = dec1+dec2
                    if dec_sum>255:
                        print('''
                        +-----------------------------------------------+
                        |                    ERROR                      |
                        +-----------------------------------------------+
                        |  The sum of two number must be less than 255  |
                        +-----------------------------------------------+

                        ''')
                    else:
                        firstNum = decToBin(dec1)
                        secondNum = decToBin(dec2)
                        value = decBitAdder(dec1,dec2)
                        print(f'''
                        +-----------------------------------------------------+
                        |                   Decimal System                    |
                        +---------------+-------------------------------------+
                        |   Variables   |              Output                 |
                        +---------------+-------------------------------------+
                          First nummber |In Decimal      - {dec1}
                                        |In 8-bit Binary - {firstNum}
                        +-----------------------------------------------------+
                          Second number |In Decimal      -  {dec2}
                                        |In 8-bit Binary -  {secondNum}
                        +-----------------------------------------------------+
                          8-bit output  |In Decimal      -  {dec_sum}
                                        |In 8-bit Binary -  {value}
                        +---------------+-------------------------------------+
                        ''')
                        try:
                            resume = False
                            while(not resume):
                                inputResume = input("Enter [Y/y] to continue or [N/n] to quit: ")
                                if inputResume in ["Y","y"]:
                                    main()
                                elif inputResume in ["N","n"]:
                                    return
                        except:
                            print("Enter either [Y/y] or [N/n]: ")
                            break
                except:
                    print("No special characters and empty spaces allowed")
                    flag = False

        elif dataType in ["b","B"]:
            print('''
                        +-------------------------------------------+
                        |               Information                 |
                        +-------------------------------------------+
                        | You have selected Binary number System    |
                        +-------------------------------------------+
                        |   Enter number ranging from  0-11111111   |
                        +-------------------------------------------+

                        ''')
            while(not flag):
                try:
                    bin1 = int(input("Enter first binary number: "))
                    if bin1>11111111:
                        print('''
                        +-------------------------------------------+
                        |                  ERROR                    |
                        +-------------------------------------------+
                        |Do not enter number greater than 11111111  |
                        +-------------------------------------------+

                        ''')
                    elif bin1<0:
                        print('''
                        +-------------------------------------------+
                        |                  ERROR                    |
                        +-------------------------------------------+
                        |        Do not enter negative number       |
                        +-------------------------------------------+

                        ''')
                    elif binaryValidate(str(bin1))==False:
                        print('''
                        +-------------------------------------------+
                        |                  ERROR                    |
                        +-------------------------------------------+
                        |            Enter either 0 or 1            |
                        +-------------------------------------------+

                        ''')
                    else:
                        break
                except:
                    print('''
                        +------------------------------------------------+
                        |                     ERROR                      |
                        +------------------------------------------------+
                        | No special characters and empty spaces allowed |
                        +------------------------------------------------+

                        ''')
                    flag = False
            while(not flag):
                try:
                    bin2 = int(input("Enter second binary number: "))
                    if bin2>11111111:
                        print('''
                        +-------------------------------------------+
                        |                  ERROR                    |
                        +-------------------------------------------+
                        |Do not enter number greater than 11111111  |
                        +-------------------------------------------+

                        ''')
                        continue
                    if binaryValidate(str(bin2))==False:
                        print('''
                        +-------------------------------------------+
                        |                  ERROR                    |
                        +-------------------------------------------+
                        |            Enter either 0 or 1            |
                        +-------------------------------------------+

                        ''')
                        continue
                    bin_sum = bin1+bin2
                    if bin_sum>11111111:
                        print('''
                        +------------------------------------------------+
                        |                     ERROR                      |
                        +------------------------------------------------+
                        |The sum of two number must be less than 11111111|
                        +------------------------------------------------+

                        ''')
                    else:
                        con1 = convert(str(bin1))
                        decs = binToDec(bin1)
                        decss = binToDec(bin2)
                        con2 = convert(str(bin2))
                        binS = binToDec(bin_sum)
                        values = binBitAdder(bin1,bin2)
                        print(f'''
                        +-------------------------------------------+
                        |                Binary System              |
                        +---------------+---------------------------+
                        |   Variables   |           Output          |
                        +---------------+---------------------------+
                          First nummber |In 8-bit   - {con1}
                                        |In Decimal - {decs}
                        +-------------------------------------------+
                          Second number |In 8-bit   - {con2}
                                        |In Decimal - {decss}
                        +-------------------------------------------+
                          8-bit output  |In 8-bit   - {values}
                                        |In Decimal - {binS}
                        +---------------+---------------------------+
                        ''')
                        try:
                            resumes = False
                            while(not resumes):
                                inputResumes = input("Enter [Y/y] to continue or [N/n] to quit: ")
                                if inputResumes in ["Y","y"]:
                                    main()
                                elif inputResumes in ["N","n"]:
                                    return
                        except:
                            print("Enter either [Y/y] or [N/n]")
                            flag = True
                            break
                except:
                    print('''
                        +------------------------------------------------+
                        |                     ERROR                      |
                        +------------------------------------------------+
                        | No special characters and empty spaces allowed |
                        +------------------------------------------------+

                        ''')
                    flag = False
        else:
            print('''
                        +------------------------------------------------+
                        |                     ERROR                      |
                        +------------------------------------------------+
                        |  Please enter the correct key for data types   |
                        +------------------------------------------------+

                        ''')
main()
