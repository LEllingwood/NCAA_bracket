import csv


def main():
    # read prelim pairings csv file and append schools 1 and 2 to the empty list
    prelim_schools = []
    with open('preliminary_pairings.csv') as prelim:
        csv_reader1 = csv.DictReader(prelim)
        for row in csv_reader1:
            prelim_schools.append(row['School 1'])
            prelim_schools.append(row['School 2'])
    # print("line 12", prelim_schools)

    # create empty dict into which we will read through each row of the complete list data and append the school name and three rank criteria
    prelim_dict = {}
    full_dict = {}

    with open('complete_list.csv') as f:
        csv_reader = csv.DictReader(f)
        for row in csv_reader:
            # full_dict.append(row)
            full_dict[row['School']] = [int(row['Location Rank']),
                                        int(row['Color Rank']), int(row['Mascot Rank'])]
            full_dict[row['School']].append(calc_overal_score(full_dict[row['School']]))
            if row['School'] in prelim_schools:
                prelim_dict[row['School']] = [int(row['Location Rank']),
                                              int(row['Color Rank']), int(row['Mascot Rank'])]
    # print("line 23", prelim_dict)
    print('line26', full_dict)

    # for loop to run through the ranks and calculate the score
    for key in prelim_dict.keys():
        prelim_dict[key].append(calc_overal_score(prelim_dict[key]))
    # print("line 28", prelim_dict)

# create a wildcard schools list into which the winner of each of four pairings will be appended.
    wildcard_schools = []

    with open('preliminary_pairings.csv') as prelim:
        csv_reader = csv.DictReader(prelim)
        for row in csv_reader:
            wildcard_schools.append(row['School 1'] if prelim_dict[row['School 1']]
                                    [-1] > prelim_dict[row['School 2']][-1] else row['School 2'])
    # print ('line 38', wildcard_schools)

    with open('predicted_pairings.csv') as rfile:
        with open('first_round.csv', 'w') as wfile:

            csv_reader = csv.DictReader(rfile)

            fieldnames = {'School 1', 'School 2', 'Conference'}

            csv_writer = csv.DictWriter(wfile, fieldnames=fieldnames)
            csv_writer.writeheader()

            for row in csv_reader:
                if "/" in row["School 2"]:
                    for school in wildcard_schools:
                        if row["School 2"].find(school) != -1:
                            row["School 2"] = school
                            break
                print ('line 56', row)
                csv_writer.writerow(row)


def calc_overal_score(rank_list):
    location_score = rank_list[0]
    color_score = rank_list[1]
    mascot_score = rank_list[2]
    # rank_list[0] islocation rank, [1] is color rank, [2] is mascot rank

# predetermined weights for ranks
    location_weight = 1
    color_weight = 2.25
    mascot_weight = 3
#
    school_score = float(location_score * location_weight) + \
        float(color_score * color_weight) + float(mascot_score * mascot_weight)
    return school_score


if __name__ == "__main__":
    main()
