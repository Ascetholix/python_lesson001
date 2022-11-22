# # Напишите программу которая принимает на вход 5 чисел и находить максимальное из них
# 1, 4, 8, 7, 5 -> 8

list1 = list()

for i in range(5):
  i = int(input(f'Введите {5-i} число: '))
  list1.append(i)
print(list1)

max = 0

for i in list1:
  if i > max:
    max = i
print(f'Макс = {max}')