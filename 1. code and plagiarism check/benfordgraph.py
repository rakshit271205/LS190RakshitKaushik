import csv
import numpy as np
import matplotlib.pyplot as plt

benford_law = {1: 30.1, 2: 17.6, 3: 12.5, 4: 9.7, 5: 7.9, 6: 6.7, 7: 5.8, 8: 5.1, 9: 4.6}


def read_csv(path):
    all_values = []
    data = open(path, encoding="utf-8")
    csv_data = csv.reader(data)
    for num in csv_data:
        all_values.extend(num)
    return all_values


def get_first_digit(values_list):
    first_digits = []
    for num in values_list:
        first_digits.append(int(str(num)[0]))
    return first_digits


def assign_first_digits(digits_list):
    amount_first_digits = {}
    for i in range(1, 10):
        amount_first_digits[i] = digits_list.count(i)
    return amount_first_digits


def digits_percentage(digits_dic, lengt):
    first_digits_percentage = {}
    for i in range(1, 10):
        first_digits_percentage[i] = (float(digits_dic[i]) / lengt) * 100
    return first_digits_percentage


def show_graphs(assume, given):
    n = 19
    data_means = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, assume[1], assume[2], assume[3], assume[4], assume[5], assume[6], assume[7], assume[8], assume[9])
    benford_means = (given[1], given[2], given[3], given[4], given[5], given[6], given[7], given[8], given[9], 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    ind = np.arange(n)
    width = 0.50
    error = 0
    for i in range(1, 10):
        square = (given[i] - assume[i])*(given[i] - assume[i])
        error += square
    final_error = error/9
    final_error_root= np.sqrt(final_error)
    final_error_root_str = str(final_error_root)
    p1 = plt.bar(ind, benford_means, width)
    p2 = plt.bar(ind, data_means, width, bottom=benford_means)
    plt.ylabel('Percentages')
    plt.title("Benford Law Analysis with error "+final_error_root_str)
    plt.xticks(ind, ('1', '2', '3', '4', '5', '6', '7', '8', '9', '|', '1', '2', '3', '4', '5', '6', '7', '8', '9'))
    plt.yticks(np.arange(0, 40, 2.5))
    plt.legend((p1[0], p2[0]), ('Benford\'s', 'Our Data'))
    plt.show()

    


        


csv_list = read_csv('arizonaFraud.csv')
first_digit_list = get_first_digit(csv_list)
first_occurrence_dict = assign_first_digits(first_digit_list)
digits_percentage_dict = digits_percentage(first_occurrence_dict, len(first_digit_list))
show_graphs(digits_percentage_dict, benford_law)


