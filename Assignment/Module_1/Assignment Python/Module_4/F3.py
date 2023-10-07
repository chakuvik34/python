lines =[]
with open(file_name) as f:
    lines.extend(f.readline() for i in xrange(N))
