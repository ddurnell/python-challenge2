import os
import csv
import locale

locale.setlocale( locale.LC_ALL, '' )

# Get the path to the data
data_path = os.path.join(".", "Resources", "budget_data.csv")

# Get a reader
with open(data_path, newline='') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

    # Read the header row
    csv_header = next(csv_reader)
    #print(f"CSV Header: {csv_header}")
 
    # Read through each row of data after the header
    months = 0
    total = 0
    profit = 0
    last_profit = 0
    change = 0
    total_change = 0
    start = True
    big_increase = 0
    big_increase_date = ""
    big_decrease = 0
    big_decrease_date = ""

    for row in csv_reader:
        #print(row[0])
        #print(row[1])
        profit = int(row[1])
        months +=1

        # the first month has no meaning
        if start != True:
            change = profit - last_profit
        else:
            change = 0
            start = False

        last_profit = profit
        total_change += change
        total += profit
        
        # keep track of the biggest changes
        if change >= big_increase:
            big_increase = change
            big_increase_date = row[0]
        elif change <= big_decrease:
            big_decrease = change
            big_decrease_date = row[0]

    results = []
    results.append(f"Total Months: {months}")
    results.append(f"Total: {locale.currency(total)}")
    results.append(f"Average Change: {locale.currency(total_change/(months-1))}")
    results.append(f"Greatest Increase in Profits: {big_increase_date}: {locale.currency(big_increase)}")
    results.append(f"Greatest Decrease in Profits: {big_decrease_date}: {locale.currency(big_decrease)}")

    results_file = 'results.txt'
    try:
        f = open(results_file, 'w')
        for result in results:
            print(result)
            f.write(result + '\n')
    finally:
        f.close()

   