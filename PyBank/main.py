# Import modules

import os
import csv
import statistics

# Create list to store values

total_months = []
total_profits = []
average_Change = []
greatest_Increase = []
greatest_Decrease = []
monthly_profit_margin = []
net_change = 0

csvpath = os.path.join(os.path.dirname(__file__), 'Resources', 'budget_data.csv')
#print(csvpath)

with open(csvpath) as budget_data:
    csvreader = csv.reader(budget_data, delimiter=",")

    header = next(csvreader)
    firstrow = next(csvreader)
    rowbefore = (int(firstrow[1]))
    total_months.append(firstrow[0])
    total_profits.append(int(firstrow[1]))
    
# Create loop to append data
    for i in csvreader:
        total_months.append(i[0])
        #print(total_months)
        total_profits.append(int(i[1]))
        #print(total_profits)
        net_change = int(i[1]) - rowbefore
        #print(net_change)
        rowbefore = int(i[1])
        #print(rowbefore)
        monthly_profit_margin.append(net_change)
        #print(net_change)
        # 
#print(monthly_profit_margin)

# Calculate max/min values

maxvalue = max(monthly_profit_margin)
minvalue = min(monthly_profit_margin)

# Join max value with month 

maxvalue_with_month = monthly_profit_margin.index(max(monthly_profit_margin)) + 1 
minvalue_with_month = monthly_profit_margin.index(min(monthly_profit_margin)) + 1

# Output results on screen

print((f"Total Months: {len(total_months)}"))
print((f"Total Amount: $ {sum(total_profits)}"))
print((f"Average Chnage: $ {round(statistics.mean(monthly_profit_margin))}"))
print(f"Greatest Increase in Profits: {total_months[maxvalue_with_month]} $ {(str(maxvalue))}")
print(f"Greatest Decrease in Profits: {total_months[minvalue_with_month]} ${(str(minvalue))}")

# Save data analysis

output_file = os.path.join("Analysis", "Analysis.txt")
with open(output_file,"w") as file:

    file.write("Financial Analysis 2020 Q1")
    file.write("\n")
    file.write("--------------------------")
    file.write("\n")
    file.write((f"Total Months: {len(total_months)}"))
    file.write("\n")
    file.write((f"Total Amount: $ {sum(total_profits)}"))
    file.write("\n")
    file.write((f"Average Chnage: $ {round(statistics.mean(monthly_profit_margin))}"))
    file.write("\n")
    file.write(f"Greatest Increase in Profits: {total_months[maxvalue_with_month]} $ {(str(maxvalue))}")
    file.write("\n")
    file.write(f"Greatest Decrease in Profits: {total_months[minvalue_with_month]} ${(str(minvalue))}")
    file.write("\n")
    file.write("---------------------------------------------------------------------------------------")
