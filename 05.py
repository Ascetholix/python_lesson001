# 5. Напишите программу котороя принимает на вход число и проверяет 
# кратно ли оно 5 и 15 или 15 но не на 30

x = int(input('--> '))
if (((x % 5 == 0) and (x % 10 == 0)) or (x % 15 == 0)) and (x % 30 != 0):
  print(True)
else:
  print(False)