
# How to use calculator:
1. Run `python calculate.py`
2. Enter the figure name. Available are Circle, Square.
3. Enter the function: Area or Perimeter.
4. Enter figure sizes. Radius for circle, one side for square.
5. Get the answer!

# Math formulas
## Area
- Circle: `S = πR²`
- Rectangle: `S = ab`
- Square: `S = a²`
- Triangle: `S = sqrt(p * (p-a) * (p-b) * (p-c))` where p is semiperimeter

## Perimeter
- Circle: `P = 2πR`
- Rectangle: `P = 2a + 2b`
- Square: `P = 4a`
- Triangle: `P = a + b + c`


## rectangle
```python
import math
def area(r): 
'''Принимает число r, возвращает площадь круга pi * r * r'''
    return math.pi * r * r

def perimeter(r):
'''Принимает число r, возвращает периметр круга 2 * pi * r'''
    return 2 * math.pi * r
```

## Example of function input
```python
print(area(5))
print(perimeter(10))
```

## Example of fynction output
```python
25
20*pi
```

## square
```python
def area(a):
'''Принимает число a, возвращает площадь квадрата a * a'''
    return a * a

def perimeter(a):
'''Принимает число a, возвращает периметр квадрата 4 * a'''
    return 4 * a
```
## Example of function input
```python
print(area(5))
print(perimeter(10))
```

## Example of fynction output
```python
25
40
```

## triangle
```python
def area(a, b, c):
'''Принимает число a, b, c возвращает ??? (a + b + c) / 2'''
    return (a + b + c) / 2

def perimeter(a, b, c):
'''Принимает число a, b, c возвращает a + b + c'''
    return a + b + c
```
## Example of function input
```python
print(area(8,6,2))
print(perimeter(8,6,2))
```

## Example of fynction output
```python
8
16
```