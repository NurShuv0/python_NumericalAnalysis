def f(x):
    """Define the function f(x) = x^3 + 2x^2 + x - 1."""
    return x**3 + 2*x**2 + x - 1

def secant_method(x0, x1, tol=1e-6, max_iter=100):
    """Approximate the root of the function using the Secant Method."""
    iterations = []  # To store (iteration, x_new, error)
    
    for i in range(max_iter):
        f_x0 = f(x0)
        f_x1 = f(x1)
        
        # Calculate the next approximation using the Secant formula
        x_new = x1 - (f_x1 * (x1 - x0)) / (f_x1 - f_x0)
        
        # Calculate absolute relative error
        if x_new != 0:  # Avoid division by zero
            error = abs((x_new - x1) / x_new) * 100
        else:
            error = float('inf')  # If x_new is 0, we set error to infinity
        
        # Store the current iteration result
        iterations.append((i + 1, x_new, error))
        
        # Check for convergence
        if error < tol:
            break
        
        # Update values for the next iteration
        x0, x1 = x1, x_new
    
    return iterations

# Initial guesses
x0 = 0
x1 = 1

# Run the Secant Method
results = secant_method(x0, x1)

# Display results
print("Iteration |   x_new   | Absolute Relative Error (%)")
for iteration in results:
    print(f"{iteration[0]:9} | {iteration[1]:10.6f} | {iteration[2]:.6f}")