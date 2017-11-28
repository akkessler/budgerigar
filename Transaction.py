# Might want to move this elsewhere?
def string_to_float(str):
	try:
		return float(str)
	except ValueError:
		return float(0)

class Transaction:
	'Common base class for all transactions.'

	string_template = """
	Transaction Date: {0}\n
	Posted Date: {1}\n
	Last Four: {2}\n
	Description: {3}\n
	Category: {4}\n
	Debit: {5}\n
	Credit: {6}\n
	"""

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
		self.debit = string_to_float(debit)
		self.credit = string_to_float(credit)

	def to_string(self):
		return self.string_template.format(self.transaction_date, self.posted_date, self.last_four, self.description, self.category, self.debit, self.credit)

	def set_raw(self, raw):
		self.raw = raw