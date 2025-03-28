# Define the function f(x)
def f(x):
    return x**3 - x - 2  # Example: Change this to your target function

# Initialize the interval [a, b]
a = 1.0  # Start of interval
b = 2.0  # End of interval

# Ensure the interval brackets a root
if f(a) * f(b) >= 0:
    raise ValueError("The function must have opposite signs at a and b (f(a)*f(b) < 0).")

# Maximum number of iterations and tolerance
iterations = 20
tolerance = 1e-6

# List to store results
results = []

# Perform the bisection method
for i in range(iterations):
    # Compute the midpoint and evaluate f(xn)
    xn = (a + b) / 2.0
    fxn = f(xn)

    # Store the results of this iteration
    results.append((i + 1, a, b, xn, f(a), f(b), fxn))

    # Check if the root is found or if the interval is small enough
    if abs(fxn) < tolerance or abs(b - a) < tolerance:
        break

    # Update the interval based on the sign of f(xn)
    if f(a) * fxn < 0:
        b = xn
    else:
        a = xn

# Display the results
print("Bisection Method Results:")
for iteration, a, b, xn, fa, fb, fxn in results:
    print(f"Iteration {iteration}: a={a}, b={b}, xn={xn}, f(a)={fa}, f(b)={fb}, f(xn)={fxn}")

# Print the estimated root
print(f"\nEstimated root: {xn}")
print(f"Function value at estimated root: {fxn}")
