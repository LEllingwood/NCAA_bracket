import csv

with open('preliminary_pairings.csv', 'w') as pairings_file:
    fieldnames = {'School 1', 'School 2'}

    csv_writer = csv.DictWriter(pairings_file, fieldnames=fieldnames)
    csv_writer.writeheader()

    csv_writer.writerow({'School 1': 'Prairie View', 'School 2': 'Norfolk'})
    csv_writer.writerow({'School 1': 'St. Francis', 'School 2': 'Iona'})
    csv_writer.writerow({'School 1': 'Auburn', 'School 2': 'Clemson'})
    csv_writer.writerow({'School 1': 'Ohio St.', 'School 2': 'Alabama'})