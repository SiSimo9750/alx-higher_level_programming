def print_last_digit(number):
    if number < 0:
        last_dig = (number * -1) % 10
    else:
        last_dig = number % 10
    print(last_dig, end="")
    return last_dig
