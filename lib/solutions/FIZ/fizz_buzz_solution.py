# noinspection PyUnusedLocal
def fizz_buzz(number):

    if number % 3 == 0 and number % 5 == 0:
        return "fizz buzz"
    
    if number % 3 == 0:
        return "fizz"

    if number % 5 == 0: 
        return "buzz"

    return str(number)

def test_fizzbuzz():
    assert(fizz_buzz(15), "fizz buzz")


def test_fizz():
    assert(fizz_buzz(6), "fizz")


def test_buzz():
    assert(fizz_buzz(10), "buzz")


def test_other():
    assert(fizz_buzz(2), "2")


