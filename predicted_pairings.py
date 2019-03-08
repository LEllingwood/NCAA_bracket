import csv

with open('predicted_pairings.csv', 'w') as pairings_file:
    fieldnames = {'School 1', 'School 2', 'Conference'}

    csv_writer = csv.DictWriter(pairings_file, fieldnames=fieldnames)
    csv_writer.writeheader()

# West Conference
    csv_writer.writerow(
        {'School 1': 'Gonzaga', 'School 2': 'Sam Houston State', 'Conference': 'West'})
    csv_writer.writerow(
        {'School 1': "St. John's", 'School 2': 'NC State', 'Conference': 'West'})
    csv_writer.writerow({'School 1': 'Florida State',
                         'School 2': 'Belmont', 'Conference': 'West'})
    csv_writer.writerow(
        {'School 1': 'LSU', 'School 2': 'Lipscomb', 'Conference': 'West'})
    csv_writer.writerow(
        {'School 1': 'Buffalo', 'School 2': 'Florida', 'Conference': 'West'})
    csv_writer.writerow(
        {'School 1': 'Kansas', 'School 2': 'Montana', 'Conference': 'West'})
    csv_writer.writerow(
        {'School 1': 'Washington', 'School 2': 'Wofford', 'Conference': 'West'})
    csv_writer.writerow(
        {'School 1': 'Michigan', 'School 2': 'Texas State', 'Conference': 'West'})
    # csv_writer.writerow({'School 1': '_______', 'School 2': '_______', 'Conference': '_______________'})

# Midwest Conference

    csv_writer.writerow(
        {'School 1': 'Kentucky', 'School 2': 'Prairie View/Norfolk State', 'Conference': 'Midwest'})
    csv_writer.writerow(
        {'School 1': 'Louisville', 'School 2': 'Oklahoma', 'Conference': 'Midwest'})
    csv_writer.writerow({'School 1': 'Kansas State',
                         'School 2': 'Auburn/Clemson', 'Conference': 'Midwest'})
    csv_writer.writerow(
        {'School 1': 'Maryland', 'School 2': 'Hofstra', 'Conference': 'Midwest'})
    csv_writer.writerow(
        {'School 1': 'Iowa', 'School 2': 'Arizona State', 'Conference': 'Midwest'})
    csv_writer.writerow(
        {'School 1': 'Houston', 'School 2': 'UC Irvine', 'Conference': 'Midwest'})
    csv_writer.writerow(
        {'School 1': 'Villanova', 'School 2': 'TCU', 'Conference': 'Midwest'})
    csv_writer.writerow({'School 1': 'North Carolina',
                         'School 2': 'Loyola-Chicago', 'Conference': 'Midwest'})
    # csv_writer.writerow({'School 1': '_______', 'School 2': '_______', 'Conference': '_______________'})

# East Conference

    csv_writer.writerow(
        {'School 1': 'Duke', 'School 2': 'Bucknell', 'Conference': 'East'})
    csv_writer.writerow(
        {'School 1': 'Ole Miss', 'School 2': 'VCU', 'Conference': 'East'})
    csv_writer.writerow({'School 1': 'Iowa State',
                         'School 2': 'Ohio State/Alabama', 'Conference': 'East'})
    csv_writer.writerow(
        {'School 1': 'Nevada', 'School 2': 'Yale', 'Conference': 'East'})
    csv_writer.writerow({'School 1': 'Virginia Tech',
                         'School 2': 'Minnesota', 'Conference': 'East'})
    csv_writer.writerow({'School 1': 'Marquette', 'School 2': 'Vermont', 'Conference': 'East'})
    csv_writer.writerow(
        {'School 1': 'Baylor', 'School 2': 'UFC', 'Conference': 'East'})
    csv_writer.writerow({'School 1': 'Michigan State',
                         'School 2': 'Wright State', 'Conference': 'East'})
    # csv_writer.writerow({'School 1': '_______', 'School 2': '_______', 'Conference': '_______________'})

# South Conference

    csv_writer.writerow(
        {'School 1': 'Virginia', 'School 2': 'St. Francis PA/Iona', 'Conference': 'South'})
    csv_writer.writerow(
        {'School 1': 'Tennessee', 'School 2': 'Radford', 'Conference': 'South'})
    csv_writer.writerow(
        {'School 1': 'Purdue', 'School 2': 'S. Dakota St.', 'Conference': 'South'})
    csv_writer.writerow(
        {'School 1': 'Texas Tech', 'School 2': 'Old Dominion', 'Conference': 'South'})
    csv_writer.writerow(
        {'School 1': 'Wisconsin', 'School 2': 'New Mexico State', 'Conference': 'South'})
    csv_writer.writerow(
        {'School 1': 'Cincinnati', 'School 2': 'Seton Hall', 'Conference': 'South'})
    csv_writer.writerow({'School 1': 'Syracuse', 'School 2': 'Texas', 'Conference': 'South'})
    csv_writer.writerow({'School 1': 'Mississippi State',
                         'School 2': 'Temple', 'Conference': 'South'})
