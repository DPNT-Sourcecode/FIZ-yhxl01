# noinspection PyUnusedLocal
def fizz_buzz(number):
    """A method for deciding if an input is a fizz, buzz, deluxe, fake deluxe, a combination of these categories, or none of the above.

    :param number: The number for testing
    :type number: integer
    :return: The Fizz, Buzz, Deluxe status
    :rtype: str
    """
    status_list = []

    if number % 3 == 0 or "3" in str(number):
        status_list.append("fizz")
    
    if number % 5 == 0 or "5" in str(number):
        status_list.append("buzz")

    if (number % 3 == 0 and "3" in str(number)) or (number % 5 == 0 and "5" in str(number)):
        if number % 2 != 0:
            status_list.append("fake deluxe")
        else:
            status_list.append("deluxe")


    if len(status_list) == 0: 
        return str(number)
    else:
        return " ".join(status_list)


def test_fizzbuzz():
    assert(fizz_buzz(358), "fizz buzz")


def test_fizz():
    assert(fizz_buzz(23), "fizz")


def test_buzz():
    assert(fizz_buzz(10), "buzz")


def test_deluxe():
    assert(fizz_buzz(30), "deluxe")


def test_fake_deluxe():
    assert(fizz_buzz(55), "fake deluxe")


def test_fizz_buzz_deluxe():
    assert(fizz_buzz(555), "fizz buzz deluxe")

def test_other():
    assert(fizz_buzz(2), "2")

