from pathlib import Path
import csv

# create a file path to csv file.
fp = Path.cwd()/"csv_reports"/"Cash_on_Hand.csv"
print(fp.exists())

# read the csv file 
with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader) # skip header
# Go through the rows, 
    for row in reader: 
        # name the according rows
        day = row[0] 
        cash_on_hand = float(row[1]) #float it as we need numberic operation
 
pervious_cash_amount = 0 
current_cash_amount = float(row[1]) 