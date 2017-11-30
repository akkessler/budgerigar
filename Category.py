print_template = """
{0}id/pid: {1}/{2}\n
{0}name: {3}\n
{0}desc: {4}\n
{0}amt/ext: {5}/{6}"""

print_template_brief = "{0}{1} : {2}"

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

	def print_node(self):
		pid = '-' if self.depth == 0 else self.parent.id
		tabs = '\t' * self.depth
		print(print_template.format(tabs,self.id,pid,self.name,self.desc,self.amount,self.extremum))

	def print_tree(self):
		self.print_node()

	def print_node_brief(self):
		tabs = '\t' * self.depth
		print(print_template_brief.format(tabs,self.id,self.name))