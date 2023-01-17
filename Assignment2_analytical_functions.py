
def calc_sum(numbers):
    """
        Calculate the sum of a list of numbers.

        :param numbers: float, int
            List of numbers.

        :return: float
            The sum of a list of numbers.
    """
    return sum(numbers)


def calc_mean(numbers):
    """
    Calculate the mean of a list of numbers.

    :param numbers: float, int
        List of numbers.

    :return: float
        The mean of a list of numbers.
    """
    return sum(numbers) / len(numbers)


def calc_median(numbers):
    """
    Calculate the median of a list of numbers.

    :param numbers: float, int
        List of numbers.

    :return: float, int
        The mean of a list of numbers.
    """
    numbers.sort()
    if len(numbers) % 2 == 0:
        med1 = numbers[len(numbers) // 2]
        med2 = numbers[len(numbers) // 2 - 1]
        return (med1 + med2) / 2
    else:
        return numbers[len(numbers) // 2]


def calc_mode(numbers):
    """
    Calculate the mode of a list of numbers.

    :param numbers: float, int
        List of numbers.

    :return: float, int
        The mode of a list of numbers.
    """
    uniques = sorted(set(numbers))
    frequencies = [numbers.count(value) for value in uniques]
    max_frequencies = max(frequencies)
    max_freq_index = frequencies.index(max_frequencies)

    return uniques[max_freq_index]


def calc_max(numbers):
    """
        Calculate the maximum of a list of numbers.

        :param numbers: float, int
            List of numbers.

        :return: float
            The maximum of a list of numbers.
    """
    return max(numbers)


def calc_min(numbers):
    """
        Calculate the minimum of a list of numbers.

        :param numbers: float, int
            List of numbers.

        :return: float
            The minimum of a list of numbers.
    """
    return min(numbers)


def calc_range(numbers):
    """
        Calculate the range of a list of numbers.

        :param numbers: float, int
            List of numbers.

        :return: float
            The range of a list of numbers.
    """
    return min(numbers), max(numbers)


def calc_iqr(numbers):
    """
    Calculate the Inter quartile Range of a list of numbers.

    :param numbers: float, int
        List of numbers.

    :return: float
        The Inter quartile Range of a list of numbers.
    """
    numbers.sort()
    mid_index = int(len(numbers) / 2)

    # defining the half point according to an even or odd length of list
    if len(numbers) % 2 == 0:
        lower_half = numbers[:mid_index]
        upper_half = numbers[mid_index:]
    else:
        lower_half = numbers[:mid_index]
        upper_half = numbers[mid_index + 1:]

    # calculating quadrilles
    q1 = calc_median(lower_half)
    q3 = calc_median(upper_half)

    return q3 - q1


def calc_std_dev(numbers):
    """
    Calculate the standard deviation of a list of numbers.

    :param numbers: float, int
        List of numbers.

    :return: float
        The standard deviation of a list of numbers.
    """
    return (sum((x - (calc_mean(numbers))) ** 2 for x in numbers) / (len(numbers) - 1)) ** 0.5


def calc_median_skewness(numbers):
    """
    Calculate the median skewness of a list of numbers.

    :param numbers: float, int
        List of numbers.

    :return: float
        The median skewness of a list of numbers.
    """
    return 3 * (calc_mean(numbers) - calc_median(numbers)) / calc_std_dev(numbers)


def calc_mode_skewness(numbers):
    """
    Calculate the mode skewness of a list of numbers.

    :param numbers: float, int
        List of numbers.

    :return: float
        The mode skewness of a list of numbers.
    """
    return (calc_mean(numbers) - calc_mode(numbers)) / calc_std_dev(numbers)


def calc_correlation(numbers1, numbers2):
    """
    Calculate the correlation between lists of numbers.

    :param numbers1: float, int
        List of numbers.
    :param numbers2: float, int
        List of numbers.

    :return: float
        The correlation between lists of numbers.
    """
    # establishing the means and standard deviations for both lists.
    x_mean = calc_mean(numbers1)
    y_mean = calc_mean(numbers2)
    x_stand_dev = calc_std_dev(numbers1)
    y_stand_dev = calc_std_dev(numbers2)

    # calculating covariance
    covariance = sum((a - x_mean) * (b - y_mean) for (a, b) in zip(numbers1, numbers2)) / len(numbers1)

    # returning the correlation
    return covariance/(x_stand_dev*y_stand_dev)





