import csv

with open('complete_list.csv') as information:
    reader = csv.reader(information)
    reader = list(reader)

    with open('overall_score.csv', 'w') as overall_score:
        csv_writer = csv.writer(overall_score)

# This function calculates the total score for each team, with scores weighted based on importance of criteria(location - 1
# color - 2.25 mascot -3 )

        for line in reader[1:]:
            school_score = float(line[5]) + float(line[7])*2.25 + float(line[9])*3
            # print(school_score)
