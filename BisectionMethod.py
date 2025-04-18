# Perform the bisection method
results = []
for i in range(iterations):
    # computing the midpoint and evaluate f(xn)
    xn = (a + b) / 2.0
    fxn = f(xn)

    # Stores the results of this iteration
    results.append((i+1, a, b, xn, f(a), f(b), fxn))
    # your code goes here
    if f(a) * fxn == 0:
      break
    elif f(a) * fxn < 0:
        b = xn  
    else:
        a = xn  


# Display the results
for iteration, a, b, xn, fa, fb, fxn in results:
  print(f"Iteration {iteration}: a={a}, b={b}, xn={xn}, f(a)={fa}, f(b)={fb}, f(xn)={fxn}")
