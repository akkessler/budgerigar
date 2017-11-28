import os
import csv

input_dir = "input"

for file_name in os.listdir(input_dir):
	fp = "{0}/{1}".format(input_dir, file_name)
	print(fp)
	with open(fp, 'rb') as f:
		reader = csv.reader(f)
		for row in reader:
			print(row)