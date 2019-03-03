import csv

with open('beginning_predictions.csv', 'w', newline='') as f:
    thewriter = csv.writer(f)

    thewriter.writerow(['Rank', 'West', 'Midwest', 'East', 'South'])
    thewriter.writerow(['1', 'Gonzaga', 'Kentucky', 'Duke', 'Virginia'])
    thewriter.writerow(['16' 'Sam Houston St.', 'Prairie View/Norfolk St.' 'Bucknell', 'St. Francis/Iona'])
    thewriter.writerow(['  ', '  ', '  ', '  '])

    thewriter.writerow(['8', "St. John's", 'Louisville', 'Ole Miss', 'Mississippi St.'])
    thewriter.writerow(['9', 'NC St.', 'Oklahoma', 'VCU', 'Temple'])
    thewriter.writerow(['  ', '  ', '  ', '  '])

    thewriter.writerow(['5', 'Florida St.', 'Kansas St.', 'Iowa St.', 'Wisconsin'])
    thewriter.writerow(['12', 'Belmont', 'Auburn/Clemson', 'Ohio St./Alabama', 'New Mexico St.'])
    thewriter.writerow(['  ', '  ', '  ', '  '])

    thewriter.writerow(['4', 'LSU', 'Maryland', 'Nevada', 'Texas Tech'])
    thewriter.writerow(['13', 'Lipscomb', 'Hofstra','Yale', 'Old Dominion'])
    thewriter.writerow(['  ', '  ', '  ', '  '])

    thewriter.writerow(['6', 'Buffalo',	'Iowa',	'Virginia Tech', 'Cincinnati'])
    thewriter.writerow(['11', 'Florida', 'Arizona St.',	'Minnesota', 'Seton Hall'])
    thewriter.writerow(['  ', '  ', '  ', '  '])
    
    thewriter.writerow(['3', 'Kansas', 'Houston', 'Marquette', 'Purdue'])
    thewriter.writerow(['14', 'Montana', 'UC Irvine', 'Vermont', 'S. Dakota St.'])
    thewriter.writerow(['  ', '  ', '  ', '  '])

    thewriter.writerow(['7', 'Washington', 'Villanova', 'Baylor', 'Syracuse'])
    thewriter.writerow(['10', 'Wofford', 'TCU', 'UCF', 'Texas'])
    thewriter.writerow(['  ', '  ', '  ', '  '])

    thewriter.writerow(['2', 'Michigan', 'North Carolina', 'Michigan St.', 'Tennessee'])
    thewriter.writerow(['15', 'Texas St.', 'Loyola-Chicago', 'Wright St.', 'Radford'])


