import csv

def read(fpath):
	with open(fpath) as csvfile:
		readCSV = csv.reader(csvfile, delimiter=',')
		print(readCSV)
