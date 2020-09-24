import os
import csv
import statistics

total_months = []
total_profits = []
average_Change = []
greatest_Increase = []
greatest_Decrease = []
monthly_profit_margin = []
net_change = 0

csvpath = os.path.join(r'C:\Users\Oswaldo Moreno\Desktop\homework\python_challenge\PyBank\budget_data.csv')
print(csvpath)

with open(csvpath) as budget_data:
    csvreader = csv.reader(budget_data, delimiter=",")
#print(budget_data)

    header = next(csvreader)
    firstrow = next(csvreader)
    rowbefore = (int(firstrow[1]))
    print(rowbefore)

    total_months.append(firstrow[0])
    total_profits.append(int(firstrow[1]))

    #rowbefore = (int(firstrow[1]))
    #print(rowbefore)
    
# Loop loopp loooop pa dooooo
    for i in csvreader:
        total_months.append(i[0])
        #print(total_months)
        total_profits.append(int(i[1]))
        #print(total_profits)
        net_change = int(i[1]) - rowbefore
        print(net_change)
        rowbefore = int(i[1])
        #print(rowbefore)
        monthly_profit_margin.append(net_change)
        #print(net_change)
        # 
#print(monthly_profit_margin)

maxvalue = max(monthly_profit_margin)
minvalue = min(monthly_profit_margin)
maxvalue_with_month = monthly_profit_margin.index(max(monthly_profit_margin)) + 1 

minvalue_with_month = monthly_profit_margin.index(min(monthly_profit_margin)) + 1

print((f"Total Months: {len(total_months)}"))
print((f"Total Amount: $ {sum(total_profits)}"))
print((f"Average Chnage: $ {round(statistics.mean(monthly_profit_margin))}"))
print(f"Greatest Increase in Profits: {total_months[maxvalue_with_month]} $ {(str(maxvalue))}")
print(f"Greatest Decrease in Profits: {total_months[minvalue_with_month]} ${(str(minvalue))}")


