###################
# Looks like a counters excersise
###################


import os
import csv
import collections
from collections import Counter

# Creating variables for counters

votes = []


# Opening the csv file for analysis

csvpath = os.path.join(os.path.dirname(__file__), 'election_data.csv')

with open(csvpath) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    #Remove the Header from the document
    csv_header = next(csv_reader)

    for i in csv_reader:
        votes.append(str(i[2]))
    
vote_count = Counter(votes)
print(vote_count)


max_votes = max(vote_count.values())

winner = [i for i in vote_count.keys() if vote_count[i] == max_votes]

percentages = [(j, round(vote_count[j] / len(vote_count) * 100.0)) for j, count in vote_count.most_common()]

print(percentages)
print("heeeeeeerreree")

print("Election Results")
print("----------------------------------------------------------")
print((f"Total Votes: {len(votes)}"))
print("----------------------------------------------------------")
print(f"Correy: {(percentages[1])} % \t Numbers of votes: {percentages[1]}")
# print(f"Khan: {(Khan_percent)} % \t \t Numbers of votes: {Khan_votes}")
# print(f"Li: {(Li_percent)} % \t \t Numbers of votes: {Li_votes}")
# print(f"O'Tooley: {(Otooley_percent)} % \t Numbers of votes: {Otooley_votes}")
# print("----------------------------------------------------------")
# print("----------------------------------------------------------")
# print(f"Winner: {key} !! .... Congratulations!! ")