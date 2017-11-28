import os
import csv
import time
from Transaction import Transaction

dot_csv = ".csv"
input_dir = "input"
date_formats = ["%m/%d/%y", "%Y-%m-%d"]
curr_date_format = date_formats[0] # 'curr'ent date format
currency_format = "${0}.{1} USD"

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
	# print(file_path)
	with open(file_path, 'r') as f:
		reader = csv.reader(f)
		header = next(reader, None)
		# print(header)
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
expense_by_category = {}
for t in transactions:
	# Strictly checking both conditions, the redundancy is probably ok. 
	# print(t.to_string())
	if(t.debit > 0 and t.credit == 0):
		debits.append(t)
		debit_total += t.debit
	elif(t.debit == 0 and t.credit > 0):
		credits.append(t)
		credit_total += t.credit
	else:
		print("Not credit nor debit?") # TODO Handle this scenario.

	if(t.category in expense_by_category):
		expense_by_category[t.category] += t.debit - t.credit
	else:
		expense_by_category[t.category] = t.debit - t.credit

debit_total_str = currency_format.format(debit_total // 100, str(debit_total % 100).zfill(2))
credit_total_str = currency_format.format(credit_total // 100, str(credit_total % 100).zfill(2))

print("# of Debits : {0}\n# of Credits : {1}\n".format(len(debits), len(credits)))
print("Debit Total : {0}\nCredit Total : {1}\n".format(debit_total_str, credit_total_str))
for key in expense_by_category:
	value = expense_by_category[key]
	value_str = currency_format.format(value // 100, str(value % 100).zfill(2))
	print("{0} : {1}".format(key, value_str))