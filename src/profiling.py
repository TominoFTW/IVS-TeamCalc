#!/usr/bin/python
# -*- coding: utf-8 -*-

#import cProfile
from MathLib import MathLib
import random


def standard_deviation(nums):
    s = MathLib.root(MathLib.div(suma(nums), MathLib.sub(len(nums), 1)), 2)
    return s


def input_data(numbers, input):
    input = input.replace("\t", " ").split(" ")
    for i in input:
        if i != "":
            numbers.append(int(i))

    return numbers


def random_input(numbers):
    for i in range(random.randint(1000, 1001)):  # max number of input numbers
        numbers.append(random.randint(-1000, 1000))

    return numbers


def suma(numbers):
    sum = 0
    for i in numbers:
        sum = MathLib.add(MathLib.power(MathLib.sub(i, prumer(numbers)), 2), sum)

    return sum


def prumer(numbers):
    sum = 0
    for i in numbers:
        sum = MathLib.add(i, sum)

    return MathLib.div(sum, len(numbers))


if __name__ == '__main__':
    string = input("Zadejte cisla pro profiling oddelena mezerou (whitespace chars): ")
    numbers = []
    if string == "random":
        numbers = random_input(numbers)
    else:
        numbers = input_data(numbers, string)

    print("\nStandardni odchylka je:", standard_deviation(numbers))

    #cProfile.run('standard_deviation(nums)')
