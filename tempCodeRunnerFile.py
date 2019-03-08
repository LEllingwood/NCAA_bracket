import csv

with open('predicted_pairings.csv', 'w') as pairings_file:
    fieldnames = {'School 1', 'School 2'}

    csv_writer = csv.DictWriter(pairings_file, fieldnames=fieldnames)
    csv_writer.writeheader()

    csv_writer.writerow({'School 1': 'Gonzaga', 'School 2': 'Sam Houston St.'})