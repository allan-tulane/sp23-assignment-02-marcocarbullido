"""
CMPS 2200  Assignment 2.
See assignment-02.pdf for details.
"""
import time
import tabulate
import matplotlib.pyplot as plt
import numpy as np

class BinaryNumber:
    """ done """
    def __init__(self, n):
        self.decimal_val = n
        self.binary_vec = list('{0:b}'.format(n))

    def __repr__(self):
        return('decimal=%d binary=%s' % (self.decimal_val, ''.join(self.binary_vec)))


def quadratic_multiply(x, y):
    return _quadratic_multiply(x, y).decimal_val


def _quadratic_multiply(x, y):
    x_vec = x.binary_vec
    y_vec = y.binary_vec
    x_vec, y_vec = pad(x_vec, y_vec)

    if x.decimal_val <= 1 and y.decimal_val <= 1:
        return BinaryNumber(x.decimal_val * y.decimal_val)

    x_left, x_right = split_number(x_vec)
    y_left, y_right = split_number(y_vec)

    x_L_times_y_L = _quadratic_multiply(x_left, y_left)
    x_R_times_y_R = _quadratic_multiply(x_right, y_right)
    x_L_times_y_R = _quadratic_multiply(x_left, y_right)
    x_R_times_y_L = _quadratic_multiply(x_right, y_left)

    middle = BinaryNumber(x_L_times_y_R.decimal_val + x_R_times_y_L.decimal_val)
    middle = bit_shift(middle, len(x_vec) // 2)

    x_L_times_y_L = bit_shift(x_L_times_y_L, len(x_vec))

    return BinaryNumber(x_L_times_y_L.decimal_val + middle.decimal_val + x_R_times_y_R.decimal_val)

def binary2int(binary_vec):
    if len(binary_vec) == 0:
        return BinaryNumber(0)
    return BinaryNumber(int(''.join(binary_vec), 2))

def split_number(vec):
    return (binary2int(vec[:len(vec)//2]),
            binary2int(vec[len(vec)//2:]))

def bit_shift(number, n):
    # append n 0s to this number's binary string
    return binary2int(number.binary_vec + ['0'] * n)

def pad(x,y):
    # pad with leading 0 if x/y have different number of bits
    # e.g., [1,0] vs [1]
    if len(x) < len(y):
        x = ['0'] * (len(y)-len(x)) + x
    elif len(y) < len(x):
        y = ['0'] * (len(x)-len(y)) + y
    # pad with leading 0 if not even number of bits
    if len(x) % 2 != 0:
        x = ['0'] + x
        y = ['0'] + y
    return x,y


def subquadratic_multiply(x, y):
    return _subquadratic_multiply(x, y).decimal_val


def _subquadratic_multiply(x, y):
    x_vec = x.binary_vec
    y_vec = y.binary_vec
    x_vec, y_vec = pad(x_vec, y_vec)
    if x.decimal_val <= 1 and y.decimal_val <= 1:
        return BinaryNumber(x.decimal_val * y.decimal_val)

    x_left, x_right = split_number(x_vec)
    y_left, y_right = split_number(y_vec)
    x_L_times_y_L = _subquadratic_multiply(x_left, y_left)
    x_R_times_y_R = _subquadratic_multiply(x_right, y_right)
    x_L_plus_x_R = BinaryNumber(x_left.decimal_val + x_right.decimal_val)
    y_L_plus_y_R = BinaryNumber(y_left.decimal_val + y_right.decimal_val)
    middle_term = BinaryNumber(_subquadratic_multiply(x_L_plus_x_R, y_L_plus_y_R).decimal_val - x_L_times_y_L.decimal_val - x_R_times_y_R.decimal_val)
    middle_term = bit_shift(middle_term, len(x_vec) // 2)
    x_L_times_y_L = bit_shift(x_L_times_y_L, len(x_vec))
    ret = BinaryNumber(x_L_times_y_L.decimal_val + middle_term.decimal_val + x_R_times_y_R.decimal_val)
    return ret

## Feel free to add your own tests here.
def test_multiply():
    assert quadratic_multiply(BinaryNumber(2), BinaryNumber(2)) == 2*2
    assert quadratic_multiply(BinaryNumber(4), BinaryNumber(4)) == 4*4
    assert quadratic_multiply(BinaryNumber(6), BinaryNumber(6)) == 6*6
    assert quadratic_multiply(BinaryNumber(8), BinaryNumber(8)) == 8*8

def test_subquadratic_multiply():
    assert subquadratic_multiply(BinaryNumber(2), BinaryNumber(2)) == 2*2
    assert subquadratic_multiply(BinaryNumber(4), BinaryNumber(4)) == 4*4
    assert subquadratic_multiply(BinaryNumber(6), BinaryNumber(6)) == 6*6
    assert subquadratic_multiply(BinaryNumber(8), BinaryNumber(8)) == 8*8



def time_multiply(x, y, f):
    start = time.time()
    result = f(x, y)
    return (time.time() - start) * 1000


def compare_multiply():
    results = []
    n_list = ([i*1000 for i in range(50)])

    for n in n_list:
        times = 10
        q_time = np.mean([time_multiply(BinaryNumber(n), BinaryNumber(n), quadratic_multiply) for i in range(times)])
        subq_time = np.mean([time_multiply(BinaryNumber(n), BinaryNumber(n), subquadratic_multiply) for i in range(times)])
        results.append((n, q_time, subq_time))
    print_results(results)

    plt.figure()
    plt.plot(n_list, [r[1] for r in results], 'o-', label='quadratic')
    plt.plot(n_list, [r[2] for r in results], 'o-', label='subquadratic')
    plt.show()


def print_results(results):
    print("\n")
    print(
        tabulate.tabulate(
            results,
            headers=['n', 'quadratic', 'subquadratic'],
            floatfmt=".3f",
            tablefmt="github"))

compare_multiply()
