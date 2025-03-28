
a = 2
b = 3
# check condition here if the choosen intervals are valid or not
# your code goes here
def f(x):
    return x**3-4*x-9

fa = f(a)
fb = f(b)

if fa * fb < 0:
    print(f"The interval [{a}, {b}] is valid for the bisection method.\n")
else:
    print(f"The interval [{a}, {b}] is invalid for the bisection method. Please select different numbers.")