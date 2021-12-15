a = 2
b = 5
length = 10

g = []
for n in range(1, length+1):
  g.append(a * b ** (n - 1))

print(g)

