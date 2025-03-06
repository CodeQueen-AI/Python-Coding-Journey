from collections import OrderedDict

od = OrderedDict()
od["apple"] = 3
od["banana"] = 5
od["cherry"] = 2
print("Original OrderedDict:", od)

# move_to_end() 
od.move_to_end("apple")
print("After move_to_end('apple'):", od)

# move_to_end() 
od.move_to_end("cherry", last=False)
print("After move_to_end('cherry', last=False):", od)

# popitem() 
removed_item = od.popitem()
print("After popitem():", od, "| Removed Item:", removed_item)

# popitem(last=False) 
removed_item = od.popitem(last=False)
print("After popitem(last=False):", od, "| Removed Item:", removed_item)

# keys() 
print("Keys:", list(od.keys()))

# values()
print("Values:", list(od.values()))

# items() 
print("Items:", list(od.items()))

# update() 
od.update({"mango": 7, "grapes": 4})
print("After update({'mango': 7, 'grapes': 4}):", od)

# copy()
od_copy = od.copy()
print("Copied OrderedDict:", od_copy)

# clear() 
od.clear()
print("After clear():", od)
