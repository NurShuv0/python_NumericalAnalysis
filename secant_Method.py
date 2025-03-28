import math

# Define the function
def f(x):
    return x ** 3 + 2 * x ** 2 + x - 1

# Secant Method function with iteration display
def secant_method(x0, x1, tol=1e-6, max_iter=100):
    iteration_results = []
    
    for i in range(max_iter):
        fx0 = f(x0)
        fx1 = f(x1)

        # Calculate x_(n+1)
        x2 = (x0 * fx1 - x1 * fx0) / (fx1 - fx0)

        # Store iteration details for display
        result = {
            'Iteration': i + 1,
            'x0': x0,
            'x1': x1,
            'x2': x2,
            'f(x0)': fx0,
            'f(x1)': fx1,
            'Absolute Error': abs(x2 - x1)*100
        }
        iteration_results.append(result)

        # Check for convergence
        if abs(x2 - x1) < tol:
            return x2, iteration_results 
        
        # Update values for the next iteration
        x0 = x1
        x1 = x2
    # If max iterations are reached
    return x1, iteration_results

# Initial guesses
x0 = 0
x1 = 1

root, iteration_results = secant_method(x0, x1)

# Displaying the results for all iterations
print("Iteration Results:")
for i, result in enumerate(iteration_results):
    print(f"Iteration {result['Iteration']}: "
          f"x{i} = {result['x0']:.4f}, "
          f"x{i+1} = {result['x1']:.4f}, "
          f"x{i+2} = {result['x2']:.4f}, "
          f"f(x{i}) = {result['f(x0)']:.4f}, "
          f"f(x{i+1}) = {result['f(x1)']:.4f}, "
          f"Absolute Error = {result['Absolute Error']:.4f}%")

# Displaying the approximate root and number of iterations
print(f"\nApproximate Root: {root:.4f}")
print(f"Number of Iterations: {len(iteration_results)}")
