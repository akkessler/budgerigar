import os
import csv
import time
from Transaction import Transaction

dot_csv = ".csv"
input_dir = "input"
date_formats = ["%m/%d/%y", "%Y-%m-%d"]
curr_date_format = date_formats[0]

# TODO Consider taking date_format as a parameter instead.
def parse_dates(t_date, p_date):
	global curr_date_format
	transaction_date = posted_date = None
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
	return transaction_date, posted_date

def handle_row(raw):
	# TODO Refactor from hard-coded indices.
	transaction_date, posted_date = parse_dates(raw[0], raw[1])
	last_four = raw[2].zfill(4)
	description = raw[3]
	category = raw[4]
	debit = raw[5]
	credit = raw[6]
	transaction = Transaction(transaction_date, posted_date, last_four, description, category, debit, credit)
	transaction.set_raw(raw)
	transactions.append(transaction)

def handle_file(file_path):
	print(file_path)
	with open(file_path, 'rb') as f:
		reader = csv.reader(f)
		header = next(reader, None)
		print(header)
		for row in reader:
			handle_row(row)

# Iterate through every file in the input directory.
transactions = []
for f in os.listdir(input_dir):
	if(f.endswith(dot_csv)):
		file_path = "{0}/{1}".format(input_dir, f)
		handle_file(file_path)

debits = []; credits = []
debit_total = credit_total = 0
for t in transactions:
	# Strictly checking both conditions, the redundancy is probably ok. 
	print(t.to_string())
	if(t.debit > 0 and t.credit == 0):
		debits.append(t)
		debit_total += t.debit
	elif(t.debit == 0 and t.credit > 0):
		credits.append(t)
		credit_total += t.credit
	else:
		print("Not credit nor debit?") # TODO Handle this scenario.

t = len(transactions)
d = len(debits)
c = len(credits)
print(t,d,c,t-d-c)
print(debit_total, credit_total, debit_total-credit_total)