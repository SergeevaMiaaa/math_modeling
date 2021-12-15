n = int(input('Введите число элементов:'))

s = 0
a = 1
b = 1
print(a)
print(b)

for i in range(n):
  s = a + b
  a = b
  b = s
  print(b)

 