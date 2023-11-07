# PyBank Instructions
# In this Challenge, you are tasked with creating a Python script to analyze the financial records of 
# your company. You will be given a financial dataset called budget_data.csv. The dataset is composed
#  of two columns: "Date" and "Profit/Losses".

# Your task is to create a Python script that analyzes the records to calculate each of the following 
# values:

# The total number of months included in the dataset

# The net total amount of "Profit/Losses" over the entire period

# The changes in "Profit/Losses" over the entire period, and then the average of those changes

# The greatest increase in profits (date and amount) over the entire period

# The greatest decrease in profits (date and amount) over the entire period

# Your analysis should align with the following results:

# Financial Analysis
# ----------------------------
# Total Months: 86
# Total: $22564198
# Average Change: $-8311.11
# Greatest Increase in Profits: Aug-16 ($1862002)
# Greatest Decrease in Profits: Feb-14 ($-1825558)
import os

# Module for reading CSV files
import csv

csvpath = os.path.join( 'Resources', 'budget_data.csv')
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
#    print(f"CSV Header: {csv_header}")
    # Keeep track of changes in values each month
    changes = []

    # keep list of month names so that we can find
    # month with max and min changes
    months = []


    # Read each row of data after the header
    month_count = 0
    total_profit_loss = 0
    for row in csvreader:
        month_count += 1
        total_profit_loss +=int(row[1])

        if month_count != 1:
            changes.append(int(row[1])- prev_profit_loss)
            months.append(row[0])

        prev_profit_loss = int(row[1])


maxChange = max(changes)
minChange = min(changes)

maxChangeMonth = months[changes.index(maxChange)]
minChangeMonth = months[changes.index(minChange)]

print("# Financial Analysis")
print("-----------------------------")
print("Total Months: " + str(month_count))
print("Total: $" + str(total_profit_loss))
print("Average Change: $" + str(sum(changes) / len(changes)) )
print("Greatest Increase in Profits: " + maxChangeMonth + " ($" + str(maxChange) + ")")
print("Greatest Decrease in Profits: " + minChangeMonth + " ($" + str(minChange) + ")")

# write this to output file financial_analysis.txt
f = open("analysis/financial_analysis.txt", "w")

f.write("# Financial Analysis\n")
f.write("-----------------------------\n")
f.write("Total Months: " + str(month_count) + "\n")
f.write("Total: $" + str(total_profit_loss) + "\n")
f.write("Average Change: $" + str(sum(changes) / len(changes)) + "\n")
f.write("Greatest Increase in Profits: " + maxChangeMonth + " ($" + str(maxChange) + ")\n")
f.write("Greatest Decrease in Profits: " + minChangeMonth + " ($" + str(minChange) + ")\n")

    

