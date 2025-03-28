import sympy as sp

# Define the variable
x = sp.symbols('x')

# Define the function and then differentiate it store in f_prime
# your code goes here
fx = 2*x**3-2*x-5
f_prime = sp.diff(fx,x)

# Display the derivative
f_prime
iterations = 4
x0 = 1.5
# Substitute the initial guess into the derivative
f_prime_at_x0 = f_prime.evalf(subs={x: x0})

# Display the result
f_prime_at_x0

#task 2

results = []
x_current = x0

# Perform the Newton-Raphson method
for i in range(iterations):
    # Calculate f(x_current) and f'(x_current) at the current guess
    # your code goes here [you must check if the derivative at x_current is zero or not]
    fx_val = fx.subs(x,x_current)
    f_prime_val = f_prime.subs(x,x_current)
    if f_prime_val == 0:
        print(f"Derivation is zero at iteraton {i}")
        break
    x_next = x_current - fx_val/f_prime_val
    results.append((i,x_current, fx_val,f_prime_val,x_next))
    x_current = x_next


# Display the results of each iteration
for iteration, x_val, fx_val, fx_prime_val, x_next_val in results:
    print(f"Iteration {iteration}: x={x_val}, f(x)={fx_val}, f'(x)={fx_prime_val}, x_next={x_next_val}")


# Task 3: Calculate the Approximate Relative Error
errors = []
for i in range(1, len(results)):
    previous_x = results[i-1][4]
    current_x = results[i][4]
# compute the absolute relative error and store in variable name 'abs_relative_error'
# your code goes here
    abs_relative_error = abs((current_x - previous_x)/current_x)*100

    errors.append(abs_relative_error)

# Display errors for each iteration
# your code goes here
for i, error in enumerate(errors, start=1):
    print(f"For the iteration {i}: Relative Error is = {error:.4f}%")