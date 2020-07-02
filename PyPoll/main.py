# import dependencies
import os
import csv

# specify path
csvpath = os.path.join("Resources", "election_data.csv")

# open csv and skip header row
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)

    # define variables
    total_votes = 0
    cand_list = []
    cand_votes = {}

    # loop through rows
    for row in csvreader:
        
        # count votes 
        total_votes = total_votes + 1

        # read name of vote
        name=row[2]

        # if new name add to list and add one vote
        if name not in cand_list:
            cand_list.append(name)
            cand_votes[name] = 1

        # else add one vote    
        else:
            cand_votes[name] = cand_votes[name] + 1

    # print answers to terminal
    print("Election Results")
    print("---------------------------")
    print(f"Total Votes: {total_votes}")
    print("---------------------------")
    print(f"{cand_list[0]}: {(cand_votes[cand_list[0]]/total_votes)*100:.3f}% ({cand_votes[cand_list[0]]})")
    print(f"{cand_list[1]}: {(cand_votes[cand_list[1]]/total_votes)*100:.3f}% ({cand_votes[cand_list[1]]})")
    print(f"{cand_list[2]}: {(cand_votes[cand_list[2]]/total_votes)*100:.3f}% ({cand_votes[cand_list[2]]})")
    print(f"{cand_list[3]}: {(cand_votes[cand_list[3]]/total_votes)*100:.3f}% ({cand_votes[cand_list[3]]})")
    print("---------------------------")
    print(f"Winner: {max(cand_votes, key=cand_votes.get)}")
    print("---------------------------")

    # print answers to text file
    with open(os.path.join("analysis", "analysis.txt"), "w") as file:
        file.write("Election Results \n")
        file.write("--------------------------- \n")
        file.write(f"Total Votes: {total_votes} \n")
        file.write("--------------------------- \n")
        file.write(f"{cand_list[0]}: {(cand_votes[cand_list[0]]/total_votes)*100:.3f}% ({cand_votes[cand_list[0]]}) \n")
        file.write(f"{cand_list[1]}: {(cand_votes[cand_list[1]]/total_votes)*100:.3f}% ({cand_votes[cand_list[1]]}) \n")
        file.write(f"{cand_list[2]}: {(cand_votes[cand_list[2]]/total_votes)*100:.3f}% ({cand_votes[cand_list[2]]}) \n")
        file.write(f"{cand_list[3]}: {(cand_votes[cand_list[3]]/total_votes)*100:.3f}% ({cand_votes[cand_list[3]]}) \n")
        file.write("--------------------------- \n")
        file.write(f"Winner: {max(cand_votes, key=cand_votes.get)} \n")
        file.write("--------------------------- \n")