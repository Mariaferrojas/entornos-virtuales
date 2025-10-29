""" 
Algoritmo A - Fibonacci y medición de tiempo
"""
import time

def fibonacci(n):
    a, b = 0, 1
    seq = []
    for _ in range(n):
        seq.append(a)
        a, b = b, a + b
    return seq

if __name__ == "__main__":
    n = 20
    t0 = time.perf_counter()
    seq = fibonacci(n)
    t1 = time.perf_counter()
    print(f"Fibonacci({n}): {seq}")
    print(f"Tiempo de ejecución: {t1 - t0:.6f} segundos")
