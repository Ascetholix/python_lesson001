# Напишите программу, которая принимает на вход цифру, обозначающую день недели,
# и проверяет, является ли этот день выходным.
# - 6 -> да
# - 7 -> да
# - 1 -> нет

day = int(input("Введите цифру от 1 до 7: "))

if(day < 6 and day != 0):
  print("Не выходной")
elif(day >= 6 and day <= 7):
  print("Да выходной")
else:
  print("Некореткно не ввели от 1 до 7")