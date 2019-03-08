import csv

with open('location_list.csv', 'w') as location_file:
    fieldnames = {'School', 'Location', 'Location Rank'}

    csv_writer = csv.DictWriter(location_file, fieldnames=fieldnames)
    csv_writer.writeheader()

    csv_writer.writerow({'Gonzaga', 'Spokane, Washington'})
    csv_writer.writerow({'Duke', 'Durham, North Carolina'})
    csv_writer.writerow({'Virginia', 'Charlottesville, Virginia'})
    csv_writer.writerow({'Kentucky', 'Lexington, Kentucky'})
    csv_writer.writerow({'Tennessee', 'Knoxville, Tennessee'})
    csv_writer.writerow({'North Carolina', 'Chapel Hill, North Carolina'})
    csv_writer.writerow({'Michian State', 'East Lansing, Michigan'})
    csv_writer.writerow({'Michigan', 'Ann Arbor, Michigan'})
    csv_writer.writerow({'Houston', 'Houston, Texas'})
    csv_writer.writerow({'Purdue', 'West Lafayette, Indiana'})
    csv_writer.writerow({'Marquette', 'Milwaukee, Wisconsin'})
    csv_writer.writerow({'Kansas', 'Lawrence, Kansas'})
    csv_writer.writerow({'LSU', 'Baton Rouge, Louisiana'})
    csv_writer.writerow({'Maryland', 'College Park, Maryland'})
    csv_writer.writerow({'Texas Tech', 'Lubbock, Texas'})
    csv_writer.writerow({'Nevada', 'Reno, Nevada'})
    csv_writer.writerow({'Kansas State', 'Manhattan, Kansas'})
    csv_writer.writerow({'Iowa State', 'Ames, Iowa'})
    csv_writer.writerow({'Florida State', 'Tallahassee, Florida'})
    csv_writer.writerow({'Wisconsin', 'Madison, Wisconsin'})
    csv_writer.writerow({'Virginia Tech', 'Blacksburg, Virginia'})
    csv_writer.writerow({'Iowa', 'Iowa City, Iowa'})
    csv_writer.writerow({'Cincinnati', 'Cincinnati, Ohio'})
    csv_writer.writerow({'Buffalo', 'Buffalo, New York'})
    csv_writer.writerow({'Washington', 'Seattle, Washington'})
    csv_writer.writerow({'Baylor', 'Waco, Texas'})
    csv_writer.writerow({'Villanova', 'Villanova, Pennsylvania'})
    csv_writer.writerow({'Syracuse', 'Syracuse, New York'})
    csv_writer.writerow({'Mississippi State', 'Starkville, Mississippi'})
    csv_writer.writerow({'Louisville', 'Louisville, Kentucky'})
    csv_writer.writerow({"St. John's", 'New York City, New York'})
    csv_writer.writerow({'Ole Miss', 'Oxford, Mississippi'})
    csv_writer.writerow({'Oklahoma', 'Norman, Oklahoma'})
    csv_writer.writerow({'NC State', 'Raleigh, North Carolina'})
    csv_writer.writerow({'VCU', 'Richmond, Virginia'})
    csv_writer.writerow({'Temple', 'Philadelphia, Pennsylvania'})
    csv_writer.writerow({'UCF', 'Orlando, Florida'})
    csv_writer.writerow({'TCU', 'Fort Worth, Texas'})
    csv_writer.writerow({'Wofford', 'Spartanburg, South Carolina'})
    csv_writer.writerow({'Texas', 'Austin, Texas'})
    csv_writer.writerow({'Florida', 'Gainesville, Florida'})
    csv_writer.writerow({'Arizona State', 'Tempe, Arizona'})
    csv_writer.writerow({'Seton Hall', 'Newark, New Jerseyy'})
    csv_writer.writerow({'Minnesota', 'Minneapolis, Minnesota'})
    csv_writer.writerow({'Ohio State', 'Columbus, Ohio'})
    csv_writer.writerow({'Alabama', 'Tuscaloosa, Alabama'})
    csv_writer.writerow({'Auburn', 'Auburn, Alabama'})
    csv_writer.writerow({'Clemson', 'Clemson, South Carolina'})
    csv_writer.writerow({'Belmont', 'Nashville, Tennessee'})
    csv_writer.writerow({'New Mexico State', 'Las Cruces, New Mexico'})
    csv_writer.writerow({'Lipscomb', 'Nashville, Tennessee'})
    csv_writer.writerow({'Hofstra', 'Hempstead, New York'})
    csv_writer.writerow({'Yale', 'New Haven, Connecticut'})
    csv_writer.writerow({'Old Dominion', 'Norfolk, Virginia'})
    csv_writer.writerow({'Vermont', 'Burlington, Vermont'})
    csv_writer.writerow({'UC Irvine', 'Irvine, California'})
    csv_writer.writerow({'South Dakota State', 'Brookings, South Dakota'})
    csv_writer.writerow({'Montana', 'Missoula, Montana'})
    csv_writer.writerow({'Texas State', 'San Marcos, Texas'})
    csv_writer.writerow({'Wright State', 'Fairborn, Ohio'})
    csv_writer.writerow({'Loyola-Chicago', 'Chicago, Illinois'})
    csv_writer.writerow({'Radford', 'Radford, Virginia'})
    csv_writer.writerow({'Bucknell', 'Lewisburg, Pennsylvania'})
    csv_writer.writerow({'Sam Houston State', 'Huntsville, Texas'})
    csv_writer.writerow({'Prairie View', 'Prairie View, Texas'})
    csv_writer.writerow({'Norfolk State', 'Norfolk, Virginia'})
    csv_writer.writerow({'St. Francis PA', 'Loretta, Pennslyvania'})
    csv_writer.writerow({'Iona', 'New Rochelle, NY'})