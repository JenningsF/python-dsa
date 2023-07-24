from hash_table import HashTable

# initial HashTable constructor
my_ht = HashTable()
print("Initial Constructor")
my_ht.print_table()

# tests set_item method
my_ht.set_item("bolts", 1400)
my_ht.set_item("washers", 50)
my_ht.set_item("lumber", 70)
print("\nSet Item")
my_ht.print_table()