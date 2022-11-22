# Напишите программу для. 
# проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
# ¬ -not 
# ⋁ - or
# ⋀ - and
from random import choice

# Проверка циклом

x = [True, False]       
y = [True, False]
z = [True, False]

for i in x:
  for j in y:
    for k in z:
      if not(i or j or k) == ((not(i)) and (not(j)) and (not(k))):
        print(f"Результат проверки X = {i}, Y = {j}, Z = {k} истинное"  )
      else:
        print(f"Результат проверки X = {i}, Y = {j}, Z = {k} ложное" )
        
# Рандомная проверка

# bool = [True, False]

# x = choice(bool)      
# y = choice(bool)
# z = choice(bool)

# print(f'X = {x}, Y = {y}, Z = {z}')

# if not(x or y or z) == ((not(x)) and (not(y)) and (not(z))):
#   print("Результат проверки" , True)
# else:
#   print("Результат проверки" , False)