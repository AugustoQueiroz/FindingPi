# -*- coding: utf-8 -*-
import sys # Used for getting the arguments from the command line
import random # Used for... well, generating random numbers

def get_args(args):
    if len(args) == 2:
        try:
            n_iterations = int(args[1])
            return [n_iterations]
        except TypeError:
            print("The first argument must be the number of iterations")
            print("Correct usage: python 2_monte_carlo.py [number of iterations]")
            return -1
    else:
        print("One argument expected, none given")
        print("Correct usage: python 2_monte_carlo.py [number of iterarions]")
        return -1

def find_pi(n_iterations, side_of_square = 1):
    r = side_of_square / 2.0
    in_circle_points_count = 0

    for _ in range(n_iterations):
        x = random.uniform(-r, r)
        y = random.uniform(-r, r)
        if x*x + y*y < r*r: in_circle_points_count += 1

    p = float(in_circle_points_count) / float(n_iterations)
    pi = 4 * p
    return pi

if __name__ == "__main__":
    args = get_args(sys.argv)
    if args != -1:
        n_iterations = args[0]
        print(find_pi(n_iterations))
