from tabulate import tabulate
import csv

import matplotlib
import matplotlib.pyplot as plt


# This function allows user to pick a name and get the school's unique id and prints a table view of the complete list of teams.
def return_school_info():
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
                return {"school_name": line[1], "color1": line[6].split(", ")[0], "color2": line[6].split(", ")[1]}


def show_color(school_info):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    plt.text(2, 30, school_info["school_name"], fontsize=15,
             ha='left', color='white', va='top')
    rect1 = matplotlib.patches.Rectangle(
        (0, 0), 50, 50, color=school_info["color1"])
    rect2 = matplotlib.patches.Rectangle(
        (55, 0), 50, 50, color=school_info["color2"])
    print(school_info["color1"], school_info["color2"])    
    ax.add_patch(rect1)
    ax.add_patch(rect2)
    plt.xlim([-10, 120])
    plt.ylim([-10, 60])
    plt.show()

# show_color(school_name, '#2D0962', '#F8CD46')


if __name__ == "__main__":

    school_info = return_school_info()

    show_color(school_info)
