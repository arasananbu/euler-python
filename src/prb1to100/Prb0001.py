#!/usr/bin/python -tt


def Mul3or5(max):
    '''
    Mul3or5 - If we list all the natural numbers below 10 that are multiples of
              3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
              Find the sum of all the multiples of 3 or 5 below 1000.
    '''
    sum = 0
    for i in range(1, max):
        if (i % 3 == 0) or (i % 5 == 0):
            sum += i

    return 'sum of all the multiples of 3 or 5 below ' + str(max) + ' is ' + str(sum)


if __name__ == '__main__':
    print('Problem 0001: ' + Mul3or5(1000))
