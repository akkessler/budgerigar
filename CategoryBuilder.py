from Category import Category
import pickle

class CategoryBuilder:
	'Object to help build categories and fill out the tree.'

	# TODO Use id module
	cat_count = 0

	id_cat_map = {} # TODO Need to traverse tree to generate on LOAD

	cat_select = None

	def __init__(self, fin=None):
		if((fin is None) or (fin == "")):
			self.root = None
		else:
			self.root = pickle.load(open(fin,'rb')) # FIXME Adjust cat_count to next id.

	def dump(self, fout):
		pickle.dump(self.root, open(fout, 'wb'), protocol=pickle.HIGHEST_PROTOCOL)

	def add_child(self, name, desc, extremum, amount):
		cat_id = CategoryBuilder.cat_count
		CategoryBuilder.cat_count += 1
		cat = Category(self.root, cat_id, name, desc, extremum, amount)
		if(self.root is None):
			self.root = cat
			CategoryBuilder.cat_select = cat
		else:
			self.root.children.append(cat)
		CategoryBuilder.id_cat_map[cat_id] = cat

	def print_root(self):
		if(self.root is not None):
			self.root.print_node_brief()
		else:			
			print('No root!')
		print('')

	def print_children(self):
		if(self.root is not None):
			for c in self.root.children: 
				c.print_node_brief()
		else:
			print('No root!')
		print('')
	
	def select_cat(self, id):
		CategoryBuilder.cat_select = CategoryBuilder.id_cat_map[id]


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
	# cmd_list()

def cmd_list():
	if(cb.root is None):
		print('No root!\n')
	else:
		cb.print_root()
		cb.print_children()

def cmd_select():
	global select
	cat_id = input("id:\n")
	select = id_cat_map[cat_id]

def cmd_menu():
	return int(input("0 : Exit\n1 : Load\n2 : Dump\n3 : List\n4 : Child\n"))

cb = CategoryBuilder()
select = cb.root
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