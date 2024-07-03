import sympy as sp

# Definir la variable
x = sp.symbols('x')

# Definir los polinomios
p = 1 + 2*x - 3*x**2
q = -2 + x + x**2

# Calcular el producto interno y las normas
inner_product = sp.integrate(p * q, (x, 0, 1))
norm_p = sp.sqrt(sp.integrate(p**2, (x, 0, 1)))
norm_q = sp.sqrt(sp.integrate(q**2, (x, 0, 1)))

# Calcular el ángulo coseno
cos_theta = inner_product / (norm_p * norm_q)

# Calcular la distancia métrica
distance = sp.sqrt(sp.integrate((p - q)**2, (x, 0, 1)))

inner_product, norm_p, norm_q, cos_theta, distance