
from pathlib import Path

import joblib

from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report,
)

from preparar_datos import preparar_datos


# Ruta del proyecto
BASE_DIR = Path(__file__).resolve().parent
RUTA_MODELO = BASE_DIR / "modelo" / "modelo_pinturas.joblib"


def evaluar_modelo():
    # 1. Verificar que exista el modelo entrenado
    if not RUTA_MODELO.exists():
        raise FileNotFoundError(
            f"No se encontró el modelo: {RUTA_MODELO}\n"
            "Ejecuta primero entrenar_modelo.py."
        )

    # 2. Cargar el modelo entrenado
    modelo = joblib.load(RUTA_MODELO)

    # 3. Cargar los datos preparados
    X, y, identificadores = preparar_datos()

    # 4. Generar predicciones
    predicciones = modelo.predict(X)

    # 5. Calcular la exactitud
    exactitud = accuracy_score(y, predicciones)

    print("\n===== EVALUACIÓN DEL MODELO =====")
    print(f"Cantidad de ejemplos: {len(X)}")
    print(
        "Tipo de evaluación: datos cargados del CSV; "
        "verifica si también se usaron para entrenar."
    )
    print(f"Exactitud: {exactitud:.2%}")

    # 6. Mostrar la matriz de confusión
    matriz = confusion_matrix(
        y,
        predicciones,
        labels=[0, 1]
    )

    print("\nMatriz de confusión:")
    print(matriz)

    print("\nInterpretación:")
    print("Filas: clases reales [0, 1]")
    print("Columnas: clases predichas [0, 1]")
    print("0 = No recomendable")
    print("1 = Recomendable")

    # 7. Mostrar métricas por clase
    print("\nReporte de clasificación:")

    print(
        classification_report(
            y,
            predicciones,
            labels=[0, 1],
            target_names=[
                "No recomendable",
                "Recomendable"
            ],
            zero_division=0
        )
    )

    # 8. Mostrar cada ejemplo con sus dos identificadores
    print("\n===== DETALLE POR EJEMPLO =====")

    for resultado_id, pintura_id, real, predicho in zip(
        identificadores["resultado_id"],
        identificadores["pintura_id"],
        y,
        predicciones
    ):
        estado = (
            "Correcto"
            if real == predicho
            else "Incorrecto"
        )

        print(
            f"Resultado: {resultado_id} | "
            f"Pintura: {pintura_id} | "
            f"Real: {real} | "
            f"Predicción: {predicho} | "
            f"{estado}"
        )


if __name__ == "__main__":
    evaluar_modelo()

