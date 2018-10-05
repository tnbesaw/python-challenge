# Modules
import csv
import os 

# declare & initialize variables
pollResults = {}
total_votes = 0
pct_vote = 0.00

# get path to file
csvpath = os.path.join('Resources', 'election_data.csv')

# open file 
with open(csvpath, newline='') as csvfile:
    
    # read the file
    csvreader = csv.reader(csvfile, delimiter=',')

    # first row is the header ... go next / skip header
    csvheader = next(csvreader)

    # evaluate all remaining rows acquired from csv file
    # row / list postions 0 & 1 can be ignored, only positon 2 is relevant (indicates who vote was for)
    for row in csvreader:
        # keep running total of all votes (1 per record)
        total_votes += 1
        
        # build dictionary of distinct candidates (key) with vote totals (value)
        if row[2] in pollResults:
            # if candidate already within dict, then simply increment value (votes)
            pollResults[row[2]] += 1
        else:
            # if candidate not in dict, then add them with value of 1 (first vote)
            pollResults[row[2]] = 1

#
# format and print results
#
print(f'')
print(f'Election Results')
print(f'-----------------------------')
print(f'Total Votes:        {total_votes}')
print(f'-----------------------------')
for key, value in pollResults.items() :
    pct_vote = str(round(value / total_votes * 100, 4)).rjust(5)
    print ( (key + ':').ljust(10) + (str(pct_vote) + '%').ljust(8) + ('(' + str(value) + ')').rjust(10))

# determine the winner / max pollResults returning the key 
winner = max(pollResults, key=pollResults.get) 
print(f'-----------------------------')
print(f'Winner:              {winner}')
print(f'-----------------------------')