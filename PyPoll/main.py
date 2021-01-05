import os
import csv
import statistics

# Creating vote counters
Total_votes = 0
Candidates = 0
Correy_votes = 0
Khan_votes = 0
Li_votes = 0
Otooley_votes = 0
Total_tally = []

#Opening cvs file
#main_path = "C:/Users/Oswaldo Moreno/Desktop/python-challenge/PyPoll/Resources/"
#dir_path = os.path.join(main_path, 'election_data.csv')
election_data_file = os.path.join("PyPoll/Resources/election_data.csv")
with open(election_data_file,newline="",encoding="utf-8") as election:
    csvreader = csv.reader(election, delimiter=",") 
    #print(csvreader)
    header = next(csvreader)
#Loop to iterate through votes
    for i in csvreader:
        Total_tally.append(len(i[0]))
        Total_votes > 0
        if i[2] == "Correy":
            Correy_votes += 1
        elif i[2] == "Khan":
            Khan_votes += 1
        elif i[2] == "Li":
            Li_votes += 1
        elif i[2] == "O'Tooley":
            Otooley_votes += 1

#print(Correy_votes)
#print(Khan_votes)
#print(Li_votes)
#print(Otooley_votes)
#print(len(Total_tally))

#Creating dictionary to find the winner from the total votes we counted:

#Candidates_Votes = {
 #   "Correy": "[Correy_votes]",
  ## "Li": "[Li_votes]", 
   # "O'Tooley": "[Otooley_votes]",
#}
Candidates = ["Correy", "Khan", "Li", "O'Tooley"]
Total_of_votes = [Correy_votes, Khan_votes, Li_votes, Otooley_votes]
Sum_of_votes = sum(Total_of_votes)

dictionary_votes_candidates = dict(zip(Candidates,Total_of_votes))
key = max(dictionary_votes_candidates, key=dictionary_votes_candidates.get)
#print(key)
#print(Candidates)
#print(Total_of_votes)
#print(Sum_of_votes)

#work around for calculating percentages
f1 = int(Correy_votes)
f2 = int(Khan_votes)
f3 = int(Li_votes)
f4 = int(Otooley_votes)
f5 = int(Sum_of_votes)

#percentage function

def percent(num1, num2):
    num1 = float(num1)
    num2 = float(num2)
    percentage = '{0:.2f}'.format((num1 / num2 * 100))
    return percentage


#print(type(Correy_percent))

Correy_percent = (percent(f1, Sum_of_votes))
Khan_percent = (percent(f2, Sum_of_votes))
Li_percent = (percent(f3, Sum_of_votes))
Otooley_percent = (percent(f4, Sum_of_votes))


#Analysis

# Screen output
print("Election Results")
print("----------------------------------------------------------")
print((f"Total Votes: {len(Total_tally)}"))
print("----------------------------------------------------------")
print(f"Correy: {(Correy_percent)} % \t Numbers of votes: {Correy_votes}")
print(f"Khan: {(Khan_percent)} % \t \t Numbers of votes: {Khan_votes}")
print(f"Li: {(Li_percent)} % \t \t Numbers of votes: {Li_votes}")
print(f"O'Tooley: {(Otooley_percent)} % \t Numbers of votes: {Otooley_votes}")
print("----------------------------------------------------------")
print("----------------------------------------------------------")
print(f"Winner: {key} !! .... Congratulations!! ")

#To outputfiles:
output_file = ("PyPoll/Analysis/Analysis.txt")
with open(output_file,"w") as file:

    file.write(f"Election Results")
    file.write("\n")
    file.write("----------------------------------------------------------")
    file.write("\n")
    file.write((f"Total Votes: {len(Total_tally)}"))
    file.write("\n")
    file.write("----------------------------------------------------------")
    file.write("\n")
    file.write(f"Correy: {(Correy_percent)} % \t Numbers of votes: {Correy_votes}")
    file.write("\n")
    file.write(f"Khan: {(Khan_percent)} % \t \t Numbers of votes: {Khan_votes}")
    file.write("\n")
    file.write(f"Li: {(Li_percent)} % \t \t Numbers of votes: {Li_votes}")
    file.write("\n")
    file.write(f"O'Tooley: {(Otooley_percent)} % \t Numbers of votes: {Otooley_votes}")
    file.write("\n")
    file.write("----------------------------------------------------------")
    file.write("\n")
    file.write("----------------------------------------------------------")
    file.write("\n")
    file.write(f"Winner: {key} !! .... Congratulations!! ")
