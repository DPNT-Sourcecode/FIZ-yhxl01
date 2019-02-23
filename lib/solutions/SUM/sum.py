#!/usr/bin/env python

import pytest


def sum(intA, intB):
    """Add two integers, both with value between 0-100

    :param intA: First integer to add
    :type intA: int
    :param intB: Second integer to add
    :type intB: int
    :return: The sum of the parameters
    :rtype: int
    """
    assert (intA >= 0), "Negative values out of bounds"
    assert (intB >= 0), "Negative values out of bounds"
    assert (intA <= 100), "Max allowed value 100"
    assert (intB <= 100), "Max allowed value 100"

    return intA + intB


def test_sum_basic():
    """Basic test of sum function
    """
    assert sum(10, 10) == 20
    

def test_sum_negative():
    """Test that negative input raises AssertionError
    """
    with pytest.raises(AssertionError):
        sum(-1,1)


def test_sum_gt100():
    """Test that input over 100 raises AssertionError
    """
    with pytest.raises(AssertionError):
        sum(101, 1)
