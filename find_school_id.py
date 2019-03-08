# from tabulate import tabulate
# import csv

# This function allows user to pick a name and get the school's unique id and prints a table view of the complete list of teams.
# school_name = input("Enter a team name: ")

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