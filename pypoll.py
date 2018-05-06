import os
import csv

pollresults = os.path.join(".","PyPoll","raw_data","election_data_1.csv")

with open(pollresults, newline = '') as polldata:
    pollreader = csv.reader(polldata, delimiter = ",")
    firstline = polldata.readline()

    lst = [l[2] for l in pollreader]
    print(lst)