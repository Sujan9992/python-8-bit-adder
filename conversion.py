def binary_to_decimal(num: int) -> int:
    value: int = 0
    power: int = 0
    while num > 0:
        value += 2**power * (num % 10)
        num //= 10
        power += 1
    return value


def decimal_to_binary(num: int) -> str:
    binary_list: list[str] = ["0"] * 8
    index: int = 7
    while num > 0:
        value = num % 2
        binary_list[index] = str(value)
        num //= 2
        index -= 1
    return "".join(binary_list)


def convert_to_eight_bit(string: str) -> int:
    eight_bit = string
    if len(string) != 8:
        for _ in range(len(string), 8):
            eight_bit = "0" + eight_bit
    return int(eight_bit)
