from conversion import decimal_to_binary
from gates import and_gate, xor_gate


def binary_adder(a: int, b: int) -> str:
    str_list: list[str] = ["0"] * 8
    i = 7
    carry = 0
    num = max(a, b)
    while num > 0:
        a1 = a % 10
        b1 = b % 10

        # sumAdder operation
        xor_first = xor_gate(a1, b1)
        sum_adder = xor_gate(xor_first, carry)

        # carryout operation
        and_first = and_gate(a1, b1)
        and_second = and_gate(xor_first, carry)
        carry = xor_gate(and_first, and_second)

        str_list[i] = str(sum_adder)
        i -= 1
        num //= 10
        a //= 10
        b //= 10
    if i >= 0:
        str_list[i] = str(carry)
    return "".join(str_list)


# Converting decimal number to 8-bit adder
def decimal_adder(a: int, b: int) -> str:
    dec_a = int(decimal_to_binary(a))
    dec_b = int(decimal_to_binary(b))
    return binary_adder(dec_a, dec_b)
