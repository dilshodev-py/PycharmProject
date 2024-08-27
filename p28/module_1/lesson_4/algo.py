# =========== 64 ===============
from math import factorial, sqrt

# n, x = map(int, input().split())
# S = 0
# i = 1
# while i <= n:
#     S += (-1) ** (i - 1) / x ** (2 * i)
#     i += 1
# print(f"{S:.3f}")

# =========== 73 ===============

# n, x = map(int, input().split())
# S = 0
# i = 1
# while i <= n:
#     S += x**(2*i-1)/(2*i-1)
#     i += 1
# print(f"{S:.3f}")

# =========== 75 ===============
# from math import factorial
#
# n, k = map(int, input().split())
# S = 0
# i = 0
# while i <= n:
#     S += (-1)**i*k**i/factorial(i)
#     i += 1
# print(f"{S:.3f}")

# =========== 70 ===============

# n, x = map(int, input().split())
# S = 0
# i = 1
# while i <= n:
#     S += (-1)**(i-1)*x**(2*i-1)/factorial(2*i-1)
#     i += 1
# print(f"{S:.3f}")

# =========== 76 ===============
# from math import cos , sin
# a, b, c = map(int, input().split())
# S = 0
# for x in range(a , c+1 , 3):
#     S += pow((a*x + b)/(b**2 + cos(x)**2) , 1/3) - sin(x**2)/(a*b)
#
# print(f"{S:.2f}")

# =========== 78 ===============


# a, b, c = map(int, input().split())
# S = 0
# x, h = a, 2
# while x <= b:
#     S += (a**b+b**x+c**a)/(2*x**2 + 3*a**x)
#     x += h
#
# print(f"{S:.2f}")

# =========== 88 ===============

# a, b, c , d = map(int, input().split())
# S = 0
# x, h = d, 1.5
# while x <= c:
#     S += pow((a*x + b)/(b**2 + cos(x)**2) , 1/5) - sin(x**2)/(a*b)
#     x += h
#
# print(f"{S:.2f}")

# =========== 97 ===============

# from math import *
#
# x, y, c, d = map(int, input().split())
# S , P , SP = 0 , 1 , 0
# n = m = i = 1
#
# while n <= x:
#     S += 1/(5-17*n + n**3)
#     n += 1
#
# while m<= y:
#     P *= sqrt(abs(m-5) + 1)/(m**2+4*m-1)
#     m += 1
#
# while i<=c:
#     k = 1
#     sp = 1
#     while k <= d:
#         sp *= (-1)**i*pow(abs(sin(k)+e**k) , 1/7) / (2*abs(4*i**3-k**4))
#         k += 1
#     SP += sp
#     i += 1
#
# print(f"{S:.2f} {P:.2f} {SP:.2f}")

