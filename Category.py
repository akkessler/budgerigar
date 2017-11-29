class Category:
	'Object representing category of transaction. Categories and their sub-categories are represented with a "Category tree".'

	def __init__(self, parent, id, name="Name", desc="Description", extremum=0, amount=0, children=[], register=[]):
		self.parent = parent # Can be None for root
		self.id = id # Long
		self.children = children # Category[]
		self.register = register # Transaction[]
		self.name = name # String
		self.desc = desc # String
		self.extremum = extremum # Integer (cents)
		self.amount = amount # Integer (cents)

	def print_data(self):
		pid = "root"
		if(self.parent is not None): pid = str(self.parent.id)
		print("""id : {0}\npid : {5}\nname : {1}\ndesc : {2}\nextremum : {3}\namount : {4}
			""".format(self.id, self.name, self.desc, self.extremum, self.amount, pid))