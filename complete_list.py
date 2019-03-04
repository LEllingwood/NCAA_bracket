"""Team_name , NCAARank, Conference, Location, Location_score, Team-colors, color_score, TeamMascot, Mascot_score, predicted_pairing"""

# 1 - best, 5 - worst

# purple
# Blue / grey
# orange /  gold
# red / yellow / cream / white

import csv

with open('team_locations.csv', 'w', newline='') as f:
    thewriter = csv.writer(f)

    thewriter.writerow(['team_name', 'NCAA_rank', 'conference', 'location', 'location_score', 'team_colors', 'color_score', 'mascot', 'mascot_score', 'predicted_pairing'])

    thewriter.writerow(['Gonzaga', '1', 'West', 'Spokane, Washington', '2', 'Blue, Red', '2',  'Bulldogs', '1', 'Sam Houston St.'])

    thewriter.writerow(['Duke', '1', 'East', 'Durham, North Carolina', '3', 'Blue, Dark Blue', '2', 'Blue Devils', '4', 'Bucknell'])

    thewriter.writerow(['Virginia', '1', 'South', 'Charlottesville, Virginia', '3', 'Blue, Orange', '2', 'Cavaliers', '5', 'St. Francis/Iona'])

    thewriter.writerow(['Kentucky', '1', 'Midwest', 'Lexington, Kentucky', '2', 'Blue, White', '3', 'Wildcats', '1', 'Prairie View/Norfolk St.'])

    thewriter.writerow(['Tennessee', '2', 'South', 'Knoxville, Tennessee', '4', 'Orange, White', '3', 'Volunteers', '5', 'Radford'])

    thewriter.writerow(['North Carolina', '2', 'Midwest', 'Chapel Hill, North Carolina', '2', 'Light Blue, White', '4', 'Tar Heels', '5', 'Loyola-Chicago'])

    thewriter.writerow(['Michian State', '2', 'East', 'East Lansing, Michigan', '5', 'Green, White', '5', 'Spartans', '5', 'Wright St.'])

    thewriter.writerow(['Michigan', '2', 'West', 'Ann Arbor, Michigan', '1', 'Yellow, Blue', '2', 'Wolverines', '1', 'Texas St.'])

    thewriter.writerow(['Houston', '3', 'Midwest', 'Houston, Texas', '2', 'Red, Dark Red', '4', 'Cougars', '2', 'UC Irvine'])

    thewriter.writerow(['Purdue', '3', 'South', 'West Lafayette, Indiana', '5', 'Black, Gold', '3', 'Boilermaker', '4', 'S. Dakota St.'])

    thewriter.writerow(['Marquette', '3', 'Easts', 'Milwaukee, Wisconsin', '5', 'Blue, Yellow', '2', 'Golden Eagles', '3', 'Vermont'])

    thewriter.writerow(['Kansas', '3', 'West', 'Lawrence, Kansas', '5', 'Blue, Red', '2', 'Jayhawks', '4', 'Montana'])

    thewriter.writerow(['LSU', '4', ' West', 'Baton Rouge, Louisiana', '3', 'Purple, Gold', '1', 'Tigers', '2', 'Lipscomb'])

    thewriter.writerow(['Maryland', '4', 'Midwest', 'College Park, Maryland', '4', 'Red, Gold', '4', 'Terrapin', '5', 'Hofstra'])

    thewriter.writerow(['Texas Tech', '4', 'South', 'Lubbock, Texas', '4', 'Red, Black', '3', 'Red Raiders', '5', 'Old Dominion'])

    thewriter.writerow(['Nevada', '4', 'East', 'Reno, Nevada', '3', 'Blue, Grey', '2', 'Wolf Pack', '1', ' Yale'])

    thewriter.writerow(['Kansas State', '5', 'Midwest', 'Manhattan, Kansas', '5', 'Purple, Grey', '1', 'Wildcats', '1', 'Auburn/Clemson'])

    thewriter.writerow(['Iowa State', '5', 'East', 'Ames, Iowa', '4', 'Red, Gold', '5', 'Cyclones', '5', 'Ohio St./Alabama'])

    thewriter.writerow(['Florida State', '5', 'West', 'Tallahassee, Florida', '4', 'Red, Gold', '5', 'Seminoles', '5', 'Belmont'])

    thewriter.writerow(['Wisconsin', '5', 'South', 'Madison, Wisconsin', '5', 'Red, Dark Red', '4', 'Badgers', '2', 'New Mexico St.'])

    thewriter.writerow(['Virginia Tech', '6', 'East', 'Blacksburg, Virginia', '3','Red Orange', '3', 'Hokies', '5', 'Minnesota'])

    thewriter.writerow(['Iowa', '6', 'Midwest', 'Iowa City, Iowa', '3', 'Black, Gold', '3', 'Hawkeyes', '2', 'Arizona St.'])

    thewriter.writerow(['Cincinnati', '6', 'South', 'Cincinnati, Ohio', '5', 'Red, Black', '3', 'Bearcats', '3', 'Seton Hall'])

    thewriter.writerow(['Buffalo', '6', 'West', 'Buffalo, New York', '5', 'Blue, White', '4', 'Bulls', '3', 'Florida'])

    thewriter.writerow(['Washington', '7', 'West', 'Seattle, Washington', '1', 'Purple, Gold', '1', 'Huskies', '1', 'Wofford'])

    thewriter.writerow(['Baylor', '7', 'East', 'Waco, Texas', '5', 'Green, Gold', '5', 'Bears', '4', 'UCF'])

    thewriter.writerow(['Villanova', '7', 'Midwest', 'Villanova, Pennsylvania', '4', 'Blue, Light Blue', '4', 'Wildcats', '1', 'TCU'])

    thewriter.writerow(['Syracuse', '7', 'South', 'Syracuse, New York', '3', 'Orange, Grey', '1', 'Orange', '5', 'Texas'])

    thewriter.writerow(['Mississippi State', '8', 'South', 'Starkville, Mississippi', '5', 'Red, White', '5', 'Bulldogs', '1', 'Temple'])

    thewriter.writerow(['Louisville', '8', 'Midwest', 'Louisville, Kentucky', '3', 'Black, Red', '3', 'Cardinals', '3', 'Oklahoma'])

    thewriter.writerow(["St. John's", '8', 'West', 'New York City, New York', '1', 'Red, Blue', '2', 'Red Storm', '5', 'NC St.'])

    thewriter.writerow(['Ole Miss', '8', 'East', 'Oxford, Mississippi', '5', 'Red, Blue', '2', 'Rebels', '5', 'VCU'])

    thewriter.writerow(['Oklahoma', '9', 'Midwest', 'Norman, Oklahoma', '5', 'Red, Cream', '4', 'Sooners', '5', 'Louisville'])

    thewriter.writerow(['NC State', '9', 'West', 'Raleigh, North Carolina'], '2', 'Red, Black', '3', 'Wolfpack', '1', "St. John's")

    thewriter.writerow(['VCU', '9', 'East', 'Richmond, Virginia', '2', 'Black, Gold', '3', 'Rams', '3', 'Ole Miss'])

    thewriter.writerow(['Temple', '9', 'South', 'Philadelphia, Pennsylvania', '4', 'Red, Yellow', '5', 'Owls', '3', 'Mississippi St.'])

    thewriter.writerow(['UCF', '10', 'East', 'Orlando, Florida', '3', 'Black, Gold', '3', 'Knights', '5', 'Baylor'])

    thewriter.writerow(['TCU', '10', 'Midwest' 'Fort Worth, Texas', '3', 'Purple, White', '2', 'Horned Frogs', '2', 'Villanova'])

    thewriter.writerow(['Wofford', '10', 'West', 'Spartanburg, South Carolina', '3', 'Black, Gold', '3', 'Terriers', '4', 'Washington'])

    thewriter.writerow(['Texas', '10', 'South', 'Austin, Texas', '1', 'Orange, Grey', '1', 'Longhorns', '2', 'Syracuse'])

    thewriter.writerow(['Florida', '11', 'West', 'Gainesville, Florida', '5', 'Blue, Orange', '1', 'Gators', '2', 'Buffalo'])

    thewriter.writerow(['Arizona State', '11', 'Midwest','Tempe, Arizona', '2', 'Red, Gold', '5', 'Sun Devils', '4', 'Iowa'])

    thewriter.writerow(['Seton Hall', '11', 'South', 'Newark, New Jersey', '5', 'Blue, Grey', '1', 'Pirates', '5', 'Cincinnati'])

    thewriter.writerow(['Minnesota', '11', 'East', 'Minneapolis, Minnesota', '5', 'Red, Yellow', '5', 'Golden Gophers', '2', 'Virginia Tech'])

    thewriter.writerow(['Ohio State', '12', 'East', 'Columbus, Ohio', '4', 'Red, Grey', '3', 'Buckeyes', '4', 'Iowa St.'])

    thewriter.writerow(['Alabama', '12', 'East', 'Tuscaloosa, Alabama', '5', 'Red, Grey', '3', 'Crimson Tide', '5', 'Iowa St.'])

    thewriter.writerow(['Auburn', '12', 'Midwest', 'Auburn, Alabama', '5', 'Blue, Orange', '1', 'Tigers', '1', 'Kansas St.'])

    thewriter.writerow(['Clemson', '12', 'Midwest', 'Clemson, South Carolina', '3', 'Orange, Purple', '1', 'Tigers', '1', 'Kansas St.'])

    thewriter.writerow(['Belmont', '12', 'West', 'Nashville, Tennessee', '2', 'Blue, Red', '2', 'Bruins', '5', 'Florida St.'])

    thewriter.writerow(['New Mexico State', '12', 'South', 'Las Cruces, New Mexico', '2', 'Red, White', '5', 'Aggies', '4', 'Wisconsin'])

    thewriter.writerow(['Lipscomb', '13', 'West', 'Nashville, Tennessee', '2', 'Purple, Gold', '1', 'Bisons', '3', 'LSU'])

    thewriter.writerow(['Hofstra', '13', 'Midwest', 'Hempstead, New York', '3', 'Blue, Gold', '2', 'Pride', '3', 'Maryland'])

    thewriter.writerow(['Yale', '13', 'East', 'New Haven, Connecticut', '3', 'Blue, White', '5', 'Bulldogs', '1', 'Nevada'])

    thewriter.writerow(['Old Dominion', '13', 'South', 'Norfolk, Virginia', '3', 'Blue, Grey', '1', 'Monarchs', '5', 'Texas Tech'])

    thewriter.writerow(['Vermont', '14', 'East', 'Burlington, Vermont', '3', 'Green, Gold', '5', 'Catamounts', '5', 'Marquette'])

    thewriter.writerow(['UC Irvine', '14', 'Midwest', 'Irvine, California', '1', 'Blue, Gold', '2', 'Anteaters', '1', 'Houston'])

    thewriter.writerow(['South Dakota State', '14', 'South', 'Brookings, South Dakota', '4', 'Blue, Yellow', '2', 'Jackrabbits', '2', 'Purdue'])

    thewriter.writerow(['Montana', '14', 'West', 'Missoula, Montana', '2', 'Red, Grey', '3', 'Grizzles', '3', 'Kansas'])

    thewriter.writerow(['Texas State', '15', 'West', 'San Marcos, Texas', '4', 'Red, Gold', '5', 'Bobcats', '1', 'Michigan'])

    thewriter.writerow(['Wright State', '15', 'East', 'Fairborn, Ohio', '4', 'Green, Gold', '5', 'Raiders', '5', 'Michigan St.'])

    thewriter.writerow(['Loyola-Chicago', '15', 'Midwest', 'Chicago, Illinois', '4', 'Red, Gold', '5', 'Ramblers', '5', 'North Carolina'])

    thewriter.writerow(['Radford', '15' 'South', 'Radford, Virginia', '3', 'Red, White', '5', 'Highlanders', '4', 'Tennessee'])

    thewriter.writerow(['Bucknell', '16', 'East', 'Lewisburg, Pennsylvania', '4', 'Red, White', '5', 'Bison', '3', 'Duke'])

    thewriter.writerow(['Sam Houston State', '16', 'West', 'Huntsville, Texas', '3', 'Orange, White', '3', 'Bearkats', '2', 'Gonzaga'])

    thewriter.writerow(['Prairie View', '16', 'Midwest','Prairie View, Texas', '5', 'Purple, Gold', '2', 'Panthers', '1', 'Kentucky'])

    thewriter.writerow(['Norfolk State', '16', 'Midwest', 'Norfolk, Virginia', '4', 'Green, Gold', '5', 'Spartans', '5', 'Kentucky'])

    thewriter.writerow(['St. Francis PA', '16', 'South', 'Loretta, Pennslyvania', '5', 'Red, White', '5', 'Red Flash', '5', 'Virginia'])

    thewriter.writerow(['Iona', '16', 'South', 'New Rochelle, NY', '3', 'Red, Gold', '5', 'Gaels', '4', 'Virginia'])


