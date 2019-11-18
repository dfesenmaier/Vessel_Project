import csv
import operator

with open('ais_sample.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    with open('new_ais_sample.csv', 'w') as new_file:
        fieldnames = ['id', 'mmsi', 'x', 'y','cog']

        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter='\t')

        csv_writer.writeheader()

        






