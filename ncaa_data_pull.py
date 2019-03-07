#!/usr/bin/env python3
"""Snippet to read selected NCAA mens basketball team data, write to csv file"""

import requests
import csv

base_url = 'http://site.api.espn.com/apis/site/v2/sports/basketball/mens-college-basketball'
interesting_keys = ('id', 'name', 'abbreviation', 'displayName', 'location', 'color', 'alternateColor')


with open('team_data.csv', 'w') as f:
    # Create a csv writer, set up headers
    writer = csv.DictWriter(f, fieldnames=interesting_keys)
    writer.writeheader()

    # Iterate through first 500 teams.
    # There are gaps in the team_id assignments.
    for team_id in range(1, 500):
        team_url = base_url + f'/teams/{team_id}'
        response = requests.get(team_url)
        print("=" * 60)
        if response.ok:
            team = response.json()['team']
            # Extract a small subset of data from team
            # This is a dictionary comprehension
            subset = {k: team.get(k) for k in interesting_keys}
            for k, v in subset.items():
                print(f'{k} : {v}')
            # write team subset data to csv file
            writer.writerow(subset)
        else:
            print(f"Error fetching team_id: {team_id}")

print("Completed")