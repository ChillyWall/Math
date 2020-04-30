import sympy
x = sympy.Symbol('x')
y = sympy.Symbol('y')
z = sympy.Symbol('z')
print(sympy.solve([3 * x + 4 * y - 49 + 2 * z, 8 * x - y - 14 - z, x + y + z - 10], [x, y, z]))
