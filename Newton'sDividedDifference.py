import numpy as np

def divided_diff_table(x, y):
    """ Compute the divided difference table """
    n = len(x)
    coef = np.zeros([n, n])
    coef[:, 0] = y  

    for j in range(1, n):
        for i in range(n - j):
            coef[i][j] = (coef[i+1][j-1] - coef[i][j-1]) / (x[i+j] - x[i])

    return coef[0] 

def newton_interpolation(x, y, x_value):
    """ Compute interpolated value using Newton's method """
    coeffs = divided_diff_table(x, y)
    n = len(x)
    
    result = coeffs[0]
    term = 1  
    
    for i in range(1, n):
        term *= (x_value - x[i-1])
        result += coeffs[i] * term

    return result, coeffs

x = [5, 6, 9, 11]
y = [12, 13, 14, 16]
x_interp = 7 

estimated_value, coeff_table = newton_interpolation(x, y, x_interp)

print("Newton's Divided Difference Coefficients:", coeff_table)
print(f"Estimated value at x = {x_interp}: {estimated_value:.4f}")
