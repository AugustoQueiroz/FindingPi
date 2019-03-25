# -*- coding: utf-8 -*-
import sys # Used for getting command line arguments
import random # Used for... well, generating random numbers
from math import sqrt # Used to get the sqrt of a number
from fractions import gcd # Used to check if two numbers are co-primes

def get_args(args):
    # Accept:
    # 1_random_numbers.py [number of iterations to run]
    if len(args) != 2:
        print("Missing number of iterations to be ran")
        print("Correct usage: python 1_random_numbers.py [number of iterations to run]")
        return -1
    else:
        try: 
            n_iterations = int(args[1])
            return [int(args[1])]
        except TypeError:
            print("The first argument must be the number of iterations to be ran.")
            print("Correct usage: python 1_random_numbers.py [number of iterations to run]")
            return -1

def find_pi(n_iterations, low_bound = 0, up_bound = 999999999):
    coprime_count = 0

    for x in range(n_iterations):
        a = random.randint(low_bound, up_bound)
        b = random.randint(low_bound, up_bound)
        if gcd(a, b) == 1: coprime_count += 1

    p = float(coprime_count) / float(n_iterations)
    pi = sqrt(6/p)
    return pi

if __name__ == "__main__":
    args = get_args(sys.argv)
    if args != -1:
        n_iterations = args[0]
        print(find_pi(n_iterations))
