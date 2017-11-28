import os
import csv

input_dir = "input"

def handle_row(r):
	print(r)

def handle_file(file_path):
	print(file_path)
	with open(file_path, 'rb') as f:
		reader = csv.reader(f)
		for row in reader:
			handle_row(row)

# Iterate through every file in the input directory
for f in os.listdir(input_dir):
	file_path = "{0}/{1}".format(input_dir, f)
	handle_file(file_path)