import csv
from collections import OrderedDict


def find_final_64(schools_info_file, prelim_schools):
    count = 1
    flag = False
    school1 = {}
    with open("1_round.csv", 'w') as outfile:
        with open(schools_info_file) as f:
            csv_reader = csv.DictReader(f)
            fieldnames = csv_reader.fieldnames
            fieldnames.append("Scores")

            csvwriter = csv.DictWriter(outfile, fieldnames=fieldnames)
            csvwriter.writeheader()
            for row in csv_reader:
                rank_list = [int(row['Location Rank']),
                             int(row['Color Rank']), int(row['Mascot Rank'])]
                score = calc_overal_score_per_school(rank_list)
                row["Scores"] = score
                row['Unique Id'] = count
                count += 1
                if row['School'] in prelim_schools and not flag:
                    flag = True
                    count -= 1
                if not school1 and flag:
                    school1 = row
                elif school1 and flag:
                    flag = False
                    print(school1["School"], school1["Scores"], row["School"], row["Scores"])
                    if school1["Scores"] > row["Scores"]:
                        row = school1
                    school1 = {}
                if not flag:
                    csvwriter.writerow(row)
    return



def calc_overal_score_per_school(rank_list):
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


def get_prelim_schools(prelim_file):
    prelim_schools = []
    with open(prelim_file) as prelim:
        csv_reader1 = csv.DictReader(prelim)
        for row in csv_reader1:
            prelim_schools.append(row['School 1'])
            prelim_schools.append(row['School 2'])
    return prelim_schools


def main():
    prelim_schools = get_prelim_schools('preliminary_pairings.csv')
    find_final_64('complete_list.csv', prelim_schools)


if __name__ == "__main__":
    main()
