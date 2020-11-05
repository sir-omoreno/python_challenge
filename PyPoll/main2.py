import os
import csv
import collections
from collections import Counter

csvpath = os.path.join(os.path.dirname(__file__), 'election_data.csv')

with open(csvpath) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    #Remove the Header from the document
    csv_header = next(csv_reader)

    