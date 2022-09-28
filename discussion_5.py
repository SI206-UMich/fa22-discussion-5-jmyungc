import unittest

# Counts the number of a's in a sentence (e.g., a string)
def count_a(sentence):
	total = 0
	for i in range(len(sentence)):
		if sentence[i] == 'a':
			total += 1
	return total


# Item class
# Describes an item to be sold. Each item has a name, a price, and a stock.
class Item:
	# Constructor.
	def __init__(self, name, price, stock):
		self.name = name
		self.price = price
		self.stock = stock

	# Print
	def __str__(self):
		return ("Item = {}, Price = {}, Stock = {}".format(self.name, self.price, self.stock))

# Warehouse class
# A warehouse stores items and manages them accordingly.
class Warehouse:

	# Constructor
	def __init__(self, items = []):
		self.items = items[:]

	# Prints all the items in the warehouse, one on each line.	
	def print_items(self):
		for item in self.items:
			print(item)
			print("\n")	

	# Adds an item to the warehouse	
	def add_item(self, item):
		self.items.append(item)

	# Returns the item in the warehouse with the most stock		
	def get_max_stock(self):
		max_stock = 0
		max_stock_item = None
		for item in self.items:
			if item.stock > max_stock:
				max_stock = item.stock
				max_stock_item = item
		return max_stock_item
	
	# Returns the item in the warehouse with the highest price
	def get_max_price(self):
		max_price = 0
		max_price_item = None
		for item in self.items:
			if item.price > max_price:
				max_price = item.price
				max_price_item = item
		return max_price_item



# Tests
class TestAllMethods(unittest.TestCase):

	# SetUp -- we create a bunch of items for you to use in your tests.
	def setUp(self):
		self.item1 = Item("Beer", 6, 20)
		self.item2 = Item("Cider", 5, 25)
		self.item3 = Item("Water", 1, 100)
		self.item4 = Item("Fanta", 2, 60)
		self.item5 = Item("CocaCola", 3, 40)

	## Check to see whether count_a works
	def test_count_a(self):

	# have all the words start and end with a
		all_word_start_end_a = count_a("applesaucea amazinga agreea")
		self.assertEqual(all_word_start_end_a, 8)

	# have all the words start with a
		all_word_start_a = count_a("apt apartment ain't it")
		self.assertEqual(all_word_start_a, 4)

	# have all words end with a
		all_word_end_a = count_a("coupa copa")
		self.assertEqual(all_word_end_a, 2)

	# have all a sentence
		all_a_sentence = count_a("aaaa")
		self.assertEqual(all_a_sentence, 4)

	# have no As
		no_a_string = count_a("no wonder why")
		self.assertEqual(no_a_string, 0)

	# empty string
		no_letters = count_a("")
		self.assertEqual(no_letters, 0)


	## Check to see whether you can add an item to the warehouse
	def test_add_item(self):
		new_warehouse = Warehouse([self.item1, self.item2])
		new_warehouse.add_item(self.item3)
		new_warehouse.add_item(self.item4)
		self.assertEqual(new_warehouse.items, [self.item1, self.item2, self.item3, self.item4])

	# add items with almost the same name
		self.item6 = Item("Ritz Crackers", 8, 22)
		self.item7 = Item("Ritz Bitz", 9, 22)

		new_warehouse.add_item(self.item6)

		self.assertEqual(new_warehouse.items, [self.item1, self.item2, self.item3, self.item4, self.item6])

		new_warehouse.add_item(self.item7)

		self.assertEqual(new_warehouse.items, [self.item1, self.item2, self.item3, self.item4, self.item6, self.item7])

	## Check to see whether warehouse correctly returns the item with the most stock
	def test_warehouse_max_stocks(self):
		new_warehouse = Warehouse([self.item1, self.item2, self.item3, self.item4, self.item5])
		max_stock_product = new_warehouse.get_max_stock()
		self.assertEqual(max_stock_product, self.item3)

	# all items have same stock
		self.same1 = Item("Mac n Cheese", 2, 12)
		self.same2 = Item("Kool-Aid", 5, 12)
		self.same3 = Item("Folklore CD", 15, 12)

		fun_warehouse = Warehouse([self.same1, self.same2, self.same3])

		max_stocked_item = fun_warehouse.get_max_stock()
		self.assertEqual(max_stocked_item, self.same1)

	# max at end
		
		self.obvious_max = Item("Zebra Cakes", 2, 200)
		fun_warehouse.add_item(self.obvious_max)
		self.assertEqual(fun_warehouse.get_max_stock(), self.obvious_max)

	# all zero stock
		self.item_none1 = Item("Peanut Butter - Crunchy", 4, 0)
		self.item_none2 = Item("Peanut Butter - Smooth", 4.50, 0)
		funner_warehouse = Warehouse([self.item_none1, self.item_none2])
		self.assertEqual(funner_warehouse.get_max_stock(), None)

	# Check to see whether the warehouse correctly return the item with the highest price
	def test_warehouse_max_price(self):
		self.max_item = Item("24k Gold Bracelet", 3000, 4)
		self.not_max_item = Item("Trash Bags", 8, 40)
		self.meh_item = Item("Kenny Chesney CD", 12, 200)

		weird_department_store = Warehouse([self.max_item, self.not_max_item, self.meh_item])
		self.assertEqual(weird_department_store.get_max_price(), self.max_item)

		self.free_item = Item("Reba McEntire's Country Album", 0, 15)
		free_stuff_store = Warehouse([self.free_item])
		self.assertEqual(free_stuff_store.get_max_price(), None)

def main():
	unittest.main()

if __name__ == "__main__":
	main()