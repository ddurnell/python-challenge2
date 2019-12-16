import os
import csv
import sys

class Logger(object):
    def __init__(self):
        self.terminal = sys.stdout
        self.log = open("results.txt", "w")

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)  

    def flush(self):
        pass    

sys.stdout = Logger()

# Get the path to the data
data_path = os.path.join(".", "Resources", "election_data.csv")

# Three columns: `Voter ID`, `County`, and `Candidate`
# We want:
    # The total number of votes cast
    # A complete list of candidates who received votes
    # The percentage of votes each candidate won
    # The total number of votes each candidate won
    # The winner of the election based on popular vote.

count = 0
candidates = {}
candidate = ""
candidate_count = 0

# Get a reader
with open(data_path, newline='') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

    # Read the header row
    csv_header = next(csv_reader)
    #print(f"CSV Header: {csv_header}")

    for row in csv_reader:
        candidate = row[2]
        if candidate in candidates:
            candidate_count = candidates[candidate]
            candidates[candidate] = candidate_count + 1
            #print(f"Candidate {candidate} has {candidate_count} votes")
        else:
            candidates[candidate] = 1
        count +=1

    candidate_list = []
    candidate_percent = []
    candidate_count = []
    count_test = 0

    winner = ""
    winner_count = 0
    i = 0
    for x in candidates:
        #print(x)
        count_test = count_test + candidates[x]
        candidate_list.append(x)
        candidate_percent.append(candidates[x]/count)
        candidate_count.append(candidates[x])
        if candidate_count[i] > winner_count:
            winner_count = candidate_count[i]
            winner = x
            #print(x)
        i = i+1

def output_results(candidate_list, candidate_percent, candidate_count):
        
    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {count}")
    print("-------------------------")
    j = 0
    for c in candidate_list:
        print(f"{c}: {candidate_percent[j]:.3%} ({candidate_count[j]})")
        j = j+1
    print("-------------------------")
    print(f"Winner: {winner}")

#   Election Results
#   -------------------------
#   Total Votes: 3521001
#   -------------------------
#   Khan: 63.000% (2218231)
#   Correy: 20.000% (704200)
#   Li: 14.000% (492940)
#   O'Tooley: 3.000% (105630)
#   -------------------------
#   Winner: Khan

output_results(candidate_list, candidate_percent, candidate_count)