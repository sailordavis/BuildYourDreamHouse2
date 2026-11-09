
from pathlib import Path

import pandas as pd


# Rutas del proyecto
BASE_DIR = Path(__file__).resolve().parent
RUTA_DATOS = BASE_DIR / "datos" / "lote_01_basico_entrenamiento.csv"

# Columnas que describen las características de cada pintura
VARIABLES_ENTRADA = [
    "es_exterior",
    "superficie_es_interior",
    "superficie_coincidencia",
    "eficiencia_coincidencia",
]

# Columna que el modelo aprenderá a predecir
VARIABLE_OBJETIVO = "es_recomendable"

# Identificadores: sirven para rastrear los ejemplos,
# pero no se utilizarán como características del modelo.
COLUMNAS_ID = ["resultado_id", "pintura_id"]


def cargar_datos():
    """Carga el conjunto de datos desde el archivo CSV."""

    if not RUTA_DATOS.exists():
        raise FileNotFoundError(
            f"No se encontró el archivo: {RUTA_DATOS}"
        )

    datos = pd.read_csv(RUTA_DATOS)

    columnas_requeridas = (
        COLUMNAS_ID
        + VARIABLES_ENTRADA
        + [VARIABLE_OBJETIVO]
    )

    faltantes = [
        columna
        for columna in columnas_requeridas
        if columna not in datos.columns
    ]

    if faltantes:
        raise ValueError(
            f"Faltan columnas obligatorias: {faltantes}"
        )

    if datos[columnas_requeridas].isnull().any().any():
        raise ValueError(
            "Hay valores vacíos en las columnas requeridas."
        )

    return datos


def validar_datos(datos):
    """Comprueba que los valores tengan el formato esperado."""

    columnas_binarias = [
        "es_exterior",
        "superficie_es_interior",
        "superficie_coincidencia",
        "eficiencia_coincidencia",
        VARIABLE_OBJETIVO,
    ]

    for columna in columnas_binarias:
        valores = set(datos[columna].unique())

        if columna == VARIABLE_OBJETIVO:
            permitidos = {0, 1}
        elif columna in [
            "superficie_coincidencia",
            "eficiencia_coincidencia",
        ]:
            permitidos = {-1, 0, 1}
        else:
            permitidos = {0, 1}

        if not valores.issubset(permitidos):
            raise ValueError(
                f"Valores inválidos en '{columna}': {valores}"
            )

    if not datos[VARIABLE_OBJETIVO].isin([0, 1]).all():
        raise ValueError("La etiqueta debe ser 0 o 1.")

    print("Validación de datos completada.")


def preparar_datos():
    """Devuelve las entradas X, las etiquetas y y los IDs."""

    datos = cargar_datos()
    validar_datos(datos)

    X = datos[VARIABLES_ENTRADA].copy()
    y = datos[VARIABLE_OBJETIVO].copy()

    # Los IDs se conservan aparte para rastrear los registros.
    identificadores = datos[COLUMNAS_ID].copy()

    print(f"Cantidad de ejemplos: {len(datos)}")
    print(f"Variables de entrada: {VARIABLES_ENTRADA}")
    print(f"Distribución de etiquetas:\n{y.value_counts().sort_index()}")

    return X, y, identificadores


if __name__ == "__main__":
    X, y, identificadores = preparar_datos()

    print("\nPrimeras entradas (X):")
    print(X.head())

    print("\nPrimeras etiquetas (y):")
    print(y.head())

    print("\nIdentificadores:")
    print(identificadores.head())
