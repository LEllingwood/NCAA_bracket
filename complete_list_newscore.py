"""Team_name , NCAARank, Conference, Location, Location_score, Team-colors, color_score, TeamMascot, Mascot_score"""

# 1 - best, 5 - worst

# purple
# Blue / grey
# orange /  gold
# red / yellow / cream / white

import csv
import itertools

my_counter = itertools.count(start=1)

with open('complete_list.csv', 'w') as complete_list:
    fieldnames = ['Unique Id', 'School', 'NCAA Rank', 'Conference', 'Location', 'Location Rank', 'Colors', 'Color Rank', 'Mascot', 'Mascot Rank']

    csv_writer = csv.DictWriter(complete_list, fieldnames=fieldnames)
    csv_writer.writeheader()

    csv_writer.writerow({'School': 'Gonzaga', 'NCAA Rank': '1', 'Conference': 'West', 'Location': 'Spokane, Washington', 'Location Rank': '4', 'Colors': 'Blue / Red', 'Color Rank': '4', 'Mascot': 'Bulldogs', 'Mascot Rank': '5', 'Unique Id': my_counter.next()})

    csv_writer.writerow({'School': 'Duke', 'NCAA Rank': '1', 'Conference': 'East', 'Location': 'Durham, North Carolina', 'Location Rank': '3', 'Colors': 'Blue / Dark Blue', 'Color Rank': '4', 'Mascot': 'Blue Devils', 'Mascot Rank': '2', 'Unique Id': my_counter.next()})

    csv_writer.writerow({'School': 'Virginia', 'NCAA Rank': '1', 'Conference': 'South', 'Location': 'Charlottesville, Virginia', 'Location Rank': '3', 'Colors': 'Blue / Orange', 'Color Rank': '4', 'Mascot': 'Cavaliers', 'Mascot Rank': '1', 'Unique Id': my_counter.next()})

    csv_writer.writerow({'School': 'Kentucky', 'NCAA Rank': '1', 'Conference': 'Midwest', 'Location': 'Lexington, Kentucky', 'Location Rank': '4', 'Colors': 'Blue / White', 'Color Rank': '3', 'Mascot': 'Wildcats', 'Mascot Rank': '5', 'Unique Id': my_counter.next()})

    csv_writer.writerow({'School': 'Tennessee', 'NCAA Rank': '2', 'Conference': 'South', 'Location': 'Knoxville, Tennessee', 'Location Rank': '2', 'Colors': 'Orange / White', 'Color Rank': '3', 'Mascot': 'Volunteers', 'Mascot Rank': '1', 'Unique Id': my_counter.next()})

    csv_writer.writerow({'School': 'North Carolina', 'NCAA Rank': '2', 'Conference': 'Midwest', 'Location': 'Chapel Hill, North Carolina', 'Location Rank': '4', 'Colors': 'Light Blue / White', 'Color Rank': '2', 'Mascot': 'Tar Heels', 'Mascot Rank': '1', 'Unique Id': my_counter.next()})

    csv_writer.writerow({'School': 'Michian State', 'NCAA Rank': '2', 'Conference': 'East', 'Location': 'East Lansing, Michigan', 'Location Rank': '1', 'Colors': 'Green / White', 'Color Rank': '1', 'Mascot': 'Spartans', 'Mascot Rank': '1', 'Unique Id': my_counter.next()})

    csv_writer.writerow({'School': 'Michigan', 'NCAA Rank': '2', 'Conference': 'West', 'Location': 'Ann Arbor, Michigan', 'Location Rank': '5', 'Colors': 'Blue / Yellow', 'Color Rank': '4', 'Mascot': 'Wolverines', 'Mascot Rank': '5', 'Unique Id': my_counter.next()})

    csv_writer.writerow({'School': 'Houston', 'NCAA Rank': '3', 'Conference': 'Midwest', 'Location': 'Houston, Texas', 'Location Rank': '4', 'Colors': 'Red / Dark Red', 'Color Rank': '2', 'Mascot': 'Cougars', 'Mascot Rank': '4', 'Unique Id': my_counter.next()})

    csv_writer.writerow({'School': 'Purdue', 'NCAA Rank': '3', 'Conference': 'South', 'Location': 'West Lafayette, Indiana', 'Location Rank': '1', 'Colors': 'Black / Gold', 'Color Rank': '3', 'Mascot': 'Boilermaker', 'Mascot Rank': '2', 'Unique Id': my_counter.next()})

    csv_writer.writerow({'School': 'Marquette', 'NCAA Rank': '3', 'Conference': 'East', 'Location': 'Milwaukee, Wisconsin', 'Location Rank': '1', 'Colors': 'Blue / Yellow', 'Color Rank': '4', 'Mascot': 'Golden Eagles', 'Mascot Rank': '3', 'Unique Id': my_counter.next()})

    csv_writer.writerow({'School': 'Kansas', 'NCAA Rank': '3', 'Conference': 'West', 'Location': 'Lawrence, Kansas', 'Location Rank': '1', 'Colors': 'Blue / Red', 'Color Rank': '4', 'Mascot': 'Jayhawks', 'Mascot Rank': '2', 'Unique Id': my_counter.next()})

    csv_writer.writerow({'School': 'LSU', 'NCAA Rank': '4', 'Conference': 'West', 'Location': 'Baton Rouge, Louisiana', 'Location Rank': '3', 'Colors': 'Purple / Gold', 'Color Rank': '5', 'Mascot': 'Tigers', 'Mascot Rank': '4', 'Unique Id': my_counter.next()})

    csv_writer.writerow({'School': 'Maryland', 'NCAA Rank': '4', 'Conference': 'Midwest', 'Location': 'College Park, Maryland', 'Location Rank': '2', 'Colors': 'Red / Gold', 'Color Rank': '2', 'Mascot':  'Terrapin', 'Mascot Rank': '1', 'Unique Id': my_counter.next()})

    csv_writer.writerow({'School': 'Texas Tech', 'NCAA Rank': '4', 'Conference': 'South', 'Location': 'Lubbock, Texas', 'Location Rank': '2', 'Colors': 'Red / Black', 'Color Rank': '3', 'Mascot': 'Red Raiders', 'Mascot Rank': '1', 'Unique Id':  my_counter.next()})

    csv_writer.writerow({'School': 'Nevada', 'NCAA Rank': '4', 'Conference': 'East', 'Location': 'Reno, Nevada', 'Location Rank': '3', 'Colors': 'Blue / Grey', 'Color Rank': '4', 'Mascot':  'Wolf Pack', 'Mascot Rank': '5', 'Unique Id': my_counter.next()})

    csv_writer.writerow({'School': 'Kansas State', 'NCAA Rank': '5', 'Conference': 'Midwest', 'Location': 'Manhattan, Kansas', 'Location Rank': '1', 'Colors': 'Purple / Grey', 'Color Rank': '5', 'Mascot':  'Wildcats', 'Mascot Rank': '5', 'Unique Id': my_counter.next()})

    csv_writer.writerow({'School': 'Iowa State', 'NCAA Rank': '5', 'Conference': 'East', 'Location': 'Ames, Iowa', 'Location Rank': '2', 'Colors': 'Red / Gold', 'Color Rank': '1', 'Mascot': 'Cyclones', 'Mascot Rank': '1', 'Unique Id': my_counter.next()})

    csv_writer.writerow({'School': 'Florida State', 'NCAA Rank': '5', 'Conference': 'West', 'Location': 'Tallahassee, Florida', 'Location Rank': '2', 'Colors': 'Red / Gold', 'Color Rank': '1', 'Mascot': 'Seminoles', 'Mascot Rank': '1', 'Unique Id': my_counter.next()})

    csv_writer.writerow({'School': 'Wisconsin', 'NCAA Rank': '5', 'Conference': 'South', 'Location': 'Madison, Wisconsin', 'Location Rank': '1', 'Colors': 'Red / Dark Red', 'Color Rank': '2', 'Mascot': 'Badgers', 'Mascot Rank': '4', 'Unique Id': my_counter.next()})

    csv_writer.writerow({'School': 'Virginia Tech', 'NCAA Rank': '6', 'Conference': 'East', 'Location': 'Blacksburg, Virginia', 'Location Rank': '3', 'Colors': 'Red / Orange', 'Color Rank': '3', 'Mascot': 'Hokies', 'Mascot Rank': '1', 'Unique Id': my_counter.next()})

    csv_writer.writerow({'School': 'Iowa', 'NCAA Rank': '6', 'Conference': 'Midwest', 'Location': 'Iowa City, Iowa', 'Location Rank': '3', 'Colors': 'Black / Gold', 'Color Rank': '3', 'Mascot': 'Hawkeyes', 'Mascot Rank': '4', 'Unique Id': my_counter.next()})

    csv_writer.writerow({'School': 'Cincinnati', 'NCAA Rank': '6', 'Conference': 'South', 'Location': 'Cincinnati, Ohio', 'Location Rank': '1', 'Colors': 'Red / Black', 'Color Rank': '3', 'Mascot': 'Bearcats', 'Mascot Rank': '3', 'Unique Id': my_counter.next()})

    csv_writer.writerow({'School': 'Buffalo', 'NCAA Rank': '6', 'Conference': 'West', 'Location': 'Buffalo, New York', 'Location Rank': '1', 'Colors': 'Blue / White', 'Color Rank': '2', 'Mascot': 'Bulls', 'Mascot Rank': '3', 'Unique Id': my_counter.next()})

    csv_writer.writerow({'School': 'Washington', 'NCAA Rank': '7', 'Conference': 'West', 'Location': 'Seattle, Washington', 'Location Rank': '5', 'Colors': 'Purple / Gold', 'Color Rank': '5', 'Mascot': 'Huskies', 'Mascot Rank': '5', 'Unique Id': my_counter.next()})

    csv_writer.writerow({'School': 'Baylor', 'NCAA Rank': '7', 'Conference': 'East', 'Location': 'Waco, Texas', 'Location Rank': '1', 'Colors': 'Green / Gold', 'Color Rank': '1', 'Mascot': 'Bears', 'Mascot Rank': '2', 'Unique Id': my_counter.next()})

    csv_writer.writerow({'School': 'Villanova', 'NCAA Rank': '7', 'Conference': 'Midwest', 'Location': 'Villanova, Pennsylvania', 'Location Rank': '2', 'Colors': 'Blue / Light Blue', 'Color Rank': '2', 'Mascot': 'Wildcats', 'Mascot Rank': '5', 'Unique Id':  my_counter.next()})

    csv_writer.writerow({'School': 'Syracuse', 'NCAA Rank': '7', 'Conference': 'South', 'Location': 'Syracuse, New York', 'Location Rank': '3', 'Colors': 'Orange / Grey', 'Color Rank': '5', 'Mascot': 'Orange', 'Mascot Rank': '1', 'Unique Id': my_counter.next()})

    csv_writer.writerow({'School': 'Mississippi State', 'NCAA Rank': '8', 'Conference': 'South', 'Location': 'Starkville, Mississippi', 'Location Rank': '1', 'Colors': 'Red / White', 'Color Rank': '1', 'Mascot': 'Bulldogs', 'Mascot Rank': '5', 'Unique Id': my_counter.next()})

    csv_writer.writerow({'School': 'Louisville', 'NCAA Rank': '8', 'Conference': 'Midwest', 'Location': 'Louisville, Kentucky', 'Location Rank': '3', 'Colors': 'Black / Red', 'Color Rank': '3', 'Mascot': 'Cardinals', 'Mascot Rank': '3', 'Unique Id': my_counter.next()})

    csv_writer.writerow({'School': "St. John's", 'NCAA Rank': '8', 'Conference': 'West', 'Location': 'New York City, New York', 'Location Rank': '5', 'Colors': 'Red / Blue', 'Color Rank': '4', 'Mascot': 'Red Storm', 'Mascot Rank': '1', 'Unique Id': my_counter.next()})

    csv_writer.writerow({'School': 'Ole Miss', 'NCAA Rank': '8', 'Conference': 'East', 'Location': 'Oxford, Mississippi', 'Location Rank': '1', 'Colors': 'Red / Blue', 'Color Rank': '4', 'Mascot': 'Rebels', 'Mascot Rank': '1', 'Unique Id': my_counter.next()})

    csv_writer.writerow({'School': 'Oklahoma', 'NCAA Rank': '9', 'Conference': 'Midwest', 'Location': 'Norman, Oklahoma', 'Location Rank': '1', 'Colors': 'Red / Cream', 'Color Rank': '2', 'Mascot': 'Sooners', 'Mascot Rank': '1', 'Unique Id': my_counter.next()})

    csv_writer.writerow({'School': 'NC State', 'NCAA Rank': '9', 'Conference': 'West', 'Location': 'Raleigh, North Carolina', 'Location Rank': '4', 'Colors': 'Red / Black', 'Color Rank': '3', 'Mascot': 'Wolfpack', 'Mascot Rank': '5', 'Unique Id': my_counter.next()})

    csv_writer.writerow({'School': 'VCU', 'NCAA Rank': '9', 'Conference': 'East', 'Location': 'Richmond, Virginia', 'Location Rank': '4', 'Colors': 'Black / Gold', 'Color Rank': '3', 'Mascot': 'Rams', 'Mascot Rank': '3', 'Unique Id': my_counter.next()})

    csv_writer.writerow({'School': 'Temple', 'NCAA Rank': '9', 'Conference': 'South', 'Location': 'Philadelphia, Pennsylvania', 'Location Rank': '2', 'Colors': 'Red / Yellow', 'Color Rank': '1', 'Mascot': 'Owls', 'Mascot Rank': '3', 'Unique Id': my_counter.next()})

    csv_writer.writerow({'School': 'UCF', 'NCAA Rank': '10', 'Conference': 'East', 'Location': 'Orlando, Florida', 'Location Rank': '3', 'Colors': 'Black / Gold', 'Color Rank': '3', 'Mascot': 'Knights', 'Mascot Rank': '1', 'Unique Id': my_counter.next()})

    csv_writer.writerow({'School': 'TCU', 'NCAA Rank': '10', 'Conference': 'Midwest', 'Location': 'Fort Worth, Texas', 'Location Rank': '3', 'Colors': 'Purple / White', 'Color Rank': '4', 'Mascot': 'Horned Frogs', 'Mascot Rank': '4', 'Unique Id': my_counter.next()})

    csv_writer.writerow({'School': 'Wofford', 'NCAA Rank': '10', 'Conference': 'West', 'Location': 'Spartanburg, South Carolina', 'Location Rank': '3', 'Colors': 'Black / Gold', 'Color Rank': '3', 'Mascot': 'Terriers', 'Mascot Rank': '2', 'Unique Id': my_counter.next()})

    csv_writer.writerow({'School': 'Texas', 'NCAA Rank': '10', 'Conference': 'South', 'Location': 'Austin, Texas', 'Location Rank': '5', 'Colors': 'Orange / Grey', 'Color Rank': '5', 'Mascot': 'Longhorns', 'Mascot Rank': '4', 'Unique Id': my_counter.next()})

    csv_writer.writerow({'School': 'Florida', 'NCAA Rank': '11', 'Conference': 'West', 'Location': 'Gainesville, Florida', 'Location Rank': '1', 'Colors': 'Blue / Orange', 'Color Rank': '5', 'Mascot': 'Gators', 'Mascot Rank': '4', 'Unique Id': my_counter.next()})

    csv_writer.writerow({'School': 'Arizona State', 'NCAA Rank': '11', 'Conference': 'Midwest', 'Location': 'Tempe, Arizona', 'Location Rank': '4', 'Colors': 'Red / Gold', 'Color Rank': '1', 'Mascot': 'Sun Devils', 'Mascot Rank': '2', 'Unique Id': my_counter.next()})

    csv_writer.writerow({'School': 'Seton Hall', 'NCAA Rank': '11', 'Conference': 'South', 'Location': 'Newark, New Jersey', 'Location Rank': '1', 'Colors': 'Blue / Grey', 'Color Rank': '5', 'Mascot': 'Pirates', 'Mascot Rank': '1', 'Unique Id': my_counter.next()})

    csv_writer.writerow({'School': 'Minnesota', 'NCAA Rank': '11', 'Conference': 'East', 'Location': 'Minneapolis, Minnesota', 'Location Rank': '1', 'Colors': 'Red / Yellow', 'Color Rank': '1', 'Mascot': 'Golden Gophers', 'Mascot Rank': '2', 'Unique Id': my_counter.next()})

    csv_writer.writerow({'School': 'Ohio State', 'NCAA Rank': '12', 'Conference': 'East', 'Location': 'Columbus, Ohio', 'Location Rank': '2', 'Colors': 'Red / Grey', 'Color Rank': '3', 'Mascot': 'Buckeyes', 'Mascot Rank': '2', 'Unique Id':  my_counter.next()})

    csv_writer.writerow({'School': 'Alabama', 'NCAA Rank': '12', 'Conference': 'East', 'Location': 'Tuscaloosa, Alabama', 'Location Rank': '1', 'Colors': 'Red / Grey', 'Color Rank': '3', 'Mascot': 'Crimson Tide', 'Mascot Rank': '1', 'Unique Id': my_counter.next()})

    csv_writer.writerow({'School': 'Auburn', 'NCAA Rank': '12', 'Conference': 'Midwest', 'Location': 'Auburn, Alabama', 'Location Rank': '1', 'Colors': 'Blue / Orange', 'Color Rank': '5', 'Mascot': 'Tigers', 'Mascot Rank': '5', 'Unique Id': my_counter.next()})

    csv_writer.writerow({'School': 'Clemson', 'NCAA Rank': '12', 'Conference': 'Midwest', 'Location': 'Clemson, South Carolina', 'Location Rank': '3', 'Colors': 'Orange / Purple', 'Color Rank': '5', 'Mascot': 'Tigers', 'Mascot Rank': '5', 'Unique Id': my_counter.next()})

    csv_writer.writerow({'School': 'Belmont', 'NCAA Rank': '12', 'Conference': 'West', 'Location': 'Nashville, Tennessee', 'Location Rank': '4', 'Colors': 'Blue / Red', 'Color Rank': '4', 'Mascot': 'Bruins', 'Mascot Rank': '1', 'Unique Id': my_counter.next()})

    csv_writer.writerow({'School': 'New Mexico State', 'NCAA Rank': '12', 'Conference': 'South', 'Location': 'Las Cruces, New Mexico', 'Location Rank': '4', 'Colors': 'Red / White', 'Color Rank': '1', 'Mascot': 'Aggies', 'Mascot Rank': '2', 'Unique Id': my_counter.next()})

    csv_writer.writerow({'School': 'Lipscomb', 'NCAA Rank': '13', 'Conference': 'West', 'Location': 'Nashville, Tennessee', 'Location Rank': '4', 'Colors': 'Purple / Gold', 'Color Rank': '5', 'Mascot': 'Bisons', 'Mascot Rank': '3', 'Unique Id':  my_counter.next()})

    csv_writer.writerow({'School': 'Hofstra', 'NCAA Rank': '13', 'Conference': 'Midwest', 'Location': 'Hempstead, New York', 'Location Rank': '3', 'Colors': 'Blue / Gold', 'Color Rank': '4', 'Mascot': 'Pride', 'Mascot Rank': '3', 'Unique Id': my_counter.next()})

    csv_writer.writerow({'School': 'Yale', 'NCAA Rank': '13', 'Conference': 'East', 'Location': 'New Haven, Connecticut', 'Location Rank': '3', 'Colors': 'Blue / White', 'Color Rank': '1', 'Mascot': 'Bulldogs', 'Mascot Rank': '5', 'Unique Id': my_counter.next()})

    csv_writer.writerow({'School': 'Old Dominion', 'NCAA Rank': '13', 'Conference': 'South', 'Location': 'Norfolk, Virginia', 'Location Rank': '3', 'Colors': 'Blue / Grey', 'Color Rank': '5', 'Mascot': 'Monarchs', 'Mascot Rank': '1', 'Unique Id': my_counter.next()})

    csv_writer.writerow({'School': 'Vermont', 'NCAA Rank': '14', 'Conference': 'East', 'Location': 'Burlington, Vermont', 'Location Rank': '3', 'Colors': 'Green / Gold', 'Color Rank': '1', 'Mascot': 'Catamounts', 'Mascot Rank': '1', 'Unique Id': my_counter.next()})

    csv_writer.writerow({'School': 'UC Irvine', 'NCAA Rank': '14', 'Conference': 'Midwest', 'Location': 'Irvine, California', 'Location Rank': '5', 'Colors': 'Blue / Gold', 'Color Rank': '4', 'Mascot': 'Anteaters', 'Mascot Rank': '5', 'Unique Id': my_counter.next()})

    csv_writer.writerow({'School': 'South Dakota State', 'NCAA Rank': '14', 'Conference': 'South', 'Location': 'Brookings, South Dakota', 'Location Rank': '2', 'Colors': 'Blue / Yellow', 'Color Rank': '4', 'Mascot': 'Jackrabbits', 'Mascot Rank': '4', 'Unique Id': my_counter.next()})

    csv_writer.writerow({'School': 'Montana', 'NCAA Rank': '14', 'Conference': 'West', 'Location': 'Missoula, Montana', 'Location Rank': '4', 'Colors': 'Red / Grey', 'Color Rank': '3', 'Mascot': 'Grizzles', 'Mascot Rank': '3', 'Unique Id': my_counter.next()})

    csv_writer.writerow({'School': 'Texas State', 'NCAA Rank': '15', 'Conference': 'West', 'Location': 'San Marcos, Texas', 'Location Rank': '2', 'Colors': 'Red / Gold', 'Color Rank': '1', 'Mascot': 'Bobcats', 'Mascot Rank': '5', 'Unique Id': my_counter.next()})

    csv_writer.writerow({'School': 'Wright State', 'NCAA Rank': '15', 'Conference': 'East', 'Location': 'Fairborn, Ohio', 'Location Rank': '2', 'Colors': 'Green / Gold', 'Color Rank': '1', 'Mascot': 'Raiders', 'Mascot Rank': '1', 'Unique Id': my_counter.next()})

    csv_writer.writerow({'School': 'Loyola-Chicago', 'NCAA Rank': '15', 'Conference': 'Midwest', 'Location': 'Chicago, Illinois', 'Location Rank': '2', 'Colors': 'Red / Gold', 'Color Rank': '1', 'Mascot': 'Ramblers', 'Mascot Rank': '1', 'Unique Id': my_counter.next()})

    csv_writer.writerow({'School': 'Radford', 'NCAA Rank': '15', 'Conference': 'South', 'Location': 'Radford, Virginia', 'Location Rank': '3', 'Colors': 'Red / White', 'Color Rank': '1', 'Mascot': 'Highlanders', 'Mascot Rank': '2', 'Unique Id': my_counter.next()})

    csv_writer.writerow({'School': 'Bucknell', 'NCAA Rank': '16', 'Conference': 'East', 'Location': 'Lewisburg, Pennsylvania', 'Location Rank': '2', 'Colors': 'Red / White', 'Color Rank': '1', 'Mascot': 'Bison', 'Mascot Rank': '3', 'Unique Id': my_counter.next()})

    csv_writer.writerow({'School': 'Sam Houston State', 'NCAA Rank': '16', 'Conference': 'West', 'Location': 'Huntsville, Texas', 'Location Rank': '3', 'Colors': 'Orange / White', 'Color Rank': '3', 'Mascot': 'Bearkats', 'Mascot Rank': '4', 'Unique Id': my_counter.next()})

    csv_writer.writerow({'School': 'Prairie View', 'NCAA Rank': '16', 'Conference': 'Midwest', 'Location': 'Prairie View, Texas', 'Location Rank': '1', 'Colors': 'Purple / Gold', 'Color Rank': '4', 'Mascot': 'Panthers', 'Mascot Rank': '5', 'Unique Id': my_counter.next()})

    csv_writer.writerow({'School': 'Norfolk State', 'NCAA Rank': '16', 'Conference': 'Midwest', 'Location': 'Norfolk, Virginia', 'Location Rank': '2', 'Colors': 'Green / Gold', 'Color Rank': '1', 'Mascot': 'Spartans', 'Mascot Rank': '1', 'Unique Id': my_counter.next()})

    csv_writer.writerow({'School': 'St. Francis PA', 'NCAA Rank': '16', 'Conference': 'South', 'Location': 'Loretta, Pennslyvania', 'Location Rank': '1', 'Colors': 'Red / White', 'Color Rank': '1', 'Mascot': 'Red Flash', 'Mascot Rank': '1', 'Unique Id': my_counter.next()})

    csv_writer.writerow({'School': 'Iona', 'NCAA Rank': '16', 'Conference': 'South', 'Location': 'New Rochelle, NY', 'Location Rank': '3', 'Colors': 'Red / Gold', 'Color Rank': '1', 'Mascot': 'Gaels', 'Mascot Rank': '2', 'Unique Id': my_counter.next()})


