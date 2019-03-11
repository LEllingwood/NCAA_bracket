NCAA Bracket Selection - 2019

OVERVIEW:
Every year, 68 of the country's 351 Men's Division 1 Basketball teams participate in March Madness - the intensive tournament that determines the national championship.  These March Madness teams consist of the winners of each of 32 individual participating conferences, as well as 36 other at-large teams selected by the NCAA's selection committee. 

Teams are officially selected for participation on Selection Sunday, held this year on March 17, 2019.  As this presentation will take place before Selection Sunday, the teams used in this bracket selection will be based on Sports Commentator Andy Katz' 2019 bracket predictions.  The teams in this program can be substituted for other teams after the official seeding has taken place.

Of the 68 teams that participate, 8 wildcard teams compete for 4 'play in' spots.  Those four spots are the "First Four", and are decided shortly before the tournament begins.  This program identifies the 8 teams competing for wildcard spots and determines the winners basedon my selection criteria.

DATA:  Because Selection Sunday has not yet happened, the beginning 68 teams are being hard coded from A. Katz predictions.  No web-scrapable or apis were available for obtaining this information.  Team colors were webscraped both from teamcolorcodes.com and each team's wikipedia webpages. We were able to obtain certain information about the teams (such as unique id's) from a Github page containing links to ESPN data.

SELECTION CRITERIA:

Teams are judged on three criteria, in order of importance:
    1.  Mascot - given a weight of 3
    2.  Team colors - given a weight of 2.25
    3.  Location - given a weight of 1

Each criterium will be ranked from 5 to 1, with 5 being the best, 1 being the worst.

Mascot: cats, dogs, and cat or dog related mascots, as well as 'weird' or 'unique' mascots (such as the anteater) will be given the highest rank.  Other animals will be given preference over non-animal mascots.

Team Colors: Purple, grey, orange, and blue are given higher ranks than red, green, yellow, and white.

Location: Highest ranks will be given to places I would like to visit on vacation.  This rank isn't necessarily intuitive; for instance, I would rank locations in Florida lower than Washington.

MODULES: Matplotlib, csv, tabulate, argparse ...

THIS CRITERIA IS PROVEN.  I've won two NCAA bracket pools using exactly this criteria.  Good luck!