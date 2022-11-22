# Напишите программу для. 
# проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
# ¬ -not 
# ⋁ - or
# ⋀ - and
from random import choice

bool = [True, False]

x = choice(bool)
y = choice(bool)
z = choice(bool)

print(f'X = {x}, Y = {y}, Z = {z}')

if not(x and y and z) == ((not(x)) or (not(y)) or (not(z))):
  print("Резултат проверки" , True)
else:
  print("Резултат проверки" , False)
