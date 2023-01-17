from Assignment2_analytical_functions import *


def print_welcome():
    """
    Print the welcome message.

    :return: none
    """
    print("#############################################################\n"
          "### Welcome and discover the 120 years of Olympic history ###\n"
          "#############################################################")


def print_goodbye():
    """
    Print the goodbye message.

    :return: none
    """
    print("#############################################################\n"
          "### Good bye and see you again soon - Slán agus beannacht ###\n"
          "#############################################################")


def print_main_console_options():
    """
    Print the main console options.

    :return: none
    """
    print("\n** Choose from the main categories **\n\n"
          "- 1: Analysis\n"
          "- 2: Visualization\n"
          "- 0: Exit")


def print_analytical_console_options():
    """
    Print the analytical console options.

    :return: none
    """
    print("\n** Choose an option for weights and heights analysis by entering the corresponding number **\n\n"
          "-  1: Print the number of values.\n"
          "-  2: Print the Total weight of all participants through the 120 years.\n"
          "-  3: Print the Mean.\n"
          "-  4: Print the Median.\n"
          "-  5: Print the Mode.\n"
          "-  6: Print the Maximum.\n"
          "-  7: Print the Minimum.\n"
          "-  8: Print the Range.\n"
          "-  9: Print the Inter-Quartile Range.\n"
          "- 10: Print the Standard Deviation.\n"
          "- 11: Print the Skewness.\n"
          "- 12: Print the Correlation.\n\n"
          "- 13: Print number of distinct values of Medals.\n"
          "- 14: Print most frequent medal and its frequency.\n"
          "- 15: Print least frequent medal and its frequency.\n"
          "- 16: Print Team with highest total and its total.\n"
          "- 17: Print Team with lowest total and its total.\n\n"
          "- 0: Back to the main menu.")


def print_visualization_console_options():
    """
    Print the visualization console options.

    :return: none
    """
    print("\n** Choose an option for visualization by entering the corresponding number **\n\n"
          "- 1: Histogram for weights and heights.\n"
          "- 2: Box plots for weights and heights.\n"
          "- 3: Scatter plot for weights and heights.\n"
          "- 4: Pie chart for sub-categories.\n"
          "- 5: Bar chart for sub-categories.\n"
          "- 6: Box plots for sub-categories.\n"
          "- 0: Back to the main menu.")


def print_numer_of_values(list1, list2):
    """
    Print the total amount of items of 2 list of numbers.

    :param list1: list (float, int)
        List of numbers.
    :param list2: list (float, int)
        List of numbers.

    :return: none
    """
    print("######################################################\n"
          "##                Number of values                  ##\n"
          "##--------------------------------------------------##\n"
          "##      Height: {}           Weight: {}       ##\n"
          "######################################################".format(len(list1),len(list2)))


def print_sum_of_lists(list1, list2):
    """
    Print the sum of the lists of numbers.

    :param list1: list (float, int)
        List of numbers.
    :param list2: list (float, int)
        List of numbers.

    :return: none
    """
    print("######################################################\n"
          "##             Total height and weight              ##\n"
          "##--------------------------------------------------##\n"
          "##    Height: {}cm     Weight: {}kg   ##\n"
          "######################################################".format(calc_sum(list1), calc_sum(list2)))


def print_mean_of_lists(list1, list2):
    """
    Print the mean of the lists of numbers.

    :param list1: list (float, int)
        List of numbers.
    :param list2: list (float, int)
        List of numbers.

    :return: none
    """
    print("######################################################\n"
          "##            Mean of height and weight             ##\n"
          "##--------------------------------------------------##\n"
          "##     Heights: {}cm        Weights: {}kg    ##\n"
          "######################################################".format("{:.2f}".format(calc_mean(list1)), "{:.2f}".format(calc_mean(list2))))


def print_median_of_lists(list1, list2):
    """
    Print the median of the lists of numbers.

    :param list1: list (float, int)
        List of numbers.
    :param list2: list (float, int)
        List of numbers.

    :return: none
    """
    print("######################################################\n"
          "##           Median of height and weight            ##\n"
          "##--------------------------------------------------##\n"
          "##        Height: {}cm      Weight: {}kg       ##\n"
          "######################################################".format(calc_median(list1), calc_median(list2)))


def print_mode_of_lists(list1, list2):
    """
    Print the mode of the lists of numbers.

    :param list1: list (float, int)
        List of numbers.
    :param list2: list (float, int)
        List of numbers.

    :return: none
    """
    print("######################################################\n"
          "##            Mode of height and weight             ##\n"
          "##--------------------------------------------------##\n"
          "##        Height: {}cm      Weight: {}kg       ##\n"
          "######################################################".format(calc_mode(list1), calc_mode(list2)))


def print_maximum_of_lists(list1, list2):
    """
    Print the maximum of the lists of numbers.

    :param list1: list (float, int)
        List of numbers.
    :param list2: list (float, int)
        List of numbers.

    :return: none
    """
    print("######################################################\n"
          "##           Maximum of height and weight           ##\n"
          "##--------------------------------------------------##\n"
          "##        Height: {}cm     Weight: {}kg       ##\n"
          "######################################################".format(calc_max(list1), calc_max(list2)))


def print_minimum_of_lists(list1, list2):
    """
    Print the minimum of the lists of numbers.

    :param list1: list (float, int)
        List of numbers.
    :param list2: list (float, int)
        List of numbers.

    :return: none
    """
    print("######################################################\n"
          "##           Minimum of height and weight           ##\n"
          "##--------------------------------------------------##\n"
          "##        Height: {}cm     Weight: {}kg        ##\n"
          "######################################################".format(calc_min(list1), calc_min(list2)))


def print_range_of_lists(list1, list2):
    """
    Print the range of the lists of numbers.

    :param list1: list (float, int)
        List of numbers.
    :param list2: list (float, int)
        List of numbers.

    :return: none
    """
    print("######################################################\n"
          "##            Range of height and weight            ##\n"
          "##--------------------------------------------------##\n"
          "## Height: {}cm Weight: {}kg ##\n"
          "######################################################".format(calc_range(list1), calc_range(list2)))


def print_iq_range_of_lists(list1, list2):
    """
    Print the inter-quartile-range of the lists of numbers.

    :param list1: list (float, int)
        List of numbers.
    :param list2: list (float, int)
        List of numbers.

    :return: none
    """
    print("######################################################\n"
          "##     Inter-Quartile Range of height and weight    ##\n"
          "##--------------------------------------------------##\n"
          "##         Height: {}cm      Weight: {}kg       ##\n"
          "######################################################".format(calc_iqr(list1), calc_iqr(list2)))


def print_standard_deviation_of_lists(list1, list2):
    """
    Print the standard deviation of the lists of numbers.

    :param list1: list (float, int)
        List of numbers.
    :param list2: list (float, int)
        List of numbers.

    :return: none
    """
    print("\n--- Please wait, this might take a while ---\n")
    print("######################################################\n"
          "##      Standard Deviation of height and weight     ##\n"
          "##--------------------------------------------------##\n"
          "##          Height: {}      Weight: {}        ##\n"
          "######################################################".format("{:.2f}".format(calc_std_dev(list1)), "{:.2f}".format(calc_std_dev(list2))))


def print_mode_skewness_of_lists(list1, list2):
    """
    Print the mode skewness of the lists of numbers.

    :param list1: list (float, int)
        List of numbers.
    :param list2: list (float, int)
        List of numbers.

    :return: none
    """
    print("\n--- Please wait, this might take a while ---\n")
    print("######################################################\n"
          "##         Mode Skewness of height and weight       ##\n"
          "##--------------------------------------------------##\n"
          "##          Height: {}       Weight: {}        ##\n"
          "######################################################".format("{:.2f}".format(calc_mode_skewness(list1)), "{:.2f}".format(calc_mode_skewness(list2))))


def print_correlation_of_lists(list1, list2):
    """
    Print the correlation between the lists of numbers.

    :param list1: list (float, int)
        List of numbers.
    :param list2: list (float, int)
        List of numbers.

    :return: none
    """
    print("\n--- Please wait, this might take a while ---\n")
    print("######################################################\n"
          "##       Correlation between height and weight      ##\n"
          "##--------------------------------------------------##\n"
          "##                       {}                      ##\n"
          "######################################################".format("{:.3f}".format(calc_correlation(list1, list2))))


def print_number_of_distinct_values(dictionary):
    """
    Print the number of distinct sub-categories.

    :param dictionary: key-value pairs
        A dictionary.

    :return: none
    """
    print("######################################################\n"
          "##    Number of distinct sub-categories in Medals   ##\n"
          "##--------------------------------------------------##\n"
          "##                        {}                         ##\n"
          "######################################################".format(len(dictionary.keys())))


def print_most_frequent_key_and_its_value(dictionary, subcategory):
    """
    Print the most frequent key and its corresponding value.

    :param subcategory: string
        Name of subcategory.
    :param dictionary: key-value pairs
        A dictionary.

    :return: none
    """
    print("\n"
          "           Most frequent {} and its value          \n"
          "  --------------------------------------------------\n"
          "  Type of {}: {}  Its frequency: {}               \n"
          "".format(subcategory, subcategory, max(dictionary, key=dictionary.get), max(dictionary.values())))


def print_least_frequent_key_and_its_value(dictionary, subcategory):
    """
    Print the least frequent key and its corresponding value.

    :param subcategory: string
        Name of subcategory.
    :param dictionary: key-value pairs
        A dictionary.

    :return: none
    """
    print("\n"
          "           Least frequent {} and its value           \n"
          "  --------------------------------------------------\n"
          "  Type of {}: {}  Its frequency: {}               \n"
          "".format(subcategory, subcategory, min(dictionary, key=dictionary.get), min(dictionary.values())))