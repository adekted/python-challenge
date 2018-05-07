import os
import csv

pollresults = os.path.join(".","PyPoll","raw_data","election_data_1.csv")
output = os.path.join(".","PyPoll","results.txt")


with open(pollresults, newline = '') as polldata:
    pollreader = csv.reader(polldata, delimiter = ",")
    firstline = polldata.readline()

    votes = 0
    poll_results = {}

    for row in pollreader:
        votes = votes + 1
        if row[2] in poll_results.keys():
            poll_results[row[2]] = poll_results[row[2]] + 1
        else:
            poll_results[row[2]] = 1
    
    vote_results = []
    for i, k in poll_results.items():
        vote_results.append((i, k, (round((float(k/votes)*100),2))))

    max_votes = 0
    winner = ''
    for j in vote_results:
        if j[1] >= max_votes:
            max_votes = j[1]
            winner = j[0]

with open(output,'w') as resultsfile:
    resultsfile.write("Election Results\n")
    resultsfile.write("----------------\n")
    for result in vote_results:
        resultsfile.writelines(result[0] + ": " + str(result[2]) + "% (" + str(result[1]) + ")\n")
    resultsfile.write("----------------\n")
    resultsfile.write("Winner: " + winner)

with open(output, 'r') as readresults:
    print(readresults.read())