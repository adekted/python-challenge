import os
import csv

csvfile = os.path.join(".","raw_data","budget_data_2.csv")
output = os.path.join(".","output1.txt")

summary_list = ["Financial Analysis","----------------------------"]
with open(csvfile, newline = '') as budgetdata:
    reader = csv.reader(budgetdata, delimiter = ",")
    firstline = budgetdata.readline()

    months = 0
    total_revenue = 0
    greatest_increase = 0
    greatest_decrease = 0

    for row in reader:
        months = months + 1
        total_revenue = total_revenue + int(row[1])

        if int(row[1]) >= 0 and int(row[1]) >= greatest_increase:
            max_date = row[0]
            greatest_increase = int(row[1])
        
        elif int(row[1]) <= 0 and int(row[1]) <= greatest_decrease:
            min_date = row[0]
            greatest_decrease = int(row[1])

with open(output,'w') as resultsfile:
    resultsfile.write("Financial Analysis\n")
    resultsfile.write("----------------\n")
    resultsfile.write("Total Months: " + str(months) + "\n")
    resultsfile.write("Total Revenue: $" + str(total_revenue) + "\n")
    resultsfile.write("Average Revenue: " + str(total_revenue/months)  + "\n")
    resultsfile.write("Greatest Increase in Revenue: " + max_date + " ("+str(greatest_increase)+")\n")
    resultsfile.write("Greatest Decrease in Revenue: " + min_date + " ("+str(greatest_decrease)+")")

with open(output, 'r') as readresults:
    print(readresults.read())