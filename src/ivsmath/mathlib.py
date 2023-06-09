#!/usr/bin/env python
# -*- coding: utf-8 -*-

##
# @package ivsmath
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
    def factorial(n, _=0):
        if type(n) != int or n < 0 :
            raise ValueError("MathError")
        if n == 0:
            return 1
        else:
            return n * MathLib.factorial(n - 1)

    ##
    # @brief      Calculates power of a number
    # @param      base base of the power
    # @param      exponent exponent of the power
    # @exception  ValueError If the exponent is negative nor integer
    # @return     power of the base to the exponent
    @staticmethod
    def power(base, exponent):
        if type(exponent) != int or exponent < 0:
            raise ValueError("MathError")
        else:
            return round(base ** exponent, 5)

    ##
    # @brief      Calculates the root of a number
    # @param      base the base of the root
    # @param      root the value of the root
    # @exception  ValueError if the base is negative
    # @return     root of base
    @staticmethod
    def root(root, base):
        if base < 0 or root == 0:
            raise ValueError("MathError")
        else:
            return round(base ** round(1/root,6), 5)

    ##
    # @brief      Calculates the modulo of a number
    # @param      a number dividend
    # @param      b number divisor
    # @exception  ValueError If b is 0
    # @return     modulo of the number
    @staticmethod
    def mod(a, b):
        if b == 0:
            raise ValueError("MathError")
        return MathLib.sub(a, MathLib.mul(a // b, b))
