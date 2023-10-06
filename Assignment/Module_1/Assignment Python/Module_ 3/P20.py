
list_of_tuples = [(1, 'a'), (2, 'b'), (3, 'c')]

j,k  = zip(*list_of_tuples)

print("First Elements:", list(j))
print("Second Elements:", list(k))
