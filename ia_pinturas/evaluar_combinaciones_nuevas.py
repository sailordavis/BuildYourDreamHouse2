
from pathlib import Path

import joblib
import pandas as pd

from preparar_datos import preparar_datos

# ============================================================
# 1. CONFIGURACION
# ============================================================

BASE_DIR = Path(__file__).resolve().parent

RUTA_MODELO = BASE_DIR / "modelo" / "modelo_pinturas.joblib"

VARIABLES_ENTRADA = [
    "es_exterior",
    "superficie_es_interior",
    "superficie_coincidencia",
    "eficiencia_coincidencia",
]

# ============================================================
# 2. CASOS NUEVOS DE EVALUACION
# ============================================================

# Cada caso contiene:
# nombre, es_exterior, superficie_es_interior,
# superficie_coincidencia, eficiencia_coincidencia

CASOS_PRUEBA = [
    {
        "nombre": "Interior con superficie diferente",
        "es_exterior": 0,
        "superficie_es_interior": 1,
        "superficie_coincidencia": 0,
        "eficiencia_coincidencia": 1,
    },
    {
        "nombre": "Interior con coincidencia de superficie",
        "es_exterior": 0,
        "superficie_es_interior": 1,
        "superficie_coincidencia": 1,
        "eficiencia_coincidencia": 1,
    },
    {
        "nombre": "Interior sin eficiencia requerida",
        "es_exterior": 0,
        "superficie_es_interior": 1,
        "superficie_coincidencia": 0,
        "eficiencia_coincidencia": 0,
    },
    {
        "nombre": "Interior sin eficiencia y con coincidencia",
        "es_exterior": 0,
        "superficie_es_interior": 1,
        "superficie_coincidencia": 1,
        "eficiencia_coincidencia": 0,
    },
    {
        "nombre": "Interior solicitado, pintura no apta",
        "es_exterior": 0,
        "superficie_es_interior": 0,
        "superficie_coincidencia": -1,
        "eficiencia_coincidencia": 0,
    },
    {
        "nombre": "Interior solicitado, pintura no apta y sin coincidencia",
        "es_exterior": 0,
        "superficie_es_interior": 0,
        "superficie_coincidencia": 0,
        "eficiencia_coincidencia": 0,
    },
    {
        "nombre": "Exterior sin dato de coincidencia de superficie",
        "es_exterior": 1,
        "superficie_es_interior": 0,
        "superficie_coincidencia": -1,
        "eficiencia_coincidencia": 1,
    },
    {
        "nombre": "Exterior sin eficiencia requerida",
        "es_exterior": 1,
        "superficie_es_interior": 0,
        "superficie_coincidencia": -1,
        "eficiencia_coincidencia": 0,
    },
    {
        "nombre": "Exterior con superficie diferente y sin eficiencia",
        "es_exterior": 1,
        "superficie_es_interior": 0,
        "superficie_coincidencia": 0,
        "eficiencia_coincidencia": 0,
    },
    {
        "nombre": "Exterior solicitado, pintura no apta",
        "es_exterior": 1,
        "superficie_es_interior": 1,
        "superficie_coincidencia": 0,
        "eficiencia_coincidencia": 0,
    },
    {
        "nombre": "Exterior solicitado, pintura no apta aunque coincide la superficie",
        "es_exterior": 1,
        "superficie_es_interior": 1,
        "superficie_coincidencia": 1,
        "eficiencia_coincidencia": 1,
    },
    {
        "nombre": "Exterior apto, superficie coincide, eficiencia insuficiente",
        "es_exterior": 1,
        "superficie_es_interior": 0,
        "superficie_coincidencia": 1,
        "eficiencia_coincidencia": 0,
    },
]

# ============================================================
# 3. REGLAS DE NEGOCIO PARA EL RESULTADO ESPERADO
# ============================================================

def calcular_resultado_esperado(caso):

    es_exterior = caso["es_exterior"]
    es_interior = caso["superficie_es_interior"]
    coincidencia = caso["superficie_coincidencia"]
    eficiencia = caso["eficiencia_coincidencia"]

    # Caso A: se solicita pintura para interiores.
    if es_exterior == 0:
        return int(es_interior == 1 and eficiencia == 1)

    # Caso B: se solicita pintura para exteriores.
    return int(
        es_interior == 0
        and coincidencia == 1
        and eficiencia == 1
    )

# ============================================================
# 4. EVALUAR LAS COMBINACIONES
# ============================================================

def evaluar_combinaciones_nuevas():

    if not RUTA_MODELO.exists():
        raise FileNotFoundError(
            f"No se encontro el modelo: {RUTA_MODELO}"
        )

    # Recuperar las variables usadas en el CSV original.
    X_entrenamiento, _, _ = preparar_datos()

    # Crear un conjunto de las combinaciones ya utilizadas.
    combinaciones_entrenamiento = {
        tuple(fila)
        for fila in X_entrenamiento.to_numpy()
    }

    # Cargar el modelo existente sin volver a entrenarlo.
    modelo = joblib.load(RUTA_MODELO)

    resultados = []
    combinaciones_vistas = set()

    print("\n" + "=" * 65)
    print(" EVALUACION DE COMBINACIONES NUEVAS")
    print("=" * 65)

    for caso in CASOS_PRUEBA:

        vector = tuple(
            caso[columna]
            for columna in VARIABLES_ENTRADA
        )

        # No evaluar vectores presentes en el entrenamiento
        # ni repetir combinaciones dentro de esta misma prueba.
        if vector in combinaciones_entrenamiento:
            print(
                f"\nOMITIDO: {caso['nombre']}"
                "\nMotivo: la combinacion ya existe "
                "en los datos de entrenamiento."
            )
            continue

        if vector in combinaciones_vistas:
            print(
                f"\nOMITIDO: {caso['nombre']}"
                "\nMotivo: combinacion repetida en esta prueba."
            )
            continue

        combinaciones_vistas.add(vector)

        entrada = pd.DataFrame(
            [caso],
            columns=VARIABLES_ENTRADA
        )

        prediccion = int(modelo.predict(entrada)[0])

        esperado = calcular_resultado_esperado(caso)

        correcto = prediccion == esperado

        estado = "CORRECTO" if correcto else "DIFERENCIA"

        resultados.append({
            "caso": caso["nombre"],
            "es_exterior": caso["es_exterior"],
            "superficie_es_interior": caso["superficie_es_interior"],
            "superficie_coincidencia": caso["superficie_coincidencia"],
            "eficiencia_coincidencia": caso["eficiencia_coincidencia"],
            "esperado": esperado,
            "prediccion": prediccion,
            "correcto": correcto,
        })

        print(f"\nCaso: {caso['nombre']}")
        print(f"Vector: {list(vector)}")
        print(f"Resultado esperado: {esperado}")
        print(f"Prediccion del modelo: {prediccion}")
        print(f"Evaluacion: {estado}")

    # ========================================================
    # 5. RESUMEN Y ARCHIVO DE RESULTADOS
    # ========================================================

    print("\n" + "=" * 65)
    print(" RESUMEN FINAL")
    print("=" * 65)

    if not resultados:
        print(
            "No se evaluaron casos nuevos. "
            "Revisa las combinaciones de prueba."
        )
        return

    df_resultados = pd.DataFrame(resultados)

    total = len(df_resultados)
    aciertos = int(df_resultados["correcto"].sum())
    diferencias = total - aciertos

    print(f"Combinaciones nuevas evaluadas: {total}")
    print(f"Coincidencias con las reglas: {aciertos}")
    print(f"Diferencias: {diferencias}")
    print(f"Porcentaje de coincidencia: {aciertos / total:.2%}")

    ruta_salida = (
        BASE_DIR / "resultados_combinaciones_nuevas.csv"
    )

    df_resultados.to_csv(
        ruta_salida,
        index=False,
        encoding="utf-8-sig"
    )

    print(f"\nResultados guardados en: {ruta_salida}")

    print(
        "\nIMPORTANTE: esta prueba comprueba si el modelo "
        "coincide con las reglas de negocio en combinaciones "
        "nuevas. No demuestra por si sola una generalizacion "
        "amplia a datos reales."
    )

if __name__ == "__main__":
    evaluar_combinaciones_nuevas()