def reversed(number):
    result = 0

    while number > 0:
        digit = number % 10
        result = result * 10 + digit
        number = number // 10

    return result

def formatter(number):
    return bin(number), oct(number)
