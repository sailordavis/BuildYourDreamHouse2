
from pathlib import Path

import pandas as pd

from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report,
)

from preparar_datos import preparar_datos


# ============================================================
# 1. CONFIGURACION
# ============================================================

BASE_DIR = Path(__file__).resolve().parent

VARIABLES_ENTRADA = [
    "es_exterior",
    "superficie_es_interior",
    "superficie_coincidencia",
    "eficiencia_coincidencia",
]

VARIABLE_OBJETIVO = "es_recomendable"

# Debe coincidir con la configuracion de entrenamiento.
PROFUNDIDAD_MAXIMA = 4

# Porcentaje reservado para evaluar.
PORCENTAJE_PRUEBA = 0.25

# Permite repetir la misma division de datos.
SEMILLA = 42


# ============================================================
# 2. PREPARAR Y DIVIDIR LOS DATOS
# ============================================================

def dividir_datos():

    # Cargar y validar el CSV mediante tu modulo existente.
    X, y, identificadores = preparar_datos()

    # Reservar ejemplos que no se usaran para entrenar
    # esta instancia del modelo.
    X_entrenamiento, X_prueba, y_entrenamiento, y_prueba, indices_entrenamiento, indices_prueba = (
        train_test_split(
            X,
            y,
            identificadores.index,
            test_size=PORCENTAJE_PRUEBA,
            random_state=SEMILLA,
            stratify=y,
        )
    )

    ids_entrenamiento = identificadores.loc[
        indices_entrenamiento
    ].reset_index(drop=True)

    ids_prueba = identificadores.loc[
        indices_prueba
    ].reset_index(drop=True)

    print("\n===== DIVISION DE LOS DATOS =====")
    print(f"Ejemplos originales: {len(X)}")
    print(f"Ejemplos para entrenamiento: {len(X_entrenamiento)}")
    print(f"Ejemplos para evaluacion: {len(X_prueba)}")

    print("\nDistribucion de etiquetas en entrenamiento:")
    print(y_entrenamiento.value_counts().sort_index())

    print("\nDistribucion de etiquetas en evaluacion:")
    print(y_prueba.value_counts().sort_index())

    return (
        X_entrenamiento,
        X_prueba,
        y_entrenamiento,
        y_prueba,
        ids_entrenamiento,
        ids_prueba,
    )


# ============================================================
# 3. ENTRENAR UNA INSTANCIA INDEPENDIENTE
# ============================================================

def entrenar_modelo_temporal(X_entrenamiento, y_entrenamiento):

    modelo = DecisionTreeClassifier(
        max_depth=PROFUNDIDAD_MAXIMA,
        random_state=SEMILLA,
    )

    modelo.fit(X_entrenamiento, y_entrenamiento)

    print("\nModelo temporal entrenado.")
    print("No se modifico el archivo modelo_pinturas.joblib.")

    return modelo


# ============================================================
# 4. EVALUAR CON EJEMPLOS RESERVADOS
# ============================================================

def evaluar_modelo_independiente():

    (
        X_entrenamiento,
        X_prueba,
        y_entrenamiento,
        y_prueba,
        ids_entrenamiento,
        ids_prueba,
    ) = dividir_datos()

    modelo = entrenar_modelo_temporal(
        X_entrenamiento,
        y_entrenamiento,
    )

    # Predecir unicamente los ejemplos reservados.
    predicciones = modelo.predict(X_prueba)

    exactitud = accuracy_score(
        y_prueba,
        predicciones,
    )

    matriz = confusion_matrix(
        y_prueba,
        predicciones,
        labels=[0, 1],
    )

    print("\n" + "=" * 60)
    print("       EVALUACION INDEPENDIENTE DEL MODELO")
    print("=" * 60)

    print(f"\nExactitud: {exactitud:.2%}")

    print("\nMatriz de confusion:")
    print("Filas = valor real; columnas = prediccion")
    print("Orden de clases: 0 = No recomendable, 1 = Recomendable")
    print(matriz)

    print("\nInforme de clasificacion:")
    print(
        classification_report(
            y_prueba,
            predicciones,
            labels=[0, 1],
            target_names=[
                "No recomendable",
                "Recomendable",
            ],
            zero_division=0,
        )
    )

    # --------------------------------------------------------
    # 5. DETALLE DE CADA EJEMPLO RESERVADO
    # --------------------------------------------------------

    resultados = X_prueba.reset_index(drop=True).copy()

    resultados.insert(
        0,
        "resultado_id",
        ids_prueba["resultado_id"].to_numpy(),
    )

    resultados.insert(
        1,
        "pintura_id",
        ids_prueba["pintura_id"].to_numpy(),
    )

    resultados["valor_real"] = y_prueba.to_numpy()
    resultados["prediccion"] = predicciones
    resultados["correcto"] = (
        resultados["valor_real"] == resultados["prediccion"]
    )

    print("\n===== DETALLE DE PREDICCIONES =====")

    for _, fila in resultados.iterrows():

        estado = "CORRECTO" if fila["correcto"] else "FALLO"

        print(
            f"\nResultado ID: {fila['resultado_id']} | "
            f"Pintura ID: {fila['pintura_id']}"
        )

        print(
            "  Vector: "
            f"{[fila[columna] for columna in VARIABLES_ENTRADA]}"
        )

        print(f"  Valor real: {fila['valor_real']}")
        print(f"  Prediccion: {fila['prediccion']}")
        print(f"  Evaluacion: {estado}")

    # --------------------------------------------------------
    # 6. GUARDAR LOS RESULTADOS
    # --------------------------------------------------------

    ruta_resultados = (
        BASE_DIR / "resultados_evaluacion_independiente.csv"
    )

    resultados.to_csv(
        ruta_resultados,
        index=False,
        encoding="utf-8-sig",
    )

    print("\n===== RESUMEN =====")
    print(f"Ejemplos evaluados: {len(resultados)}")
    print(f"Predicciones correctas: {int(resultados['correcto'].sum())}")
    print(f"Predicciones incorrectas: {int((~resultados['correcto']).sum())}")
    print(f"Resultados guardados en: {ruta_resultados}")

    print(
        "\nIMPORTANTE: la evaluacion utiliza una division aleatoria "
        "de los datos disponibles. Con pocos ejemplos, la metrica "
        "puede variar mucho entre divisiones."
    )


# ============================================================
# 7. PUNTO DE ENTRADA
# ============================================================

if __name__ == "__main__":
    evaluar_modelo_independiente()
