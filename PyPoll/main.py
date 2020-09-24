###################
# Looks like a counters excersise
###################


import os
import csv
import statistics

# Creating variables for counters

candidates = 0
total_votes = 0
candidate_1 = 0
candidate_2 = 0
candidate_3 = 0
candidate_4 = 0
total_tallly = []

# Opening the csv file for analysis

csvpath = os.path.join(r'C:\Users\Oswaldo Moreno\Desktop\homework\python_challenge\PyPoll\election_data.csv')
