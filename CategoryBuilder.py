from Category import Category
import pickle
import fileinput

class CategoryBuilder:
	'Object to help build categories and fill out the tree.'

	# TODO Use id module
	cat_count = 0

	def __init__(self, fin=None):
		cat_id = CategoryBuilder.cat_count
		CategoryBuilder.cat_count += 1
		if(fin is None or fin == ""):
			self.root = Category(None, cat_id)
		else:
			self.root = pickle.load(open(fin,'rb'))

	def dump(self, fout):
		pickle.dump(self.root, open(fout, 'wb'), protocol=pickle.HIGHEST_PROTOCOL)

	def add_child(self, name, desc, extremum, amount):
		cat_id = CategoryBuilder.cat_count
		CategoryBuilder.cat_count += 1
		cat = Category(self.root, cat_id, name, desc, extremum, amount)
		self.root.children.append(cat)

	def print_root(self):
		self.root.print_data()

	def print_children(self):
		for c in self.root.children: c.print_data()


def cmd_load():
	global cb
	fin = input("fin: *.pkl\n")
	cb = CategoryBuilder(fin)

def cmd_dump():
	fout = input("fout: *.pkl\n")
	cb.dump(fout)

def cmd_child():
	name = input("Name:\n")
	desc = input("Description:\n")
	extremum = input("Extremum:\n")
	amount = input("Amount:\n")
	cb.add_child(name, desc, extremum, amount)
	cmd_list()

def cmd_list():
	cb.print_root()
	cb.print_children()

def cmd_menu():
	return int(input("0 : Exit\n1 : Load\n2 : Dump\n3 : List\n4 : Child\n"))

cmd = cmd_menu() # prime that loop!~
while(cmd != 0):
	print("")
	if(cmd == 1):
		cmd_load()
	elif(cmd == 2):
		cmd_dump()
	elif(cmd == 3):
		cmd_list()
	elif(cmd == 4):
		cmd_child()
	cmd = cmd_menu()