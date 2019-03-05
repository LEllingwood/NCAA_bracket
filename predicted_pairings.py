import csv

with open('predicted_pairings.csv', 'w') as pairings_file:
    fieldnames = {'School 1', 'School 2'}

    csv_writer = csv.DictWriter(pairings_file, fieldnames=fieldnames)
    csv_writer.writeheader()

    csv_writer.writerow({'School 1': 'Gonzaga', 'School 2': 'Sam Houston St.'})
    csv_writer.writerow({'School 1': 'Duke', 'School 2': 'Bucknell'})
    csv_writer.writerow({'School 1': 'Virginia', 'School 2': 'St. Francis/Iona'})
    csv_writer.writerow({'School 1': 'Kentucky', 'School 2': 'Prairie View/Norfolk St.'})
    
    csv_writer.writerow({'School 1': 'Tennessee', 'School 2': 'Radford'})
    csv_writer.writerow({'School 1': 'North Carolina', 'School 2': 'Loyola-Chicago'})
    csv_writer.writerow({'School 1': 'Michigan State', 'School 2': 'Wright State'})
    csv_writer.writerow({'School 1': 'Michigan', 'School 2': 'Texas State'})

    csv_writer.writerow({'School 1': 'Houston', 'School 2': 'UC Irvine'})
    csv_writer.writerow({'School 1': 'Purdue', 'School 2': 'S. Dakota St.'})
    csv_writer.writerow({'School 1': 'Marquette', 'School 2': 'Vermont'})
    csv_writer.writerow({'School 1': 'Kansas', 'School 2': 'Montana'})

    csv_writer.writerow({'School 1': 'LSE', 'School 2': 'Lipscomb'})
    csv_writer.writerow({'School 1': 'Maryland', 'School 2': 'Hofstra'})
    csv_writer.writerow({'School 1': 'Texas Tech', 'School 2': 'Old Dominion'})
    csv_writer.writerow({'School 1': 'Nevada', 'School 2': 'Yale'})

    csv_writer.writerow({'School 1': 'Kansas State', 'School 2': 'Auburn/Clemson'})
    csv_writer.writerow({'School 1': 'Iowa State', 'School 2': 'Ohio St./Alabama'})
    csv_writer.writerow({'School 1': 'Florida State', 'School 2': 'Belmont'})
    csv_writer.writerow({'School 1': 'Wisconsin', 'School 2': 'New Mexico St.'})

    csv_writer.writerow({'School 1': 'Virginia Tech', 'School 2': 'Minnesota'})
    csv_writer.writerow({'School 1': 'Iowa', 'School 2': 'Arizona St.'})
    csv_writer.writerow({'School 1': 'Cincinnati', 'School 2': 'Seton Hall'})
    csv_writer.writerow({'School 1': 'Buffalo', 'School 2': 'Florida'})

    csv_writer.writerow({'School 1': 'Washington', 'School 2': 'Wofford'})
    csv_writer.writerow({'School 1': 'Baylor', 'School 2': 'UFC'})
    csv_writer.writerow({'School 1': 'Villanova', 'School 2': 'TCU'})
    csv_writer.writerow({'School 1': 'Syracuse', 'School 2': 'Texas'})

    csv_writer.writerow({'School 1': 'Mississippi State', 'School 2': 'Temple'})
    csv_writer.writerow({'School 1': 'Louisville', 'School 2': 'Oklahoma'})
    csv_writer.writerow({'School 1': "St. John's", 'School 2': 'NC St.'})
    csv_writer.writerow({'School 1': 'Ole Miss', 'School 2': 'VCU'})
    