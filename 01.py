# 1. Напишите программу, которая принимает на вход два числа и проверяет, 
# является ли одно число квадратом другого.
#     - 5, 25 -> да
#     - 4, 16 -> да
#     - 25, 5 -> да
#     - 8,9 -> нет

num1 =int(input('Введите 1 число: '))
num2 =int(input('Введите 2 число: '))

if num1<num2:
  num1 = num1**2
else:  
  num2 = num2**2

if num1 == num2:
  print("да")
else:
  print('нет')