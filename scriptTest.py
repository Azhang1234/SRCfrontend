import csv
import time
while True:
    with open('data.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for line in csv_reader:
            print(line)
            time.sleep(1)
