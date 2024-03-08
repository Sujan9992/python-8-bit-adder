import strings
from adder import binary_adder, decimal_adder
from conversion import binary_to_decimal, convert_to_eight_bit, decimal_to_binary
from validation import check_binary, check_num, is_binary

welcome: str = "Welcome to the 8-bit Adder Program"
data_type: str = "Enter d/D for decimal or b/B for binary: "


def main() -> None:
    print(f"{welcome:-^60}")

    # flag: bool = False
    while True:
        try:
            dataType = input(data_type).strip()
        except EOFError:
            continue
        if dataType in ["d", "D"]:
            print(strings.decimal_info)
            while True:
                try:
                    decimal1 = int(input("Enter first decimal number: "))
                    if check_num(decimal1) == 1:
                        continue
                except ValueError:
                    print(strings.error3)
                    continue
                else:
                    break
            while True:
                try:
                    decimal2 = int(input("Enter second decimal number: "))
                    if check_num(decimal2) == 1:
                        continue
                    decimal_sum: int = decimal1 + decimal2
                    if decimal_sum > 255:
                        print(strings.info1)
                        continue
                except ValueError:
                    print(strings.error3)
                    continue
                else:
                    binary1 = int(decimal_to_binary(decimal1))
                    binary2 = int(decimal_to_binary(decimal2))
                    binary_sum = int(decimal_adder(decimal1, decimal2))
                    break
        elif dataType in ["b", "B"]:
            print(strings.binary_info)
            while True:
                try:
                    binary1 = int(input("Enter first binary number: "))
                    if is_binary(str(binary1)) is False:
                        print(strings.error7)
                        continue
                    if check_binary(binary1) == 1:
                        continue
                except ValueError:
                    print(strings.error3)
                    continue
                else:
                    break
            while True:
                try:
                    binary2 = int(input("Enter second binary number: "))
                    if is_binary(str(binary2)) is False:
                        print(strings.error7)
                        continue
                    if check_binary(binary2) == 1:
                        continue
                    binary_sum = binary1 + binary2
                    if binary_sum > 11111111:
                        print(strings.error6)
                        continue
                except ValueError:
                    print(strings.error3)
                    continue
                else:
                    binary1 = convert_to_eight_bit(str(binary1))
                    decimal1 = binary_to_decimal(binary1)
                    decimal2 = binary_to_decimal(binary2)
                    binary2 = convert_to_eight_bit(str(binary2))
                    binary_sum = int(binary_adder(binary1, binary2))
                    decimal_sum = binary_to_decimal(binary_sum)
                    break
        else:
            print(strings.error5)
            continue
        print_result(binary1, binary2, binary_sum, decimal1, decimal2, decimal_sum)
        if input("Enter [Y/y] to continue: ") not in ["Y", "y"]:
            break


def print_result(*args) -> None:
    print(f"""
    +-------------------------------------------+
    |                Binary System              |
    +-----------------+-------------------------+
    |   Variables     |         Output          |
    +-----------------+-------------------------+
        First number  |In 8-bit   - {args[0]}
                      |In Decimal - {args[3]}
    +-------------------------------------------+
        Second number |In 8-bit   - {args[1]}
                      |In Decimal - {args[4]}
    +-------------------------------------------+
        8-bit output  |In 8-bit   - {args[2]}
                      |In Decimal - {args[5]}
    +-----------------+-------------------------+
    """)


if __name__ == "__main__":
    main()
