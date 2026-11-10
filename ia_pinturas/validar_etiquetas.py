
from pathlib import Path

import pandas as pd

from preparar_datos import cargar_datos, VARIABLES_ENTRADA


# ============================================================
# 1. CONFIGURACION
# ============================================================

BASE_DIR = Path(__file__).resolve().parent

RUTA_RESULTADOS = BASE_DIR / "resultado_validacion_etiquetas.csv"


# ============================================================
# 2. REGLAS DE NEGOCIO
# ============================================================

def calcular_resultado_esperado(fila):

    es_exterior = fila["es_exterior"]
    superficie_es_interior = fila["superficie_es_interior"]
    superficie_coincidencia = fila["superficie_coincidencia"]
    eficiencia_coincidencia = fila["eficiencia_coincidencia"]

    # Para interiores:
    # la pintura debe ser apta para interior
    # y cumplir con la eficiencia requerida.
    if es_exterior == 0:
        return int(
            superficie_es_interior == 1
            and eficiencia_coincidencia == 1
        )

    # Para exteriores:
    # la pintura debe ser apta para exterior,
    # coincidir con la superficie y cumplir la eficiencia.
    return int(
        superficie_es_interior == 0
        and superficie_coincidencia == 1
        and eficiencia_coincidencia == 1
    )


# ============================================================
# 3. VALIDAR ETIQUETAS
# ============================================================

def validar_etiquetas():

    datos = cargar_datos()

    datos["esperado_segun_reglas"] = datos.apply(
        calcular_resultado_esperado,
        axis=1
    )

    datos["etiqueta_coherente"] = (
        datos["es_recomendable"]
        == datos["esperado_segun_reglas"]
    )

    datos["observacion"] = datos.apply(
        lambda fila: (
            "COHERENTE"
            if fila["etiqueta_coherente"]
            else "REVISAR: la etiqueta contradice las reglas"
        ),
        axis=1
    )

    # Guardar el resultado completo para poder inspeccionarlo.
    datos.to_csv(
        RUTA_RESULTADOS,
        index=False,
        encoding="utf-8-sig"
    )

    coherentes = datos[datos["etiqueta_coherente"]]
    inconsistentes = datos[~datos["etiqueta_coherente"]]

    print("\n" + "=" * 65)
    print(" VALIDACION DE ETIQUETAS DEL ENTRENAMIENTO")
    print("=" * 65)

    print(f"\nRegistros revisados: {len(datos)}")
    print(f"Etiquetas coherentes: {len(coherentes)}")
    print(f"Etiquetas por revisar: {len(inconsistentes)}")

    if len(datos) > 0:
        porcentaje = len(coherentes) / len(datos) * 100
        print(f"Coherencia de etiquetas: {porcentaje:.2f}%")

    if inconsistentes.empty:
        print("\nTodas las etiquetas coinciden con las reglas definidas.")
    else:
        print("\n===== REGISTROS POR REVISAR =====")

        columnas_mostrar = [
            "resultado_id",
            "pintura_id",
            *VARIABLES_ENTRADA,
            "es_recomendable",
            "esperado_segun_reglas",
            "observacion",
        ]

        print(
            inconsistentes[columnas_mostrar].to_string(index=False)
        )

    print(f"\nResultados guardados en: {RUTA_RESULTADOS}")

    print(
        "\nNOTA: esta validacion comprueba las etiquetas frente "
        "a las reglas programadas. Si las reglas de negocio "
        "cambian, tambien debe revisarse esta funcion."
    )


if __name__ == "__main__":
    validar_etiquetas()
