"""
Algoritmo B1 - pandas: crear DataFrame y mostrar estadísticas
"""
import pandas as pd

if __name__ == "__main__":
    data = {
        "Producto": ["Manzana", "Banana", "Tomate", "Lechuga", "Manzana", "Banana"],
        "Precio": [1200, 800, 2500, 1800, 1300, 850],
        "Cantidad": [10, 15, 8, 5, 7, 20]
    }
    df = pd.DataFrame(data)
    print("DataFrame:\n", df)
    print("\nDescripción estadística:\n", df.describe())
