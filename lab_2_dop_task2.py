a = int(input('Введите значение a:'))
b = int(input('Введите значение b:'))
c = int(input('Введите значение c:'))

if a + b > c or a + c > b or b + c > a:
  if a == b == c:
    print('Равносторонний')
  elif a == b or b == c or a == c:
    print ('Равнобедренный')
  else:
    print ('Разносторонний')
else:
  print('Не существует')
   