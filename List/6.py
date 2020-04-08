# # Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given
# # list of non-empty tuples.
# a = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# v = []
# g = []
# for i in a:
#     b = (i[1], i[0])
#     v.append(b)
#     v.sort()
# for j in v:
#     c = (j[1], j[0])
#     g.append(c)
# print(g)
a = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
print(sorted(a, key=lambda a: a[1]))
