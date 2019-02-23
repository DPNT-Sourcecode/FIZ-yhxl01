# noinspection PyUnusedLocal
def fizz_buzz(number):

    is_fizz = False
    is_buzz = False

    if number % 3 == 0 or "3" in str(number):
        is_fizz = True
    
    if number % 5 == 0 or "5" in str(number):
        is_buzz = True

    if is_fizz and is_buzz:
        return "fizz buzz"
    elif is_fizz:
        return "fizz"
    elif is_buzz:
        return "buzz"
    else:
        return str(number)


def test_fizzbuzz():
    assert(fizz_buzz(30), "fizz buzz")


def test_fizz():
    assert(fizz_buzz(23), "fizz")


def test_buzz():
    assert(fizz_buzz(10), "buzz")


def test_other():
    assert(fizz_buzz(2), "2")



