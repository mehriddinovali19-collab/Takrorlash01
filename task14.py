def sorted_tuple(t1, t2):
    return tuple(sorted(t1 +t2))

a = (3,1,2)
b = (6,4,5)

print(sorted_tuple(a, b))