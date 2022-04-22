#!/usr/bin/python
# -*- coding: utf-8 -*-

##
# @package MathLib
# Mathematical library for calculator.

##
# @brief Class for library of mathematical operations.
class MathLib:

    ##
    # @brief      Adds two numbers
    # @param      a addend
    # @param      b addend
    # @return     The sum of a and b
    @staticmethod
    def add(a, b):
        return a + b

    ##
    # @brief      Subtracts two numbers
    # @param      a minuend
    # @param      b subtrahend
    # @return     The difference of a and b
    @staticmethod
    def sub(a, b):
        return a - b

    ##
    # @brief      Multiplies two numbers
    # @param      a multiplicand
    # @param      b multiplier
    # @return     The product of a and b
    @staticmethod
    def mul(a, b):
        return a * b

    ##
    # @brief      Divides two numbers
    # @param      a dividend
    # @param      b divisor
    # @exception  ValueError If b is 0
    # @return     The quotient of a and b
    @staticmethod
    def div(a, b):
        if (b == 0):
            raise ValueError("MathError")
        if a % b == 0:
            return a / b
        return float(a) / b

    ##
    # @brief      Calculates the factorial of a number  
    # @param      n number to calculate factorial of
    # @exception  ValueError If the number is negative nor integer
    # @return     factorial of the number
    @staticmethod
    def factorial(n):
        if type(n) != int or n <0 :
            raise ValueError("MathError")
        if n == 0:
            return 1
        else:
            return n * MathLib.factorial(n - 1)

    ##
    # @brief      Calculates the power of a number
    # @param      base the base of the power
    # @param      exponent the exponent of the power
    # @exception  ValueError If the exponent is negative nor integer
    # @return     power of the base to the exponent
    @staticmethod
    def power(base, exponent):
        if type(exponent) != int or exponent < 0:
            raise ValueError("MathError")
        else:
            return round(base ** exponent, 6)

    ##
    # @brief      Calculates the root of a number
    # @param      base the base of the root
    # @param      root the value of the root
    # @exception  ValueError if the base is negative
    # @return     root of base
    @staticmethod
    def root(base, root):
        if base <= 0:
            raise ValueError("MathError")
        else:
            return round(base ** round(1/root,6), 6)

    ##
    # @brief      Calculates the absolute value of a number
    # @param      n number to calculate the absolute value of
    # @return     absolute value of the number
    @staticmethod
    def abs(n):
        if n < 0:
            return -n
        else:
            return n
