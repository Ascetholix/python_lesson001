# Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).

n = int(input("Введити номер плоскости от 1 до 4: "))

if(n==1):
  print("Диапозон от X = (от 1 до бесконечности), Y = (от 1 до бесконечности)")
elif(n==2):
  print("Диапозон от X = (от -1 до -бесконечности), Y = (от 1 до бесконечности)")
elif(n==3):
  print("Диапозон от X = (от -1 до -бесконечности), Y = (от -1 до -бесконечности)")
elif(n==4):
  print("Диапозон от X = (от 1 до бесконечности), Y = (от -1 до -бесконечности)")
else:
  print("Нет диапазона")