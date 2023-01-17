from Assignment2_print_functions import *
from Assignment2_visualization_functions import *


def main():
    """
    The main method that initiates all necessary functions to run the application.

    :return:none
    """
    ######################################################################
    #            Analysing data from the appropriate csv file.           #
    ######################################################################

    # The first line of a file contains the column headings. The columns are
    #
    # Name - The name of the athlete
    # Sex - The gender of the athlete
    # Age - The age of the athlete
    # Height - The height of the athlete
    # Weight - The weight of the athlete
    # Team - The country the athlete is competing for
    # Year - The year of the competition
    # Season - The season of the competition
    # City - The city where the competition held
    # Sport - The specific sport the athlete competed in
    # Medal - The medal the athlete earned

    # creating lists for the columns
    names = []
    genders = []
    ages = []
    heights = []
    weights = []
    teams = []
    years = []
    seasons = []
    cities = []
    sports = []
    medals = []

    # creating dictionaries for relevant plotting and frequency tasks
    height_dict = {}
    weight_dict = {}
    medal_dict = {}
    team_dict = {}

    # name of subcategories
    subcategory1 = "Medal"
    subcategory2 = "Team"

    try:
        # opening csv file with read method
        with open("athlete_events_cleaned_assignment_2.csv", "r") as data_file:
            # reading the first row that contains the column names
            _ = data_file.readline()

            # initiating tasks for all remaining lines in the csv
            for line in data_file:

                try:
                    # splitting the line and assigning the appropriate value to the relevant variable
                    name, gender, age, height, weight, team, year, season, city, sport, medal = line.split(",")
                except ValueError:
                    print("Line has invalid format:", line)
                    continue
                try:
                    # populating the lists with the appropriate row values
                    names.append(name)
                    genders.append(gender)
                    ages.append(float(age))
                    heights.append(float(height))
                    weights.append(float(weight))
                    teams.append(team)
                    years.append(int(year))
                    seasons.append(season)
                    cities.append(city)
                    sports.append(sport)
                    medals.append(medal)

                    # populating the dictionaries with the appropriate row values
                    height_dict[name] = float(height)
                    weight_dict[name] = float(weight)

                    # validating values for dictionary population
                    if medal in medal_dict:
                        medal_dict[medal] += 1
                    else:
                        medal_dict[medal] = 1

                    # validating values for dictionary population

                    if team in team_dict:
                        team_dict[team] += 1
                    else:
                        team_dict[team] = 1

                except ValueError:
                    print("Invalid or missing number of members for", line)
                    continue

    except FileNotFoundError:
        print("Unable to open the file: athlete_events_cleaned_assignment.csv")

    print_welcome()

    ######################################################################
    #                     Running the main console.                      #
    ######################################################################

    while True:
        print_main_console_options()
        try:
            request = int(input("\nYour choice: "))
            if int(request) < 0 or int(request) > 2:
                print("Only values accepted from the console.")
                continue

        except ValueError:
            print("Please enter a valid request value.")
            continue

        if request == 1:
            ######################################################################
            #                  Running the analytical console.                   #
            ######################################################################
            while True:
                print_analytical_console_options()

                # requesting user input and validating it
                try:
                    request = int(input("\nYour choice: "))
                    if int(request) < 0 or int(request) > 17:
                        print("Only values accepted from the console.")
                        continue

                except ValueError:
                    print("Please enter a valid request value.")
                    continue

                match int(request):
                    case 0:
                        break
                    case 1:
                        print_numer_of_values(heights, weights)
                        continue
                    case 2:
                        print_sum_of_lists(heights, weights)
                        continue
                    case 3:
                        print_mean_of_lists(heights, weights)
                        continue
                    case 4:
                        print_median_of_lists(heights, weights)
                        continue
                    case 5:
                        print_mode_of_lists(heights, weights)
                        continue
                    case 6:
                        print_maximum_of_lists(heights, weights)
                        continue
                    case 7:
                        print_minimum_of_lists(heights, weights)
                        continue
                    case 8:
                        print_range_of_lists(heights, weights)
                        continue
                    case 9:
                        print_iq_range_of_lists(heights, weights)
                        continue
                    case 10:
                        print_standard_deviation_of_lists(heights, weights)
                        continue
                    case 11:
                        print_mode_skewness_of_lists(heights, weights)
                        continue
                    case 12:
                        print_correlation_of_lists(heights, weights)
                        continue
                    case 13:
                        print_number_of_distinct_values(medal_dict)
                        continue
                    case 14:
                        print_most_frequent_key_and_its_value(medal_dict, subcategory1)
                        continue
                    case 15:
                        print_least_frequent_key_and_its_value(medal_dict, subcategory1)
                        continue
                    case 16:
                        print_most_frequent_key_and_its_value(team_dict, subcategory2)
                        continue
                    case 17:
                        print_least_frequent_key_and_its_value(team_dict, subcategory2)
                        continue


        elif request == 2:
            while True:
                ######################################################################
                #               Running the visualization console.                   #
                ######################################################################
                print_visualization_console_options()

                # requesting user input and validating it
                try:
                    request = int(input("\nYour choice: "))
                    if int(request) < 0 or int(request) > 6:
                        print("Only values accepted from the console.")
                        continue

                except ValueError:
                    print("Please enter a valid request value.")
                    continue

                match int(request):
                    case 0:
                        break
                    case 1:
                        histogram_for_numeric_columns(height_dict, weight_dict)
                        continue
                    case 2:
                        box_plot_for_numeric_columns(height_dict, weight_dict)
                        continue
                    case 3:
                        scatter_plot_for_numeric_columns(heights, weights, weights, ages)
                        continue
                    case 4:
                        pie_chart_for_values_in_each_sub_cat(medal_dict)
                        continue
                    case 5:
                        barh_chart_for_values_in_each_sub_cat(medal_dict)
                        continue
                    case 6:
                        box_plot_for_val_in_each_sub_cat(medal_dict)
                        continue

        elif request == 0:
            print_goodbye()
            break
if __name__ == "__main__":
    main()
