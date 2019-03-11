"""Team_name , NCAARank, Conference, Location, Location_score, Team-colors, color_score, TeamMascot, Mascot_score"""

# 1 - best, 5 - worst

# purple
# Blue / grey
# orange /  gold
# red / yellow / cream / white
# TODO: Add color
import csv
import itertools


def create_complete_list_csv():
    my_counter = itertools.count(start=1)

    with open('complete_list.csv', 'w') as complete_list:
        fieldnames = ['Unique Id', 'School', 'NCAA Rank', 'Conference', 'Location',
                      'Location Rank', 'Colors', 'Color Rank', 'Mascot', 'Mascot Rank']

        csv_writer = csv.DictWriter(complete_list, fieldnames=fieldnames)
        csv_writer.writeheader()


###### West
        csv_writer.writerow({'School': 'Gonzaga', 'NCAA Rank': '1', 'Conference': 'West', 'Location': 'Spokane, Washington', 'Location Rank': '4',
                             'Colors': "#041E42, #C8102E", 'Color Rank': '4', 'Mascot': 'Bulldogs', 'Mascot Rank': '5', 'Unique Id': next(my_counter)})

        csv_writer.writerow({'School': 'Sam Houston State', 'NCAA Rank': '16', 'Conference': 'West', 'Location': 'Huntsville, Texas', 'Location Rank': '3',
                             'Colors': "#D88438', '#FFFFFF", 'Color Rank': '3', 'Mascot': 'Bearkats', 'Mascot Rank': '4', 'Unique Id': next(my_counter)})
        
        csv_writer.writerow({'School': "St. John's", 'NCAA Rank': '8', 'Conference': 'West', 'Location': 'New York City, New York', 'Location Rank': '5',
                             'Colors': "#BA0C2F, #FFFFFF", 'Color Rank': '5', 'Mascot': 'Red Storm', 'Mascot Rank': '1', 'Unique Id': next(my_counter)})

        csv_writer.writerow({'School': 'NC State', 'NCAA Rank': '9', 'Conference': 'West', 'Location': 'Raleigh, North Carolina', 'Location Rank': '4',
                             'Colors': "#cc0000, #000000", 'Color Rank': '3', 'Mascot': 'Wolfpack', 'Mascot Rank': '5', 'Unique Id': next(my_counter)})

        csv_writer.writerow({'School': 'Florida State', 'NCAA Rank': '5', 'Conference': 'West', 'Location': 'Tallahassee, Florida', 'Location Rank': '2',
                             'Colors': "#782F40, #CEB888", 'Color Rank': '1', 'Mascot': 'Seminoles', 'Mascot Rank': '1', 'Unique Id': next(my_counter)})

        csv_writer.writerow({'School': 'Belmont', 'NCAA Rank': '12', 'Conference': 'West', 'Location': 'Nashville, Tennessee', 'Location Rank': '4',
                             'Colors': "#15105b, #a01c21", 'Color Rank': '4', 'Mascot': 'Bruins', 'Mascot Rank': '1', 'Unique Id': next(my_counter)})

        csv_writer.writerow({'School': 'Louisiana State', 'NCAA Rank': '4', 'Conference': 'West', 'Location': 'Baton Rouge, Louisiana',
                             'Location Rank': '3', 'Colors': "#fdd023', '#461D7C", 'Color Rank': '5', 'Mascot': 'Tigers', 'Mascot Rank': '4', 'Unique Id': next(my_counter)})

        csv_writer.writerow({'School': 'Lipscomb', 'NCAA Rank': '13', 'Conference': 'West', 'Location': 'Nashville, Tennessee', 'Location Rank': '4',
                             'Colors': "#331e54, #F4AA00", 'Color Rank': '5', 'Mascot': 'Bisons', 'Mascot Rank': '3', 'Unique Id':  next(my_counter)})

        csv_writer.writerow({'School': 'Buffalo', 'NCAA Rank': '6', 'Conference': 'West', 'Location': 'Buffalo, New York', 'Location Rank': '1',
                             'Colors': "#005BBB, #FFFFFF", 'Color Rank': '2', 'Mascot': 'Bulls', 'Mascot Rank': '3', 'Unique Id': next(my_counter)})
 
        csv_writer.writerow({'School': 'Florida', 'NCAA Rank': '11', 'Conference': 'West', 'Location': 'Gainesville, Florida', 'Location Rank': '1',
                             'Colors': "#0021A5, #FA4616", 'Color Rank': '5', 'Mascot': 'Gators', 'Mascot Rank': '4', 'Unique Id': next(my_counter)})

        csv_writer.writerow({'School': 'Kansas', 'NCAA Rank': '3', 'Conference': 'West', 'Location': 'Lawrence, Kansas', 'Location Rank': '1',
                             'Colors': "#0051ba, #e8000d", 'Color Rank': '4', 'Mascot': 'Jayhawks', 'Mascot Rank': '2', 'Unique Id': next(my_counter)})

        csv_writer.writerow({'School': 'Montana', 'NCAA Rank': '14', 'Conference': 'West', 'Location': 'Missoula, Montana', 'Location Rank': '4',
                             'Colors': "#999999, #660033", 'Color Rank': '3', 'Mascot': 'Grizzles', 'Mascot Rank': '3', 'Unique Id': next(my_counter)})

        csv_writer.writerow({'School': 'Washington', 'NCAA Rank': '7', 'Conference': 'West', 'Location': 'Seattle, Washington', 'Location Rank': '5',
                             'Colors': "#4B2e83, #85754d", 'Color Rank': '5', 'Mascot': 'Huskies', 'Mascot Rank': '5', 'Unique Id': next(my_counter)})

        csv_writer.writerow({'School': 'Wofford', 'NCAA Rank': '10', 'Conference': 'West', 'Location': 'Spartanburg, South Carolina',
                             'Location Rank': '3', 'Colors': "#846F51, #000000", 'Color Rank': '3', 'Mascot': 'Terriers', 'Mascot Rank': '2', 'Unique Id': next(my_counter)})

        csv_writer.writerow({'School': 'Michigan', 'NCAA Rank': '2', 'Conference': 'West', 'Location': 'Ann Arbor, Michigan', 'Location Rank': '5',
                             'Colors': "#ffcb05, #00274c", 'Color Rank': '4', 'Mascot': 'Wolverines', 'Mascot Rank': '5', 'Unique Id': next(my_counter)})

        csv_writer.writerow({'School': 'Texas State', 'NCAA Rank': '15', 'Conference': 'West', 'Location': 'San Marcos, Texas', 'Location Rank': '2',
                             'Colors': "#8d734a, #501214", 'Color Rank': '1', 'Mascot': 'Bobcats', 'Mascot Rank': '5', 'Unique Id': next(my_counter)})



########    Midwest
        csv_writer.writerow({'School': 'Kentucky', 'NCAA Rank': '1', 'Conference': 'Midwest', 'Location': 'Lexington, Kentucky', 'Location Rank': '4',
                             'Colors': "#0033a0, #FFFFFF", 'Color Rank': '3', 'Mascot': 'Wildcats', 'Mascot Rank': '5', 'Unique Id': next(my_counter)})

        csv_writer.writerow({'School': 'Prairie View', 'NCAA Rank': '16', 'Conference': 'Midwest', 'Location': 'Prairie View, Texas', 'Location Rank': '1',
                             'Colors': "#2D0962, #F8CD46", 'Color Rank': '4', 'Mascot': 'Panthers', 'Mascot Rank': '5', 'Unique Id': next(my_counter)})

        csv_writer.writerow({'School': 'Norfolk State', 'NCAA Rank': '16', 'Conference': 'Midwest', 'Location': 'Norfolk, Virginia', 'Location Rank': '2',
                             'Colors': "#347856, #EED05B", 'Color Rank': '1', 'Mascot': 'Spartans', 'Mascot Rank': '1', 'Unique Id': next(my_counter)})

        csv_writer.writerow({'School': 'Louisville', 'NCAA Rank': '8', 'Conference': 'Midwest', 'Location': 'Louisville, Kentucky', 'Location Rank': '3',
                             'Colors': "#9F1F14, #000000", 'Color Rank': '3', 'Mascot': 'Cardinals', 'Mascot Rank': '3', 'Unique Id': next(my_counter)})

        csv_writer.writerow({'School': 'Oklahoma', 'NCAA Rank': '9', 'Conference': 'Midwest', 'Location': 'Norman, Oklahoma', 'Location Rank': '1',
                             'Colors': "#841617, #fdf9d8", 'Color Rank': '2', 'Mascot': 'Sooners', 'Mascot Rank': '1', 'Unique Id': next(my_counter)})

        csv_writer.writerow({'School': 'Kansas State', 'NCAA Rank': '5', 'Conference': 'Midwest', 'Location': 'Manhattan, Kansas', 'Location Rank': '1',
                             'Colors': "#a7a7a7, #512888", 'Color Rank': '5', 'Mascot':  'Wildcats', 'Mascot Rank': '5', 'Unique Id': next(my_counter)})

        csv_writer.writerow({'School': 'Auburn', 'NCAA Rank': '12', 'Conference': 'Midwest', 'Location': 'Auburn, Alabama', 'Location Rank': '1',
                             'Colors': "#E87722, #0C2340", 'Color Rank': '5', 'Mascot': 'Tigers', 'Mascot Rank': '5', 'Unique Id': next(my_counter)})

        csv_writer.writerow({'School': 'Clemson', 'NCAA Rank': '12', 'Conference': 'Midwest', 'Location': 'Clemson, South Carolina', 'Location Rank': '3',
                             'Colors': "#F56600, #522D80", 'Color Rank': '5', 'Mascot': 'Tigers', 'Mascot Rank': '5', 'Unique Id': next(my_counter)})

        csv_writer.writerow({'School': 'Maryland', 'NCAA Rank': '4', 'Conference': 'Midwest', 'Location': 'College Park, Maryland', 'Location Rank': '2',
                             'Colors': "#E03a3e, #ffd520", 'Color Rank': '2', 'Mascot':  'Terrapin', 'Mascot Rank': '1', 'Unique Id': next(my_counter)})

        csv_writer.writerow({'School': 'Hofstra', 'NCAA Rank': '13', 'Conference': 'Midwest', 'Location': 'Hempstead, New York', 'Location Rank': '3',
                             'Colors': "#0D368C, #F6C952", 'Color Rank': '4', 'Mascot': 'Pride', 'Mascot Rank': '3', 'Unique Id': next(my_counter)})
 
        csv_writer.writerow({'School': 'Iowa', 'NCAA Rank': '6', 'Conference': 'Midwest', 'Location': 'Iowa City, Iowa', 'Location Rank': '3',
                             'Colors': "#FFCD00, #00000", 'Color Rank': '3', 'Mascot': 'Hawkeyes', 'Mascot Rank': '4', 'Unique Id': next(my_counter)})

        csv_writer.writerow({'School': 'Arizona State', 'NCAA Rank': '11', 'Conference': 'Midwest', 'Location': 'Tempe, Arizona', 'Location Rank': '4',
                             'Colors': "#8c1d40, #FFC627", 'Color Rank': '1', 'Mascot': 'Sun Devils', 'Mascot Rank': '2', 'Unique Id': next(my_counter)})

        csv_writer.writerow({'School': 'Houston', 'NCAA Rank': '3', 'Conference': 'Midwest', 'Location': 'Houston, Texas', 'Location Rank': '4',
                             'Colors': "#C8102E, #76232F", 'Color Rank': '2', 'Mascot': 'Cougars', 'Mascot Rank': '4', 'Unique Id': next(my_counter)})

        csv_writer.writerow({'School': 'UC Irvine', 'NCAA Rank': '14', 'Conference': 'Midwest', 'Location': 'Irvine, California', 'Location Rank': '5',
                             'Colors': "#0C2340, #FFC72C", 'Color Rank': '4', 'Mascot': 'Anteaters', 'Mascot Rank': '5', 'Unique Id': next(my_counter)})

        csv_writer.writerow({'School': 'Villanova', 'NCAA Rank': '7', 'Conference': 'Midwest', 'Location': 'Villanova, Pennsylvania', 'Location Rank': '2',
                             'Colors': "#13b5ea, #00205b", 'Color Rank': '2', 'Mascot': 'Wildcats', 'Mascot Rank': '5', 'Unique Id':  next(my_counter)})
   
        csv_writer.writerow({'School': 'TCU', 'NCAA Rank': '10', 'Conference': 'Midwest', 'Location': 'Fort Worth, Texas', 'Location Rank': '3',
                             'Colors': "#4D1979, #A3A9AC", 'Color Rank': '5', 'Mascot': 'Horned Frogs', 'Mascot Rank': '4', 'Unique Id': next(my_counter)})

        csv_writer.writerow({'School': 'North Carolina', 'NCAA Rank': '2', 'Conference': 'Midwest', 'Location': 'Chapel Hill, North Carolina',
                             'Location Rank': '4', 'Colors': "#7BAFD4, #FFFFFF", 'Color Rank': '2', 'Mascot': 'Tar Heels', 'Mascot Rank': '1', 'Unique Id': next(my_counter)})

        csv_writer.writerow({'School': 'Loyola-Chicago', 'NCAA Rank': '15', 'Conference': 'Midwest', 'Location': 'Chicago, Illinois',
                             'Location Rank': '2', 'Colors': "#530e11, #e5a92a", 'Color Rank': '1', 'Mascot': 'Ramblers', 'Mascot Rank': '1', 'Unique Id': next(my_counter)})


##########   East

        csv_writer.writerow({'School': 'Duke', 'NCAA Rank': '1', 'Conference': 'East', 'Location': 'Durham, North Carolina', 'Location Rank': '3',
                             'Colors': "#235f9c, #003366", 'Color Rank': '4', 'Mascot': 'Blue Devils', 'Mascot Rank': '2', 'Unique Id': next(my_counter)})

        csv_writer.writerow({'School': 'Bucknell', 'NCAA Rank': '16', 'Conference': 'East', 'Location': 'Lewisburg, Pennsylvania',
                             'Location Rank': '2', 'Colors': "#123862, #DF642C", 'Color Rank': '1', 'Mascot': 'Bison', 'Mascot Rank': '3', 'Unique Id': next(my_counter)})

        csv_writer.writerow({'School': 'Ole Miss', 'NCAA Rank': '8', 'Conference': 'East', 'Location': 'Oxford, Mississippi', 'Location Rank': '1',
                             'Colors': "#CE1126, #006BA6", 'Color Rank': '4', 'Mascot': 'Rebels', 'Mascot Rank': '1', 'Unique Id': next(my_counter)})

        csv_writer.writerow({'School': 'VCU', 'NCAA Rank': '9', 'Conference': 'East', 'Location': 'Richmond, Virginia', 'Location Rank': '4',
                             'Colors': "#000000, #ffb300", 'Color Rank': '3', 'Mascot': 'Rams', 'Mascot Rank': '3', 'Unique Id': next(my_counter)})

        csv_writer.writerow({'School': 'Iowa State', 'NCAA Rank': '5', 'Conference': 'East', 'Location': 'Ames, Iowa', 'Location Rank': '2',
                             'Colors': "#c8102e, #f1be48", 'Color Rank': '1', 'Mascot': 'Cyclones', 'Mascot Rank': '1', 'Unique Id': next(my_counter)})

        csv_writer.writerow({'School': 'Ohio State', 'NCAA Rank': '12', 'Conference': 'East', 'Location': 'Columbus, Ohio', 'Location Rank': '2',
                             'Colors': "#666666, #bb0000", 'Color Rank': '3', 'Mascot': 'Buckeyes', 'Mascot Rank': '2', 'Unique Id':  next(my_counter)})

        csv_writer.writerow({'School': 'Alabama', 'NCAA Rank': '12', 'Conference': 'East', 'Location': 'Tuscaloosa, Alabama', 'Location Rank': '1',
                             'Colors': "#828a8f, #9e1b32", 'Color Rank': '3', 'Mascot': 'Crimson Tide', 'Mascot Rank': '1', 'Unique Id': next(my_counter)})

        csv_writer.writerow({'School': 'Nevada', 'NCAA Rank': '4', 'Conference': 'East', 'Location': 'Reno, Nevada', 'Location Rank': '3',
                             'Colors': "#003366, #807f84", 'Color Rank': '4', 'Mascot':  'Wolf Pack', 'Mascot Rank': '5', 'Unique Id': next(my_counter)})

        csv_writer.writerow({'School': 'Yale', 'NCAA Rank': '13', 'Conference': 'East', 'Location': 'New Haven, Connecticut', 'Location Rank': '3',
                             'Colors': "#00356b, #FFFFFF", 'Color Rank': '1', 'Mascot': 'Bulldogs', 'Mascot Rank': '5', 'Unique Id': next(my_counter)})

        csv_writer.writerow({'School': 'Virginia Tech', 'NCAA Rank': '6', 'Conference': 'East', 'Location': 'Blacksburg, Virginia',
                             'Location Rank': '3', 'Colors': "#cf4420, #63003", 'Color Rank': '3', 'Mascot': 'Hokies', 'Mascot Rank': '1', 'Unique Id': next(my_counter)})

        csv_writer.writerow({'School': 'Minnesota', 'NCAA Rank': '11', 'Conference': 'East', 'Location': 'Minneapolis, Minnesota', 'Location Rank': '1',
                             'Colors': "#FFCC33, #7A0019", 'Color Rank': '1', 'Mascot': 'Golden Gophers', 'Mascot Rank': '2', 'Unique Id': next(my_counter)})

        csv_writer.writerow({'School': 'Marquette', 'NCAA Rank': '3', 'Conference': 'East', 'Location': 'Milwaukee, Wisconsin', 'Location Rank': '1',
                             'Colors': "#003366, #ffcc00", 'Color Rank': '4', 'Mascot': 'Golden Eagles', 'Mascot Rank': '3', 'Unique Id': next(my_counter)})

        csv_writer.writerow({'School': 'Vermont', 'NCAA Rank': '14', 'Conference': 'East', 'Location': 'Burlington, Vermont', 'Location Rank': '3',
                             'Colors': "#2F6F57, #F9D44C", 'Color Rank': '1', 'Mascot': 'Catamounts', 'Mascot Rank': '1', 'Unique Id': next(my_counter)})
        
        csv_writer.writerow({'School': 'Baylor', 'NCAA Rank': '7', 'Conference': 'East', 'Location': 'Waco, Texas', 'Location Rank': '1',
                             'Colors': "#003015, #Fecb00", 'Color Rank': '1', 'Mascot': 'Bears', 'Mascot Rank': '2', 'Unique Id': next(my_counter)})

        csv_writer.writerow({'School': 'UCF', 'NCAA Rank': '10', 'Conference': 'East', 'Location': 'Orlando, Florida', 'Location Rank': '3',
                             'Colors': "#ceb888, #000000", 'Color Rank': '3', 'Mascot': 'Knights', 'Mascot Rank': '1', 'Unique Id': next(my_counter)})

        csv_writer.writerow({'School': 'Michian State', 'NCAA Rank': '2', 'Conference': 'East', 'Location': 'East Lansing, Michigan', 'Location Rank': '1',
                             'Colors': "#FFFFFF, #18453b", 'Color Rank': '1', 'Mascot': 'Spartans', 'Mascot Rank': '1', 'Unique Id': next(my_counter)})

        csv_writer.writerow({'School': 'Wright State', 'NCAA Rank': '15', 'Conference': 'East', 'Location': 'Fairborn, Ohio', 'Location Rank': '2',
                             'Colors': "#FFE1A5, #CEA052", 'Color Rank': '1', 'Mascot': 'Raiders', 'Mascot Rank': '1', 'Unique Id': next(my_counter)})

#########   South

        csv_writer.writerow({'School': 'Virginia', 'NCAA Rank': '1', 'Conference': 'South', 'Location': 'Charlottesville, Virginia', 'Location Rank': '3',
                             'Colors': "#232d4b, #F84C1E", 'Color Rank': '4', 'Mascot': 'Cavaliers', 'Mascot Rank': '1', 'Unique Id': next(my_counter)})

        csv_writer.writerow({'School': 'St. Francis PA', 'NCAA Rank': '16', 'Conference': 'South', 'Location': 'Loretta, Pennslyvania',
                             'Location Rank': '1', 'Colors': "#001DF5, #EB3323", 'Color Rank': '1', 'Mascot': 'Red Flash', 'Mascot Rank': '1', 'Unique Id': next(my_counter)})

        csv_writer.writerow({'School': 'Iona', 'NCAA Rank': '16', 'Conference': 'South', 'Location': 'New Rochelle, NY', 'Location Rank': '3',
                             'Colors': "#851929, #F4BB44", 'Color Rank': '1', 'Mascot': 'Gaels', 'Mascot Rank': '2', 'Unique Id': next(my_counter)})

        csv_writer.writerow({'School': 'Tennessee', 'NCAA Rank': '2', 'Conference': 'South', 'Location': 'Knoxville, Tennessee', 'Location Rank': '2',
                             'Colors': "#ff8324, #ffffff", 'Color Rank': '3', 'Mascot': 'Volunteers', 'Mascot Rank': '1', 'Unique Id': next(my_counter)})
        
        csv_writer.writerow({'School': 'Radford', 'NCAA Rank': '15', 'Conference': 'South', 'Location': 'Radford, Virginia', 'Location Rank': '3',
                             'Colors': "#B22426, #FFFFFF", 'Color Rank': '1', 'Mascot': 'Highlanders', 'Mascot Rank': '2', 'Unique Id': next(my_counter)})

        csv_writer.writerow({'School': 'Purdue', 'NCAA Rank': '3', 'Conference': 'South', 'Location': 'West Lafayette, Indiana', 'Location Rank': '1',
                             'Colors': "#ceb888, #000000", 'Color Rank': '3', 'Mascot': 'Boilermaker', 'Mascot Rank': '2', 'Unique Id': next(my_counter)})

        csv_writer.writerow({'School': 'South Dakota State', 'NCAA Rank': '14', 'Conference': 'South', 'Location': 'Brookings, South Dakota',
                             'Location Rank': '2', 'Colors': "#FFD100, #0033A0", 'Color Rank': '4', 'Mascot': 'Jackrabbits', 'Mascot Rank': '4', 'Unique Id': next(my_counter)})

        csv_writer.writerow({'School': 'Texas Tech', 'NCAA Rank': '4', 'Conference': 'South', 'Location': 'Lubbock, Texas', 'Location Rank': '2',
                             'Colors': "#cc0000, #000000", 'Color Rank': '3', 'Mascot': 'Red Raiders', 'Mascot Rank': '1', 'Unique Id':  next(my_counter)})

        csv_writer.writerow({'School': 'Old Dominion', 'NCAA Rank': '13', 'Conference': 'South', 'Location': 'Norfolk, Virginia', 'Location Rank': '3',
                             'Colors': "#92C1E9, #003057", 'Color Rank': '5', 'Mascot': 'Monarchs', 'Mascot Rank': '1', 'Unique Id': next(my_counter)})

        csv_writer.writerow({'School': 'Wisconsin', 'NCAA Rank': '5', 'Conference': 'South', 'Location': 'Madison, Wisconsin', 'Location Rank': '1',
                             'Colors': "#c5050c, #9b0000", 'Color Rank': '2', 'Mascot': 'Badgers', 'Mascot Rank': '4', 'Unique Id': next(my_counter)})

        csv_writer.writerow({'School': 'New Mexico State', 'NCAA Rank': '12', 'Conference': 'South', 'Location': 'Las Cruces, New Mexico',
                             'Location Rank': '4', 'Colors': "#000000, #861F41", 'Color Rank': '1', 'Mascot': 'Aggies', 'Mascot Rank': '2', 'Unique Id': next(my_counter)})

        csv_writer.writerow({'School': 'Cincinnati', 'NCAA Rank': '6', 'Conference': 'South', 'Location': 'Cincinnati, Ohio', 'Location Rank': '1',
                             'Colors': "#E00122, #000000", 'Color Rank': '3', 'Mascot': 'Bearcats', 'Mascot Rank': '3', 'Unique Id': next(my_counter)})
   
        csv_writer.writerow({'School': 'Seton Hall', 'NCAA Rank': '11', 'Conference': 'South', 'Location': 'Newark, New Jersey', 'Location Rank': '1',
                             'Colors': "#A2AAAD, #004488", 'Color Rank': '5', 'Mascot': 'Pirates', 'Mascot Rank': '1', 'Unique Id': next(my_counter)})

        csv_writer.writerow({'School': 'Syracuse', 'NCAA Rank': '7', 'Conference': 'South', 'Location': 'Syracuse, New York', 'Location Rank': '3',
                             'Colors': "#3e3d3c, #d44500", 'Color Rank': '5', 'Mascot': 'Orange', 'Mascot Rank': '1', 'Unique Id': next(my_counter)})

        csv_writer.writerow({'School': 'Texas', 'NCAA Rank': '10', 'Conference': 'South', 'Location': 'Austin, Texas', 'Location Rank': '5',
                             'Colors': "#bf5700, #333f48", 'Color Rank': '5', 'Mascot': 'Longhorns', 'Mascot Rank': '4', 'Unique Id': next(my_counter)})

        csv_writer.writerow({'School': 'Mississippi State', 'NCAA Rank': '8', 'Conference': 'South', 'Location': 'Starkville, Mississippi',
                             'Location Rank': '1', 'Colors': "#ffffff, #660000", 'Color Rank': '1', 'Mascot': 'Bulldogs', 'Mascot Rank': '5', 'Unique Id': next(my_counter)})

        csv_writer.writerow({'School': 'Temple', 'NCAA Rank': '9', 'Conference': 'South', 'Location': 'Philadelphia, Pennsylvania',
                             'Location Rank': '2', 'Colors': "#9D2235, #FFCD00", 'Color Rank': '1', 'Mascot': 'Owls', 'Mascot Rank': '3', 'Unique Id': next(my_counter)})



def create_preliminary_picks_csv():
    with open('preliminary_pairings.csv', 'w') as pairings_file:
        fieldnames = {'School 1', 'School 2'}

        csv_writer = csv.DictWriter(pairings_file, fieldnames=fieldnames)
        csv_writer.writeheader()

        csv_writer.writerow({'School 1': 'Prairie View',
                            'School 2': 'Norfolk State'})
        csv_writer.writerow({'School 1': 'St. Francis PA', 'School 2': 'Iona'})
        csv_writer.writerow({'School 1': 'Auburn', 'School 2': 'Clemson'})
        csv_writer.writerow({'School 1': 'Ohio State', 'School 2': 'Alabama'})


if __name__ == "__main__":
    create_complete_list_csv()
    create_preliminary_picks_csv()
