import matplotlib.pyplot as plt


def histogram_for_numeric_columns(dictionary1, dictionary2):

    """
    Plot the histogram of 2 dictionaries.

    :param dictionary1: dictionary
    :param dictionary2: dictionary

    :return: none
    """
    fig, axs = plt.subplots(1, 2, figsize=(15, 10))

    fig.suptitle("Histogram of Height and Weight numeric columns")

    # Creating Histograms

    axs[0].set_title("Histogram of Height")

    axs[0].set_xlabel("Heights")

    bins = range(int(max(dictionary1.values()) + 2))

    axs[0].set_xticks(bins)

    axs[0].hist(dictionary1.values(), bins, ec="black")

    axs[0].xaxis.set_major_locator(plt.MaxNLocator(5))

    axs[0].ticklabel_format(useOffset=False)

    axs[1].set_title("Histogram of Weights")

    axs[1].set_xlabel("Weight")

    bins = range(int(max(dictionary2.values()) + 2))

    axs[1].set_xticks(bins)

    axs[1].hist(dictionary2.values(), bins, ec="black")

    plt.setp(axs[1].get_xticklabels(), rotation=90)

    axs[1].xaxis.set_major_locator(plt.MaxNLocator(5))

    axs[1].ticklabel_format(useOffset=False)

    plt.show()


def box_plot_for_numeric_columns(dictionary1, dictionary2):
    """
    Plot the box plot of 2 dictionaries.

    :param dictionary1: dictionary
    :param dictionary2: dictionary

    :return: none
    """
    fig, axs = plt.subplots(1, 2, figsize=(15, 10))

    # setting the title
    fig.suptitle("Box plot of Height and Weight numeric columns")

    # Creating Box Plots

    axs[0].set_title("Box Plot for heights")

    axs[0].set_ylabel("Heights")

    axs[0].boxplot(dictionary1.values(), showmeans=True, meanline=True)

    axs[1].set_title("Box Plot for weights")

    axs[1].set_ylabel("Weights")

    axs[1].boxplot(dictionary2.values(), showmeans=True, meanline=True)

    plt.show()


def scatter_plot_for_numeric_columns(list_1a, list_1b, list_2a, list_2b):
    """
    Plot the scatter plot for a pair of lists.

    :param list_1a: float, int
        A list of numbers.
    :param list_1b: float, int
        A list of numbers.
    :param list_2a: float, int
        A list of numbers.
    :param list_2b: float, int
        A list of numbers.

    :return: none
    """
    fig, axs = plt.subplots(1, 2, figsize=(15, 10))

    # setting the title
    fig.suptitle("Scatter plot of Height and Weight numeric columns")

    axs[0].set_xlabel("Height")

    axs[0].set_ylabel("Weight")

    axs[0].set_title("Scatter plot for Height vs Weight")

    axs[0].scatter(list_1a, list_1b, marker =".")

    axs[1].set_xlabel("Weight")

    axs[1].set_ylabel("Age")

    axs[1].set_title("Scatter plot for Weight vs Age")

    axs[1].scatter(list_2a, list_2b, marker=".")

    plt.show()


def pie_chart_for_values_in_each_sub_cat(dictionary):
    """
    Plot the pie plot for a dictionary.

    :param dictionary: key-value pair
        A dictionary.

    :return: none
    """
    fig, ax = plt.subplots(1)

    # setting the title
    fig.suptitle("Medal type distribution in the Olympic history")

    ax.pie(dictionary.values(), labels=dictionary.keys(), autopct="%.0f%%")

    plt.show()


def barh_chart_for_values_in_each_sub_cat(dictionary):
    """
   Plot the barh chart for a dictionary.

   :param dictionary: key-value pair
       A dictionary.

   :return: none
   """
    fig, ax = plt.subplots()

    # setting the title
    fig.suptitle("Medal type distribution in the Olympic history")

    # setting the x position
    y_pos = [i for i in range(len(dictionary))]

    # setting y tick labels
    ax.set_yticks(y_pos)
    ax.set_yticklabels(dictionary.keys())

    ax.set_ylabel("Medal type")
    ax.set_xlabel("Total number of medal")

    ax.barh(y_pos,dictionary.values(), align="center")

    plt.show()


def box_plot_for_val_in_each_sub_cat(dictionary):
    """
     Plot the box plot for a dictionary.

    :param dictionary: key-value pair
        A dictionary.

     :return: none
     """
    fig, ax = plt.subplots()

    ax.set_ylabel("Number of medal")

    ax.set_title("Medal type distribution in the Olympic history")

    ax.boxplot(dictionary.values())

    plt.show()




