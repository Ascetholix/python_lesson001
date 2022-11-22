# Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве.
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21
# AB = sqrt((xb - xa)**2 + (yb - ya)**2)  формула 
import math

x = list()
y = list()

for x1 in range(2):
  x1 = int(input(f"Ведите точку X{x1+1} = "))
  x.append(x1)
  
for y1 in range(2):
  y1 = int(input(f"Ведите точку Y{y1+1} = "))
  y.append(y1)
  
distance = math.sqrt((x[0]-x[1])**2 + (y[0]-y[1])**2)
print(round(distance,2))