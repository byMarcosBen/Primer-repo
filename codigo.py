def factorial(num):
    resultado = num * factorial(num-1)
    return resultado
factorial(8)