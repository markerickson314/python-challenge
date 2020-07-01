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
    count = 0
    total = 0
    previous_pl = 0
    months_list = []
    change_profit_list =[] 
    
    # loop through rows
    for row in csvreader:
        
        #calculate change in profit/loss and reset previous pl
        change_profit = int(row[1]) - previous_pl
        previous_pl = int(row[1])

        #add month and profit change to lists
        months_list.append(row[0])
        change_profit_list.append(change_profit)

        # add profit/loss to total change
        total = total + int(row[1])

        # add one to counter
        count = count + 1

        # for the first month, set starting profit/loss
        if count == 1:
            start_profit = int(row[1])
        
    # return index of max and min profits
    max_index = change_profit_list.index(max(change_profit_list))
    min_index = change_profit_list.index(min(change_profit_list))

    #print answers to terminal
    print("Financial Analysis")
    print("---------------------------------")
    print(f"Total Months: {count}")
    print(f"Total: ${total}")
    print(f"Average Change: ${round((int(row[1]) - start_profit)/(count - 1), 2)}")
    print(f"Greatest Increase in Profits: {months_list[max_index]} (${max(change_profit_list)})")
    print(f"Greatest Increase in Profits: {months_list[min_index]} (${min(change_profit_list)})")
    
    #print answers to text file 
    with open(os.path.join("analysis", "analysis.txt"), "w") as file:
        file.write("Financial Analysis \n")
        file.write("--------------------------------- \n")
        file.write(f"Total Months: {count} \n")
        file.write(f"Total: ${total} \n")
        file.write(f"Average Change: ${round((int(row[1]) - start_profit)/(count - 1), 2)} \n")
        file.write(f"Greatest Increase in Profits: {months_list[max_index]} (${max(change_profit_list)}) \n")
        file.write(f"Greatest Increase in Profits: {months_list[min_index]} (${min(change_profit_list)})")

   
        
