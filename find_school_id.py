from tabulate import tabulate
import csv

import matplotlib
import matplotlib.pyplot as plt

# This function allows user to pick a name and get the school's unique id and prints a table view of the complete list of teams.
school_name = input("Enter a team name: ")

with open('complete_list.csv') as information:
    data = csv.reader(information)
    data = list(data)
    print(tabulate(data, tablefmt='grid'))
    for line in data:
        if line[1] == school_name:
            print('School Name: ', school_name)
            print('School ID: ', line[0])
            print('Conference: ', line[3])
            print('Location: ', line[4])
            print('Colors: ', line[6])
            print('Mascot: ', line[8])


def show_color(school_name, color1, color2):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    plt.text(2, 30, school_name, fontsize=15, ha='left', color='white', va='top')
    rect1 = matplotlib.patches.Rectangle((0, 0), 50, 50, color=color1)
    rect2 = matplotlib.patches.Rectangle((55, 0), 50, 50, color=color2)
    ax.add_patch(rect1)
    ax.add_patch(rect2)
    plt.xlim([-10, 120])
    plt.ylim([-10, 60])
    plt.show()

show_color(school_name, '#2D0962', '#F8CD46')