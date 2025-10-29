"""
Algoritmo B2 - pandas: agrupamiento y filtrado
"""
import pandas as pd

if __name__ == "__main__":
    df = pd.DataFrame({
        "Categoria": ["Fruta", "Fruta", "Verdura", "Verdura", "Fruta", "Fruta"],
        "Precio": [1200, 800, 2500, 1800, 1300, 850],
        "Cantidad": [10, 15, 8, 5, 7, 20]
    })

    filtrado = df[df["Precio"] > 1000]

    agrup = df.groupby("Categoria").agg({"Cantidad": "sum", "Precio": "mean"})
    print("\nAgrupamiento por Categoria:\n", agrup)
