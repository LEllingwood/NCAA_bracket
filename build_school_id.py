from tabulate import tabulate
import csv

# This function allows user to pick a name and get the school's unique id.
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

# This function calculates the total score for each team, with scores weighted based on importance of criteria(location - 1
# color - 2.25 mascot -3 )
    for line in data[1:]:
        school_score = float(line[5]) + float(line[7])*2.25 + float(line[9])*3
        print(school_score)