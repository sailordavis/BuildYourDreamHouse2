
from pathlib import Path
from itertools import product

import joblib
import pandas as pd

from preparar_datos import preparar_datos


# ============================================================
# 1. CONFIGURACION
# ============================================================

BASE_DIR = Path(__file__).resolve().parent

RUTA_MODELO = (
    BASE_DIR / "modelo" / "modelo_pinturas.joblib"
)

RUTA_RESULTADOS = (
    BASE_DIR / "resultados_todas_combinaciones.csv"
)

VARIABLES_ENTRADA = [
    "es_exterior",
    "superficie_es_interior",
    "superficie_coincidencia",
    "eficiencia_coincidencia",
]


# ============================================================
# 2. DEFINIR LOS VALORES POSIBLES DE CADA VARIABLE
# ============================================================

VALORES_POSIBLES = {
    "es_exterior": [0, 1],
    "superficie_es_interior": [0, 1],
    "superficie_coincidencia": [-1, 0, 1],
    "eficiencia_coincidencia": [0, 1],
}


# ============================================================
# 3. CALCULAR EL RESULTADO ESPERADO SEGUN LAS REGLAS
# ============================================================

def calcular_resultado_esperado(caso):

    es_exterior = caso["es_exterior"]
    es_interior = caso["superficie_es_interior"]
    coincidencia = caso["superficie_coincidencia"]
    eficiencia = caso["eficiencia_coincidencia"]

    # Si se solicita pintura para interiores:
    # debe ser apta para interior y cumplir la eficiencia.
    if es_exterior == 0:
        return int(
            es_interior == 1
            and eficiencia == 1
        )

    # Si se solicita pintura para exteriores:
    # debe ser apta para exterior y coincidir
    # tanto la superficie como la eficiencia.
    return int(
        es_interior == 0
        and coincidencia == 1
        and eficiencia == 1
    )


# ============================================================
# 4. GENERAR TODAS LAS COMBINACIONES
# ============================================================

def generar_combinaciones():

    valores = [
        VALORES_POSIBLES[columna]
        for columna in VARIABLES_ENTRADA
    ]

    combinaciones = list(product(*valores))

    datos = pd.DataFrame(
        combinaciones,
        columns=VARIABLES_ENTRADA
    )

    return datos


# ============================================================
# 5. EVALUAR TODAS LAS COMBINACIONES
# ============================================================

def evaluar_todas_combinaciones():

    if not RUTA_MODELO.exists():
        raise FileNotFoundError(
            f"No se encontro el modelo: {RUTA_MODELO}"
        )

    # Cargar y validar los datos originales.
    X_entrenamiento, _, _ = preparar_datos()

    # Registrar los vectores que aparecen en entrenamiento.
    combinaciones_entrenamiento = {
        tuple(int(valor) for valor in fila)
        for fila in X_entrenamiento.to_numpy()
    }

    # Cargar el modelo ya entrenado.
    modelo = joblib.load(RUTA_MODELO)

    # Generar las 24 combinaciones.
    datos_prueba = generar_combinaciones()

    # Obtener las predicciones del modelo.
    predicciones = modelo.predict(datos_prueba)

    # Calcular los resultados esperados.
    esperados = [
        calcular_resultado_esperado(caso)
        for caso in datos_prueba.to_dict(orient="records")
    ]

    resultados = datos_prueba.copy()

    resultados["esperado"] = esperados
    resultados["prediccion"] = predicciones.astype(int)

    resultados["correcto"] = (
        resultados["esperado"]
        == resultados["prediccion"]
    )

    # Identificar si cada combinación ya se utilizó
    # en el CSV de entrenamiento.
    resultados["presente_en_entrenamiento"] = [
        tuple(int(valor) for valor in fila)
        in combinaciones_entrenamiento
        for fila in datos_prueba.to_numpy()
    ]

    resultados["tipo_evaluacion"] = resultados[
        "presente_en_entrenamiento"
    ].map({
        True: "Combinacion conocida",
        False: "Combinacion no vista",
    })

    # Guardar todos los resultados.
    resultados.to_csv(
        RUTA_RESULTADOS,
        index=False,
        encoding="utf-8-sig"
    )

    # ========================================================
    # 6. MOSTRAR RESULTADOS
    # ========================================================

    conocidas = resultados[
        resultados["presente_en_entrenamiento"]
    ]

    nuevas = resultados[
        ~resultados["presente_en_entrenamiento"]
    ]

    correctas = int(resultados["correcto"].sum())
    diferencias = len(resultados) - correctas

    print("\n" + "=" * 65)
    print(" EVALUACION EXHAUSTIVA DE COMBINACIONES")
    print("=" * 65)

    print(f"\nTotal de combinaciones: {len(resultados)}")
    print(f"Combinaciones conocidas: {len(conocidas)}")
    print(f"Combinaciones no vistas: {len(nuevas)}")

    print("\n===== RESULTADO GENERAL =====")
    print(f"Coincidencias con las reglas: {correctas}")
    print(f"Diferencias: {diferencias}")
    print(f"Porcentaje de coincidencia: {correctas / len(resultados):.2%}")

    if len(nuevas) > 0:
        correctas_nuevas = int(nuevas["correcto"].sum())
        diferencias_nuevas = len(nuevas) - correctas_nuevas

        print("\n===== COMBINACIONES NO VISTAS =====")
        print(f"Evaluadas: {len(nuevas)}")
        print(f"Coincidencias: {correctas_nuevas}")
        print(f"Diferencias: {diferencias_nuevas}")
        print(
            "Porcentaje de coincidencia: "
            f"{correctas_nuevas / len(nuevas):.2%}"
        )

    print("\n===== DETALLE DE LAS 24 COMBINACIONES =====")

    for _, fila in resultados.iterrows():

        estado = (
            "CORRECTO"
            if fila["correcto"]
            else "DIFERENCIA"
        )

        origen = fila["tipo_evaluacion"]

        vector = [
            int(fila[columna])
            for columna in VARIABLES_ENTRADA
        ]

        print(
            f"\nVector: {vector}"
            f"\n  Esperado: {int(fila['esperado'])}"
            f"\n  Prediccion: {int(fila['prediccion'])}"
            f"\n  Estado: {estado}"
            f"\n  Datos: {origen}"
        )

    # Mostrar las combinaciones donde el modelo difiere.
    errores = resultados[~resultados["correcto"]]

    if not errores.empty:
        print("\n===== COMBINACIONES CON DIFERENCIAS =====")
        print(
            errores[
                VARIABLES_ENTRADA
                + ["esperado", "prediccion", "tipo_evaluacion"]
            ].to_string(index=False)
        )
    else:
        print(
            "\nNo se encontraron diferencias entre las "
            "predicciones y las reglas definidas."
        )

    print(f"\nArchivo generado: {RUTA_RESULTADOS}")

    print(
        "\nNOTA: esta evaluacion compara el modelo con reglas "
        "definidas manualmente. No garantiza que las reglas "
        "representen todos los casos reales."
    )


# ============================================================
# 7. PUNTO DE ENTRADA
# ============================================================

if __name__ == "__main__":
    evaluar_todas_combinaciones()
