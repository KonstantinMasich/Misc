import csv
import math
with open('data.csv','rb') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
	for row in spamreader:
		print ' '.join(row)
print "hello"
