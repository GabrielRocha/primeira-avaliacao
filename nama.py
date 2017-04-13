import settings


def is_multiples(number):
    """Verify if the number is mulples of MULTIPLES values"""
    for multiply in sorted(settings.MULTIPLES.keys(), reverse=True):
        if number % multiply == 0:
            return settings.MULTIPLES.get(multiply)
    return str(number)


def nama_numbers():
    """Return a string with number and respective word of multiples.

    The first values of the even indices will be incremented by '.'
    in relation to the size of the previous index plus 1 and
    the latest values will be add "."
    in relation of items from your list plus 1
    """
    result = []
    for numbers in settings.RANGE_PRINT:
        index = settings.RANGE_PRINT.index(numbers)
        list_numbers = [is_multiples(digit) for digit in numbers]
        if (index+1) % 2 == 0:
            tag_begin = (str((len(settings.RANGE_PRINT[index-1])+1) * "."))
            tag_end = (str((len(numbers)+1) * "."))
            list_numbers[0] = "{} {}".format(tag_begin, list_numbers[0])
            list_numbers[-1] = "{} {}".format(list_numbers[-1], tag_end)
        result += list_numbers
    return ", ".join(result)


if __name__ == '__main__':
    print(nama_numbers())
