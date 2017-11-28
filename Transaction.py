from time import strftime

# Might want to move this elsewhere?
def string_to_cents(str):
	# Due to how floating point values are stored on hardware
	# it is better to use whole integers to represent currency
	# and format display text with the decimal '.' later.
	dollars = cents = 0
	exploded = str.split('.')
	if(len(exploded) <= 2 and exploded[0].isdigit()): # There will always be a dollar amount
		dollars = int(exploded[0])
		if(len(exploded) == 2 and exploded[1].isdigit()): # There is not always a mantissa
			cents = int(exploded[1])
			if(len(exploded[1]) == 1): # For case where reads #.9 instead of #.09
				cents *= 10
	return (dollars * 100) + cents # Return value in cents (integer)

string_template = """
	Transaction Date: {0}\n
	Posted Date: {1}\n
	Last Four: {2}\n
	Description: {3}\n
	Category: {4}\n
	Debit: {5} cents\n
	Credit: {6} cents\n
	"""

df = "%Y %b %d, %a %H:%M:%S +0000"

class Transaction:
	'Common base class for all transactions.'

	# Tried to make use of dict to have smaller method signature
	# def __init__(self, *args, **kwargs):
		# self.__dict__.update(kwargs)

	def __init__(self, transaction_date, posted_date, last_four, description, category, debit, credit):
		self.transaction_date = transaction_date
		self.posted_date = posted_date
		self.last_four = last_four
		self.description = description
		self.category = category
		# Don't really need seperate debit/credit vars, for they are mutually exclusive.
		self.debit = string_to_cents(debit)
		self.credit = string_to_cents(credit)

	def to_string(self):
		transaction_date = strftime(df,self.transaction_date)
		posted_date = strftime(df,self.posted_date)
		return string_template.format(transaction_date, posted_date, self.last_four, self.description, self.category, self.debit, self.credit)


	def set_raw(self, raw):
		self.raw = raw