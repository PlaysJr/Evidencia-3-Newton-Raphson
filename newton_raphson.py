import sympy as sp

def menu():
   
    print("\n-- MENU PRINCIPAL --")
    print("1. Resolver con metodo newton-raphson")
    print("2. Salir")
    
    while True:
        try:
            opcion = int(input("Selecciona una opcion: "))
            if opcion in [1, 2]:
                return opcion
            else:
                print("Opcion no valida. Ingresa un numero valido.")
        except ValueError:
            print("Por favor, ingresa un numero xd.")

def newton_raphson(f_expr_str, x0, tol, max_iter):
    #Convertir cadena a expresion 
    x = sp.symbols('x')
    f_expr = sp.sympify(f_expr_str)
    f_prime_expr = sp.diff(f_expr, x)

    f = sp.lambdify(x, f_expr, 'math')
    f_prime = sp.lambdify(x, f_prime_expr, 'math')

    print(f"\nMetodo de Newton-Raphson para f(x) = {f_expr_str}")
    print(f"{'Iter':<6}{'x_n':<20}{'f(x_n)':<20}")
    print("-" * 50)

    for i in range(1, max_iter + 1):
        fx = f(x0)
        fpx = f_prime(x0)

        if fpx == 0:
            print("La derivada es cero, el metodo no puede continuar.")
            return None

        x1 = x0 - fx / fpx
        print(f"{i:<6}{x0:<20.10f}{fx:<20.10f}")

        if abs(x1 - x0) < tol:
            print(f"\nRaíz aproximada encontrada: {x1:.10f}")
            return x1

        x0 = x1

    print("\nNo se alcanzo la tolerancia en el numero maximo de iteraciones.")
    return None