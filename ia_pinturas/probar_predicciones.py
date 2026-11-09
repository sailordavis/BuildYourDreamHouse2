
from pathlib import Path

import joblib
import pandas as pd


# Rutas del proyecto
BASE_DIR = Path(__file__).resolve().parent
RUTA_MODELO = BASE_DIR / "modelo" / "modelo_pinturas.joblib"

# Variables que recibe el modelo, en el mismo orden del entrenamiento
VARIABLES_ENTRADA = [
    "es_exterior",
    "superficie_es_interior",
    "superficie_coincidencia",
    "eficiencia_coincidencia",
]


def cargar_modelo():
    """Carga el modelo previamente entrenado."""

    if not RUTA_MODELO.exists():
        raise FileNotFoundError(
            f"No se encontró el modelo: {RUTA_MODELO}\n"
            "Ejecuta primero entrenar_modelo.py."
        )

    return joblib.load(RUTA_MODELO)


def crear_casos_prueba():
    """Define combinaciones nuevas para probar el modelo."""

    casos = [
        {
            "caso": 1,
            "descripcion": "Exterior solicitado, pintura de interior",
            "es_exterior": 1,
            "superficie_es_interior": 1,
            "superficie_coincidencia": 1,
            "eficiencia_coincidencia": 1,
            "esperado": 0,
        },
        {
            "caso": 2,
            "descripcion": "Interior, eficiencia coincidente",
            "es_exterior": 0,
            "superficie_es_interior": 1,
            "superficie_coincidencia": -1,
            "eficiencia_coincidencia": 1,
            "esperado": 1,
        },
        {
            "caso": 3,
            "descripcion": "Interior, eficiencia no coincidente",
            "es_exterior": 0,
            "superficie_es_interior": 1,
            "superficie_coincidencia": -1,
            "eficiencia_coincidencia": 0,
            "esperado": 0,
        },
        {
            "caso": 4,
            "descripcion": "Exterior, superficie no coincidente",
            "es_exterior": 1,
            "superficie_es_interior": 0,
            "superficie_coincidencia": 0,
            "eficiencia_coincidencia": 1,
            "esperado": 0,
        },
        {
            "caso": 5,
            "descripcion": "Exterior, ambas coincidencias positivas",
            "es_exterior": 1,
            "superficie_es_interior": 0,
            "superficie_coincidencia": 1,
            "eficiencia_coincidencia": 1,
            "esperado": 1,
        },
        {
            "caso": 6,
            "descripcion": "Interior, superficie positiva pero irrelevante",
            "es_exterior": 0,
            "superficie_es_interior": 1,
            "superficie_coincidencia": 1,
            "eficiencia_coincidencia": 1,
            "esperado": 1,
        },
    ]

    return pd.DataFrame(casos)


def probar_predicciones():
    """Compara las predicciones con los resultados esperados."""

    modelo = cargar_modelo()
    casos = crear_casos_prueba()

    # Solo enviar al modelo las variables utilizadas durante el entrenamiento
    X_prueba = casos[VARIABLES_ENTRADA]

    predicciones = modelo.predict(X_prueba)

    print("\n===== PRUEBAS DE PREDICCIÓN =====")

    correctos = 0

    for i, (_, fila) in enumerate(casos.iterrows()):
        prediccion = int(predicciones[i])
        esperado = int(fila["esperado"])

        coincide = prediccion == esperado

        if coincide:
            correctos += 1

        resultado = "Correcto" if coincide else "Incorrecto"

        print(f"\nCaso {fila['caso']}: {fila['descripcion']}")
        print(f"  Tipo solicitado: {'Exterior' if fila['es_exterior'] == 1 else 'Interior'}")
        print(f"  Pintura apta para: {'Interior' if fila['superficie_es_interior'] == 1 else 'Exterior'}")
        print(f"  Coincidencia de superficie: {fila['superficie_coincidencia']}")
        print(f"  Coincidencia de eficiencia: {fila['eficiencia_coincidencia']}")
        print(f"  Resultado esperado: {esperado}")
        print(f"  Predicción del modelo: {prediccion}")
        print(f"  Evaluación: {resultado}")

    print("\n===== RESUMEN =====")
    print(f"Casos probados: {len(casos)}")
    print(f"Predicciones coincidentes: {correctos}")
    print(f"Predicciones diferentes: {len(casos) - correctos}")
    print(f"Coincidencia con los resultados esperados: {correctos / len(casos):.2%}")


if __name__ == "__main__":
    probar_predicciones()
