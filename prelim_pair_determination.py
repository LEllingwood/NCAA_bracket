import csv


def main():
    # read prelim pairings csv file and append schools 1 and 2 to the empty list
    prelim_schools = []
    with open('preliminary_pairings.csv') as prelim:
        csv_reader1 = csv.DictReader(prelim)
        for row in csv_reader1:
            prelim_schools.append(row['School 1'])
            prelim_schools.append(row['School 2'])
    print(prelim_schools)

    # create empty dict into which we will read through each row of the complete list data and append the school name and three rank criteria
    prelim_dict = {}

    with open('complete_list.csv') as f:
        csv_reader = csv.DictReader(f)
        for row in csv_reader:
            if row['School'] in prelim_schools:
                prelim_dict[row['School']] = [int(row['Location Rank']),
                                              int(row['Color Rank']), int(row['Mascot Rank'])]
    print(prelim_dict)
    
    # for loop to run through the ranks and calculate the score
    for key in prelim_dict.keys():
        prelim_dict[key].append(calc_overal_score(prelim_dict[key]))
    print(prelim_dict)

# create a wildcard schools list into which the winner of each of four pairings will be appended.
    wildcard_schools=[]

    with open('preliminary_pairings.csv') as prelim:
        csv_reader = csv.DictReader(prelim)
        for row in csv_reader:
            wildcard_schools.append( row['School 1']  if prelim_dict[row['School 1']][-1] > prelim_dict[row['School 2']][-1] else row['School 2'])
    print (wildcard_schools)

    # with open('predicteed_pairings.csv') as rfile, wfile:
    #     csv_reader = csv.DictReader(rfile)
    #     csv_writer = csv.DictWriter(wfile)
    #     for row in reader:
    # To be continued  

    # with open(filename, 'r') as csvfile, tempfile:
    # reader = csv.DictReader(csvfile, fieldnames=fields)
    # writer = csv.DictWriter(tempfile, fieldnames=fields)
    # for row in reader:
    #     if row['ID'] == str(stud_ID):
    #         print('updating row', row['ID'])
    #         row['Name'], row['Course'], row['Year'] = stud_name, stud_course, stud_year
    #     row = {'ID': row['ID'], 'Name': row['Name'], 'Course': row['Course'], 'Year': row['Year']}
    #     writer.writerow(row)
    

# function used to calculate the winning score.  rank_list[0] is used to find the separate ranks because at thislevel, we're dealing with a list.
def calc_overal_score(rank_list):
    # rank_list[0] islocation rank, [1] is color rank, [2] is mascot rank
    location_score = rank_list[0]
    color_score = rank_list[1]
    mascot_score = rank_list[2]

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
