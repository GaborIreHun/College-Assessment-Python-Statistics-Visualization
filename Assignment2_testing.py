from Assignment2_analytical_functions import *
from pytest import approx

test_list = [1,2,3,4,5]
test_list2 = [2,2,3,5,5]


def test_sum():
    assert calc_sum(test_list) == 15


def test_mean():
    assert calc_mean(test_list) == 3


def test_median():
    assert calc_median(test_list) == 3


def test_mode():
    assert calc_mode(test_list) == 1


def test_iqr():
    assert calc_iqr(test_list) == 3


def test_mode_skewness():
    assert calc_mode_skewness(test_list) == 1.2649110640673518


def test_correlation():
    assert calc_correlation(test_list, test_list2) == 0.7506518906054692
