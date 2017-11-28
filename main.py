import os
import csv
import time

dot_csv = ".csv"
input_dir = "input"
date_formats = ["%m/%d/%y", "%Y-%m-%d"]
curr_date_format = date_formats[0]

# TODO Consider taking date_format as a parameter instead.
def parse_dates(t_date, p_date):
	global curr_date_format
	try: # Use the most last used date format before trying others.
		transaction_date = time.strptime(t_date, curr_date_format)
		posted_date = time.strptime(p_date, curr_date_format)
	except ValueError as e:
		print(str(e))
		# Iterate through every date format provided.
		for df in date_formats:
			if(df == curr_date_format):
				continue # Skip curr_df as we already tried above.
			try:
				transaction_date = time.strptime(t_date, df)
				posted_date = time.strptime(p_date, df)
				curr_date_format = df # Remember curr_df to speed up future calls.
				break
			except ValueError as e:
				print(str(e))
		return None, None
	return transaction_date, posted_date

def handle_row(r):
	# TODO Refactor from hard-coded indices.
	transaction_date, posted_date = parse_dates(r[0], r[1])
	last_four = r[2].zfill(4)
	description = r[3]
	category = r[4]
	debit = r[5]
	credit = r[6]
	print(description, debit)

def handle_file(file_path):
	print(file_path)
	with open(file_path, 'rb') as f:
		reader = csv.reader(f)
		header = next(reader, None)
		print(header)
		for row in reader:
			handle_row(row)

# Iterate through every file in the input directory.
for f in os.listdir(input_dir):
	if(f.endswith(dot_csv)):
		file_path = "{0}/{1}".format(input_dir, f)
		handle_file(file_path)