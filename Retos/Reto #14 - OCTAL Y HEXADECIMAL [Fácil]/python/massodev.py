"""Reto #14 - python.

/*
 * Crea una función que reciba un número decimal y lo trasforme a Octal
 * y Hexadecimal.
 * - No está permitido usar funciones propias del lenguaje de programación que
 * realicen esas operaciones directamente.
 */
"""


def get_input_number():
    """Ask the user for an integer number.

    Returns:
        int: number introduced by the user
    """
    while True:
        user_input = input("enter the number to transform: ")
        try:
            return int(user_input)
        except ValueError:
            print(f"{user_input!r} is not a number")


def int_2_base(number, base=16):
    """Transform a integer number into a different base representation.

    Supports any base up to hexadecimal(16), e.g. binary(2), octal(8), decimal(10)

    Args:
        number (int): integer number to transform
        base (int, optional): destination base. Defaults to 16.

    Raises:
        ValueError: if the base is not supported (2-16)

    Returns:
        str: number represented in the requested base
    """
    if base > 16 or base < 2:
        raise ValueError("Wrong base. Must be between 2 and 16")

    base_digits = "0123456789ABCDEF"
    result = ""

    while number >= 0:
        quotient = int(number / base)
        remainder = int(number % base)
        result = base_digits[remainder] + result
        number = quotient
        if number == 0:
            break
    return result


if __name__ == "__main__":
    number = get_input_number()
    number_in_hex = int_2_base(number, 16)
    number_in_oct = int_2_base(number, 8)
    print(
        f"{number!r} is {number_in_hex!r} in hexadecimal and {number_in_oct!r} in octal"
    )
