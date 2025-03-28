def calculation(a, b):
    addition = a + b
    subtraction = a - b
    multiplication = a * b
    if b!= 0:
        division = a/b
    else:
        division ='The result is INFINITY'
    return (addition,subtraction,multiplication,division)

x = int(input())
y = int(input())
ans = calculation(x, y)
print(ans)