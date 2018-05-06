import os
import csv

csvfile = os.path.join(".","PyBank","raw_data","budget_data_1.csv")
output = os.path.join(".","PyBank","output1.csv")

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

    summary_list.append("Total Months: " + str(months))
    summary_list.append("Total Revenue: $" + str(total_revenue))
    summary_list.append("Average Revenue: " + str(total_revenue/months))
    summary_list.append("Greatest Increase in Revenue: " + max_date + " ("+str(greatest_increase)+")")
    summary_list.append("Greatest Decrease in Revenue: " + min_date + " ("+str(greatest_decrease)+")")

    for row in summary_list:
        print(row)

''' to be continued
with open(output, "w") as budgetwriting:
    writer = csv.writer(budgetwriting)
    for row in summary_list:
        writer.write(row)
'''