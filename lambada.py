import math

def a(x):
    return x**2

def b(x, y):
    return math.sqrt(x**2 + y**2)

def c(*args):
    return sum(args) / len(args)

def d(s):
    return "".join(set(s))

# Example usage:
result_a = a(5)
result_b = b(3, 4)
result_c = c(1, 2, 3, 4, 5)
result_d = d("hello")

print("Result a:", result_a)
print("Result b:", result_b)
print("Result c:", result_c)
print("Result d:", result_d)
