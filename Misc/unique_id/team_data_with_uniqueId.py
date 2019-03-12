# read complete list
# read team @staticmethod

# write to new file (team data with id).  match the team name on complete list with the team name on team_data.  If the team names match, write the unique id in team_data to the complete_list_with_uniqueID file.  Otherwise, return a space saver of some sort that identifies which teams i need to look up.
import csv
import pprint

big_data = {}

with open('complete_list.csv') as f:
    csv_reader = csv.reader(f)
    for line in csv_reader:
        school_name = line[1]
        school_data = line[2:]
        big_data[school_name] = school_data
    pprint.pprint(big_data)

