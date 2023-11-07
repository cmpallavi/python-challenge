# In this Challenge, you are tasked with helping a small, rural town modernize
# its vote-counting process.
#
# You will be given a set of poll data called election_data.csv. The dataset is composed of three
# columns: "Voter ID", "County", and "Candidate". Your task is to create a Python script that
# analyzes the votes and calculates each of the following values:
#
# The total number of votes cast
#
# A complete list of candidates who received votes
#
# The percentage of votes each candidate won
#
# The total number of votes each candidate won
#
# The winner of the election based on popular vote
#
# Your analysis should align with the following results:
#
# Election Results
# -------------------------
# Total Votes: 369711
# -------------------------
# Charles Casper Stockham: 23.049% (85213)
# Diana DeGette: 73.812% (272892)
# Raymon Anthony Doane: 3.139% (11606)
# -------------------------
# Winner: Diana DeGette
# -------------------------

import os
import csv

census_csv = os.path.join("Resources", "election_data.csv")

# Lists to store data
totalVotes = 0
# keep dictionary of candidate and votes they got
candidateVoteList = dict()


with open(census_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvreader)

    for row in csvreader:
        totalVotes += 1
        candidate = row[2]
# increment votes a candidate got by 1 to existing value
        candidateVoteList[candidate] = candidateVoteList.get(candidate, 0) + 1

print(candidateVoteList)

print("Election Results")
print("-----------------------------")
print("Total Votes: " + str(totalVotes))
print("-----------------------------")

maxVotes = 0
for candidate in candidateVoteList:
    candidateVotes = candidateVoteList[candidate]
    if maxVotes < candidateVotes:
        maxVotes = candidateVotes
        winner = candidate

    print(f'{candidate}: {candidateVotes*100/totalVotes:.3f}% ({candidateVotes})' )

print("-----------------------------")
print("Winner: " + winner)
print("-----------------------------")
# write this to output file election-results.txt

f = open("analysis/election-results.txt", "w")

f.write("Election Results\n")
f.write("-----------------------------\n")
f.write("Total Votes: " + str(totalVotes) + "\n")
f.write("-----------------------------\n")

# output votes for each candidate
for candidate in candidateVoteList:
    candidateVotes = candidateVoteList[candidate]
    f.write(f'{candidate}: {candidateVotes*100/totalVotes:.3f}% ({candidateVotes})\n' )
# print winner from above
f.write("-----------------------------\n")
f.write("Winner: " + winner + "\n")
f.write("-----------------------------\n")
