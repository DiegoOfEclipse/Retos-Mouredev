def cuenta_regresiva(numero):
    if numero == 0:
        print("Se Termino la Cuenta Regresiva")
    else:
        print(numero)
        cuenta_regresiva(numero - 1)
cuenta_regresiva(100)

def num_factorial(numero):
    if numero == 0:
        return 1
    else:
        return numero * num_factorial(numero - 1)
print(num_factorial(5))

def espiral_fibonacci(numero):
    if numero <= 1:
        return 1
    else:
        return espiral_fibonacci(numero - 1) + espiral_fibonacci(numero - 2)
print(espiral_fibonacci(7))