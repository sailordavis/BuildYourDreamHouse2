
from pathlib import Path

import joblib
from sklearn.tree import export_text

BASE_DIR = Path(__file__).resolve().parent

RUTA_MODELO = (
    BASE_DIR / "modelo" / "modelo_pinturas.joblib"
)


def inspeccionar_modelo():

    if not RUTA_MODELO.exists():
        raise FileNotFoundError(
            f"No se encontro el modelo: {RUTA_MODELO}"
        )

    modelo = joblib.load(RUTA_MODELO)

    nombres_variables = list(modelo.feature_names_in_)

    print("\n" + "=" * 60)
    print(" REGLAS APRENDIDAS POR EL ARBOL DE DECISION")
    print("=" * 60)

    reglas = export_text(
        modelo,
        feature_names=nombres_variables,
        decimals=2
    )

    print(reglas)

    print("\n" + "=" * 60)
    print(" IMPORTANCIA DE LAS VARIABLES")
    print("=" * 60)

    importancias = sorted(
        zip(
            nombres_variables,
            modelo.feature_importances_
        ),
        key=lambda elemento: elemento[1],
        reverse=True
    )

    for nombre, importancia in importancias:
        print(f"{nombre}: {importancia:.4f}")

    print("\n" + "=" * 60)
    print(" INFORMACION DEL MODELO")
    print("=" * 60)

    print(f"Algoritmo: {type(modelo).__name__}")
    print(f"Profundidad real del arbol: {modelo.get_depth()}")
    print(f"Cantidad de hojas: {modelo.get_n_leaves()}")
    print(f"Profundidad maxima configurada: {modelo.max_depth}")


if __name__ == "__main__":
    inspeccionar_modelo()
