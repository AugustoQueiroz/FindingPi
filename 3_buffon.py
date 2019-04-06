import sys
import random
import math

def buffon(l,t,n):
    # https://en.wikipedia.org/wiki/Buffon%27s_needle_problem
    # l: stick length
    # t: parallel lines t units apart
    # n: number of thrown sticks

    # probability P that a stick crosses a line
    # l <= t: P = 2*l/(t*pi) -> pi = 2*l/(t*P)
    # but h/n approximates P, so 2*l*n/(t*h) approximates pi,
    # where h is how many sticks crossed a parallel line.

    # normalizing to t = 1
    l = l/t
    t = 1
    if l <= t:
        h = 0

        for _ in range(n):
            x1,y1 = (random.random(), random.random())
            # y1 will be between 0 and 1,
            # y2 will be between 0+l and 1+l
            # so y2 will be at least -l = -t
            x2,y2 = x1,y1+l
            theta = random.random() * 2*math.pi

            xt2, yt2 = x2-x1, y2-y1
            
            # rotating second point to obtain randomly thrown line
            # xr2 isn't important.
            yr2 = xt2*math.sin(theta) + yt2*math.cos(theta)
            
            y2 = yr2 + y1

            if y1 > y2:
                y1,y2=y2,y1

            if (y1 <= -1 and -1 <= y2) or (y1 <= 0 and 0 <= y2) or (y1 <= 1 and 1 <= y2):
                h += 1
                
        return 2*l*n/(t*h)

    else:
        # I think this method only works if l <= t... but i'm not sure.
        return "I DON'T KNOW"

def get_args(args):
    if len(args) == 2:
        n_iterations = int(args[1])
        return [n_iterations]
    else:
        raise Exception("Oh Noes!")

if __name__ == "__main__":
    try:
        args = get_args(sys.argv)
        n = args[0]
        print('PI is equal-ish to',buffon(5/6,1,n))
    except TypeError:
        print("The first argument must be the number of iterations to be ran.")
        print("Correct usage: python3 3_buffon.py number_of_iterations")
    except Exception as e:
        print(e)
        print("One argument expected")
        print("Correct usage: python3 3_buffon.py number_of_iterarions")
