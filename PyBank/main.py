# Modules
import csv
import os 
from datetime import datetime

# declare & initialize variables
budgetData1 = [] # list to store dates
budgetData2 = [] # list to store profit
budgetData3 = [] # list to store change

# declare change / prior loop variables
prior_value= 0.00
change_value = 0.00

# declare variables for summary
cnt_value = 0
tot_value = 0.00
# find max / min changes 
max_value = 0.00 
max_index = 0.00 
max_date = ""
min_value = 0.00
min_index = 0.00 
min_date = ""
# declare variables used for average calc
first_value = 0.00
last_value = 0.00
avg_value = 0.00

# get path to file
csvpath = os.path.join('Resources', 'budget_data.csv')

# open file 
with open(csvpath, newline='') as csvfile:
    
    # read the file
    csvreader = csv.reader(csvfile, delimiter=',')

    # first row is the header ... go next / skip header
    csvheader = next(csvreader)

    # assign each csv row value into lists (creating extra list to store change from month to month)
    # row postion 0 is date | postion 1 is value 
    for row in csvreader:
        # calculate change from prior record vs current row
        change_value = float(row[1]) - prior_value
        
        # build lists of values 
        budgetData1.append(datetime.strptime(row[0], '%b-%Y'))
        budgetData2.append(float(row[1]))
        budgetData3.append(float(change_value))

        # store profit value into variable for  eval on next loop iteration (represents prior value)
        prior_value = float(row[1]) # keep track of prior value

# calculate raw totals
cnt_value = len(budgetData1)
tot_value = round(sum(budgetData2)) 

# find the largest increase in profit from month to month (max) ... use value to get index and associated date
max_value = max(budgetData3) 
max_index = budgetData3.index(max_value)
max_date = budgetData1[max_index]

# find the largest decrease in profit from month to month (min) ... use value to get index and associated date
min_value = min(budgetData3) 
min_index = budgetData3.index(min_value)
min_date = budgetData1[min_index]

# take the last value minus the first value and divide by the amout of periods bewteen
first_value = budgetData2[0] 
last_value =  budgetData2[-1]
avg_value = round((last_value - first_value) / (cnt_value - 1),2)

#
# format and print results
#
print(f'')
print(f'Financial Analysis')
print(f'------------------------------------------------------------')
print(f'Total Months:                  {cnt_value}')
print(f'Total:                         ${tot_value}')
print(f'Average Change:                ${avg_value}')
print('Greatest Increase in Profits:  ' + datetime.strftime(max_date,'%b-%Y') + '  $(' + str(round(max_value)) + ')')
print('Greatest Decrease in Profits:  ' + datetime.strftime(min_date,'%b-%Y') + '  $(' + str(round(min_value)) + ')')   

#
# format and export results
#
output_path = os.path.join("results.txt")
with open(output_path, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow((f'',))
        csvwriter.writerow((f'Financial Analysis',))
        csvwriter.writerow((f'------------------------------------------------------------',))
        csvwriter.writerow((f'Total Months:                  {cnt_value}',))
        csvwriter.writerow((f'Total:                         ${tot_value}',))
        csvwriter.writerow((f'Average Change:                ${avg_value}',))
        csvwriter.writerow(('Greatest Increase in Profits:  ' + datetime.strftime(max_date,'%b-%Y') + '  $(' + str(round(max_value)) + ')',))
        csvwriter.writerow(('Greatest Decrease in Profits:  ' + datetime.strftime(min_date,'%b-%Y') + '  $(' + str(round(min_value)) + ')',))   