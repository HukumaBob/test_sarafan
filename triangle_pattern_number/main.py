
def triangle_pattern_number(number_of_elements: int) -> str:
    """
    Function to print the first n elements of the sequence 122333444455555...

    :param number_of_elements: The number of elements to print
    """

    sign = ''
    if number_of_elements < 0:
        sign = '-'
    triangle_sequence = sign + '\n'.join([str(digit)*digit for digit in range(1, abs(number_of_elements)+1)])
    return triangle_sequence


if __name__ == '__main__':
    n = int(input("Enter the number of elements: "))
    print(triangle_pattern_number(n))