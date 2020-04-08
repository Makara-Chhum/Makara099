# 1.Write a Python script to sort (ascending and descending) a dictionary by value.
import operator


dict = {1: 1, 3: 4, 4: 2, 2: 3}
sort_dict = sorted(dict.items(), key=operator.itemgetter(1))
print("Ascending: ",sort_dict)
sort_dict = sorted(dict.items(), key=operator.itemgetter(1),reverse = True)
print("Descending: ",sort_dict)


