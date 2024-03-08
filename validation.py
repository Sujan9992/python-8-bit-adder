import strings


def is_binary(num: str) -> bool:
    for digit in num:
        if digit not in "01":
            return False
    return True


def check_num(num: int) -> int:
    match num:
        case num if num > 255:
            print(strings.error1)
            return 1
        case num if num < 0:
            print(strings.error2)
            return 1
        case _:
            return 0


def check_binary(num: int) -> int:
    match num:
        case num if num > 11111111:
            print(strings.error4)
            return 1
        case num if num < 0:
            print(strings.error2)
            return 1
        case _:
            return 0
