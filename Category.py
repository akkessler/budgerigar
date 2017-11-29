class Category:
	'Object representing category of transaction. Categories and their sub-categories are represented with a "Category tree".'

	def __init__(self, parent, id, name="Name", desc="Description", extremum=0, amount=0, children=[], register=[]):
		self.depth = 0 if (parent is None) else parent.depth + 1
		self.parent = parent
		self.id = id # Long
		self.children = children # Category[]
		self.register = register # Transaction[]
		self.name = name # String
		self.desc = desc # String
		self.extremum = extremum # Integer (cents)
		self.amount = amount # Integer (cents)

	def print_data(self):
		# pid = "root"
		# if(self.depth != 0): 
		# 	pid = str(self.parent.id)
		print(
			"""
			{6}id : {0}\n
			{6}depth : {1}\n
			{6}name : {2}\n
			{6}desc : {3}\n
			{6}extremum : {4}\n
			{6}amount : {5}
			""".format(
				self.id,
				self.depth,
				self.name, 
				self.desc, 
				self.extremum, 
				self.amount,
				self.depth * '\t'
				)
			)
		# if(len(self.children) != 0):
		# 	for c in self.children: 
		# 		c.print_data()