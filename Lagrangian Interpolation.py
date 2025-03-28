""" Compute the interpolated value using Lagrange interpolation """

def lagrange_interpolation(x, y, x_value):
    n = len(x)
    result = 0
    
    for i in range(n):
        term = y[i]
        for j in range(n):
            if i != j:
                term *= (x_value - x[j]) / (x[i] - x[j])
        result += term

    return result

x = [5, 6, 9, 11]
y = [12, 13, 14, 16]
x_interp = 7  

estimated_value = lagrange_interpolation(x, y, x_interp)
print(f"Estimated value at x = {x_interp}: {estimated_value:.4f}")
