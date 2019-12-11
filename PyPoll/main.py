import os
import csv

electiondata = os.path.join("Resources", "election_data.csv")

file_to_output = os.path.join("election_results.txt")

totalvotes = 0

results = ""

khancount = 0
khanpercent = 0.000

correycount = 0
correypercent = 0.000

licount = 0
lipercent = 0.000

otooleycount = 0
otooleypercent = 0.000

candidatecount = [khancount, correycount, licount, otooleycount]

with open(electiondata) as csvfile:

    csvreader = csv.reader(csvfile, delimiter = ',')

    csv_header = next(csvreader)

    for row in csvreader:
        totalvotes += 1

        if row[2] == "Khan":
            khancount += 1
        elif row[2] == "Correy":
            correycount += 1
        elif row[2] == "Li":
            licount += 1
        elif row[2] == "O'Tooley":
            otooleycount += 1
    
    khanpercent = round((khancount / totalvotes) * 100, 3)

    correypercent = round((correycount / totalvotes) * 100, 3)

    lipercent = round((licount / totalvotes) * 100, 3)

    otooleypercent = round((otooleycount / totalvotes) * 100, 3)

    
with open(file_to_output, 'w') as output:
    results = (
    f"Election Results\n"
    f"-------------------------\n"
    f"Total Votes: {totalvotes}\n"
    f"------------------------\n"
    f"Khan:  {khanpercent} % {khancount}\n"
    f"Correy: {correypercent} % {correycount}\n"
    f"Li: {lipercent} % {licount}\n"
    f"O'Tooley: {otooleypercent} % {otooleycount}\n"
    f"-------------------------\n")
    if [khancount > correycount and khancount > licount and khancount > otooleycount]:
        results += f"winner: Khan\n"
    elif (correycount > khancount and correycount > licount and correycount > otooleycount):
        results += f"Winner: Correy\n"
    elif (licount > khancount and licount > correycount and licount > otooleycount):
        results += f"Winner: Li\n"
    elif (otooleycount > khancount and otooleycount > correycount and otooleycount > licount):
        results += f"Winner: O'Tooley\n"
    
    results += f"-------------------------\n"

    output.write(results)
    print(results)