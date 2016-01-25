from csv import reader
from datetime import date
from datetime import datetime
from datetime import time
from datetime import timedelta
from fileinput import input
from statistics import median
from statistics import stdev

csv_reader = reader(input())

info = {}
network_rows = []
for row in csv_reader:
    category = row[0]
    if category == 'AAA':
        info[row[1]] = row[2]
    elif category == 'NET':
        network_rows.append(row)


start = datetime.strptime("T".join([info["date"], info["time"]]),
                          "%d-%b-%YT%H:%M.%S")
eth0_read = [(start + timedelta(0, index * 2), float(item[2])) for index, item in
             list(enumerate(network_rows))[1:]]

out_file = open('out.dat', 'w')
out_file.write('X\tY\n')
for row in eth0_read:
    out_file.write('{}\t{}\n'.format(row[0], row[1]))

rates = [row[1] for row in eth0_read]
eth0_read_median = median(rates)
eth0_read_stdev = stdev(rates)
limit = eth0_read_median + 3 * eth0_read_stdev

print("median = {}".format(eth0_read_median))
print("stdev = {}".format(eth0_read_stdev))
for row in eth0_read:
    if row[1] > limit:
        print("Above limit: {} @ {}".format(row[0], row[1]))
