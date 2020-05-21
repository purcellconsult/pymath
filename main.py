"""
This is the file in which
we'll test the functions that
we'll created in basic_math.py
"""
import basic_math

if __name__ == '__main__':
    add1 = basic_math.add(10, 100)
    subtract1 = basic_math.subtract(100, 10)
    multiply1 = basic_math.multiply(10, 10**2)
    divide1 = basic_math.divide(9, 3)
    print('add1={} subtract1={} multiply1={} divide1 = '
          '{}'.format(add1, subtract1, multiply1, divide1))