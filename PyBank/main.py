import os
import csv

budgetdata = os.path.join('Resources', 'budget_data.csv')

file_to_output = os.path.join("Financial_Analysis.txt")

totalMonths = 0

totalAmount = 0

totalavg = 0.00

diff_list = []

previous = 0

avg_diff = 0

greatInc = ["", 0]

greatDec = ["", 0]

with open (budgetdata) as csvfile:

    csvreader = csv.reader(csvfile, delimiter = ',')

    csv_header = next(csvreader)

    for row in csvreader:
        totalMonths += 1 #finds total months

        totalAmount += int(row[1]) #net total amount

        avg_diff = int(row[1]) - previous

        previous = int(row[1])

        diff_list.append(avg_diff)

        length = len(diff_list) - 1

        if avg_diff < greatDec[1]:
            greatDec[0] = row[0]
            greatDec[1] = avg_diff
        if avg_diff > greatInc[1]:
            greatInc[0] = row[0]
            greatInc[1] = avg_diff
    

totalavg = sum(diff_list[1:]) / length

totalavg = round(totalavg, 2)

with open(file_to_output, 'w') as output:
    results = (
        f'Financial Analysis\n'
        f'----------------------------\n'
        f'Total Months: {totalMonths}\n'
        f'Total: ${totalAmount}\n'
        f'Average Change: ${totalavg}\n'
        f'Greatest Increase in Profits: {greatInc[0]} (${greatInc[1]})\n'
        f'Greatest Decrease in Profits: {greatDec[0]} (${greatDec[1]})\n'
    )
    output.write(results)
    print(results)