#import dependencies
import os
import csv

# specify path
csvpath = os.path.join("Resources", "budget_data.csv")

# open budget_data
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    # skip first row and set counters to 0
    next(csvreader)
    months = 0
    total = 0
    
    
    # loop through rows
    for row in csvreader:
        
        # add profit/loss to total change
        total = total + int(row[1])

        # add one to counter
        months = months + 1

        # for the first month, set starting profit/loss
        if months == 1:
            start_profit = int(row[1])

    #print answers to terminal
    print("Financial Analysis")
    print("---------------------------------")
    print(f"Total Months: {months}")
    print(f"Total: ${total}")
    print(f"Average Change: ${round((int(row[1]) - start_profit)/(months - 1), 2)}")
    
    #print answers to text file 
    with open(os.path.join("analysis", "analysis.txt"), "w") as file:
        file.write("Financial Analysis \n")
        file.write("--------------------------------- \n")
        file.write(f"Total Months: {months} \n")
        file.write(f"Total: ${total} \n")
        file.write(f"Average Change: ${round((int(row[1]) - start_profit)/(months - 1), 2)} \n")


   
        
