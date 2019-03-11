import argparse
import csv

def find_winner_schools(round):
    count = 1
    flag = False
    school1 = {}
    with open(round + "_round.csv", 'w') as outfile:
        with open(str(int(round)-1) + "_round.csv") as f:
            csv_reader = csv.DictReader(f)
            fieldnames = csv_reader.fieldnames
            csvwriter = csv.DictWriter(outfile, fieldnames=fieldnames)
            csvwriter.writeheader()
            for row in csv_reader:
                row['Unique Id'] = count
                count += 1
                if not flag:
                    flag = True
                    count -= 1
                if not school1 and flag:
                    school1 = row
                elif school1 and flag:
                    flag = False
                    if school1["Scores"] > row["Scores"]:
                        row = school1
                    school1 = {}
                if not flag:
                    csvwriter.writerow(row)
    return



def create_parser():
    """Create a cmd line parser object with 2 argument definitions"""
    parser = argparse.ArgumentParser()
    parser.add_argument("round", help="Enter the round number")
    return parser


def main():
    parser = create_parser()
    args = parser.parse_args()

    if not args:
        parser.print_usage()
        sys.exit(1) 
    find_winner_schools(args.round)

if __name__ == "__main__":
    main()
