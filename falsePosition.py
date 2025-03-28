
def f(x):
    return x**3 - 2 * x - 5
iterations = 10
a = 2
b = 3
#solution of task 1:
fa = f(a)
fb = f(b)
if fa * fb > 0:
    print("THE CHOSEN INTERVAL IS INVALID")
else:
    print("THE CHOSEN INTERVAL  IS VALID")


#solution of task  2:
results = []
for i in range(iterations):
    xn = (a*fb - b*fa)/(fb - fa)
    fxn = f(xn)
    results.append((i + 1, a, b, fa, fb, xn, fxn))
    if(fa * fxn < 0):
        b = xn
        fb = fxn
    else:
        a = xn
        fa = fxn
    
for iterations, a, b, fa, fb, xn, fxn in  results:
    print(f"Iterations {iterations} : a = {a:.4f}, b = {b:.4f}, f(a) = {fa:.4f}, f(b) = {fb:.4f}, xn = {xn:.4f}, fxn = {fxn:.4f}")

#solution of task 3:
errors = []
for i in range(1, len(results)):
    previous_xn = results[i - 1][5]
    current_xn = results[i][5]
    abs_relative_error = abs((current_xn - previous_xn) / current_xn) * 100
    errors.append(abs_relative_error)

for i, (iteration, a, b, fa, fb, xn, fxn) in enumerate(results):
    if i == 0:
        error = "None"
    else:
        error = f"{errors[i - 1]:.4f}%"
    print(f"Iteration {iteration}:xn = {xn:.4f}, Error = {error}")