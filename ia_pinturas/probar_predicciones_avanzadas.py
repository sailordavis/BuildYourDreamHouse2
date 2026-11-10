
from pathlib import Path

import joblib
import pandas as pd


# ============================================================
# 1. CONFIGURACIÓN
# ============================================================

BASE_DIR = Path(__file__).resolve().parent

RUTA_MODELO = (
    BASE_DIR / "modelo" / "modelo_pinturas.joblib"
)

VARIABLES_ENTRADA = [
    "es_exterior",
    "superficie_es_interior",
    "superficie_coincidencia",
    "eficiencia_coincidencia",
]


# ============================================================
# 2. CARGAR EL MODELO ENTRENADO
# ============================================================

def cargar_modelo():
    if not RUTA_MODELO.exists():
        raise FileNotFoundError(
            f"No se encontró el modelo: {RUTA_MODELO}\n"
            "Ejecuta primero entrenar_modelo.py."
        )

    modelo = joblib.load(RUTA_MODELO)

    print("Modelo cargado correctamente.")
    print(f"Archivo: {RUTA_MODELO}")

    return modelo


# ============================================================
# 3. CREAR CASOS DE PRUEBA
# ============================================================

def crear_casos_prueba():

    casos = [

        # ----------------------------------------------------
        # A. CASOS NORMALES
        # ----------------------------------------------------

        {
            "caso": 1,
            "categoria": "Normal",
            "descripcion": "Exterior: todas las condiciones coinciden",
            "es_exterior": 1,
            "superficie_es_interior": 0,
            "superficie_coincidencia": 1,
            "eficiencia_coincidencia": 1,
            "esperado": 1,
        },
        {
            "caso": 2,
            "categoria": "Normal",
            "descripcion": "Interior: eficiencia coincidente",
            "es_exterior": 0,
            "superficie_es_interior": 1,
            "superficie_coincidencia": -1,
            "eficiencia_coincidencia": 1,
            "esperado": 1,
        },
        {
            "caso": 3,
            "categoria": "Normal",
            "descripcion": "Interior: eficiencia no coincidente",
            "es_exterior": 0,
            "superficie_es_interior": 1,
            "superficie_coincidencia": -1,
            "eficiencia_coincidencia": 0,
            "esperado": 0,
        },
        {
            "caso": 4,
            "categoria": "Normal",
            "descripcion": "Exterior: superficie no coincidente",
            "es_exterior": 1,
            "superficie_es_interior": 0,
            "superficie_coincidencia": 0,
            "eficiencia_coincidencia": 1,
            "esperado": 0,
        },

        # ----------------------------------------------------
        # B. CONTRADICCIONES ENTRE TIPO Y USO SOLICITADO
        # ----------------------------------------------------

        {
            "caso": 5,
            "categoria": "Contradiccion",
            "descripcion": "Pintura interior para exterior con coincidencias positivas",
            "es_exterior": 1,
            "superficie_es_interior": 1,
            "superficie_coincidencia": 1,
            "eficiencia_coincidencia": 1,
            "esperado": 0,
        },
        {
            "caso": 6,
            "categoria": "Contradiccion",
            "descripcion": "Pintura exterior para interior con eficiencia positiva",
            "es_exterior": 0,
            "superficie_es_interior": 0,
            "superficie_coincidencia": -1,
            "eficiencia_coincidencia": 1,
            "esperado": 0,
        },
        {
            "caso": 7,
            "categoria": "Contradiccion",
            "descripcion": "Pintura interior para exterior con coincidencias negativas",
            "es_exterior": 1,
            "superficie_es_interior": 1,
            "superficie_coincidencia": 0,
            "eficiencia_coincidencia": 0,
            "esperado": 0,
        },

        # ----------------------------------------------------
        # C. CASOS LIMITE
        # ----------------------------------------------------

        {
            "caso": 8,
            "categoria": "Limite",
            "descripcion": "Exterior: superficie coincide, eficiencia no",
            "es_exterior": 1,
            "superficie_es_interior": 0,
            "superficie_coincidencia": 1,
            "eficiencia_coincidencia": 0,
            "esperado": 0,
        },
        {
            "caso": 9,
            "categoria": "Limite",
            "descripcion": "Exterior: eficiencia coincide, superficie no",
            "es_exterior": 1,
            "superficie_es_interior": 0,
            "superficie_coincidencia": 0,
            "eficiencia_coincidencia": 1,
            "esperado": 0,
        },
        {
            "caso": 10,
            "categoria": "Limite",
            "descripcion": "Interior: superficie coincide, eficiencia no",
            "es_exterior": 0,
            "superficie_es_interior": 1,
            "superficie_coincidencia": 1,
            "eficiencia_coincidencia": 0,
            "esperado": 0,
        },
        {
            "caso": 11,
            "categoria": "Limite",
            "descripcion": "Exterior: ninguna coincidencia positiva",
            "es_exterior": 1,
            "superficie_es_interior": 0,
            "superficie_coincidencia": 0,
            "eficiencia_coincidencia": 0,
            "esperado": 0,
        },

        # ----------------------------------------------------
        # D. VALORES -1 Y DATOS NO APLICABLES
        # ----------------------------------------------------

        {
            "caso": 12,
            "categoria": "Valor especial",
            "descripcion": "Interior: superficie no evaluada y eficiencia positiva",
            "es_exterior": 0,
            "superficie_es_interior": 1,
            "superficie_coincidencia": -1,
            "eficiencia_coincidencia": 1,
            "esperado": 1,
        },
        {
            "caso": 13,
            "categoria": "Valor especial",
            "descripcion": "Interior: superficie no evaluada y eficiencia negativa",
            "es_exterior": 0,
            "superficie_es_interior": 1,
            "superficie_coincidencia": -1,
            "eficiencia_coincidencia": 0,
            "esperado": 0,
        },
        {
            "caso": 14,
            "categoria": "Valor especial",
            "descripcion": "Exterior: superficie no evaluada y eficiencia positiva",
            "es_exterior": 1,
            "superficie_es_interior": 0,
            "superficie_coincidencia": -1,
            "eficiencia_coincidencia": 1,
            "esperado": 0,
        },
        {
            "caso": 15,
            "categoria": "Valor especial",
            "descripcion": "Exterior: superficie no evaluada y eficiencia negativa",
            "es_exterior": 1,
            "superficie_es_interior": 0,
            "superficie_coincidencia": -1,
            "eficiencia_coincidencia": 0,
            "esperado": 0,
        },

        # ----------------------------------------------------
        # E. COMBINACIONES INUSUALES
        # ----------------------------------------------------

        {
            "caso": 16,
            "categoria": "Inusual",
            "descripcion": "Interior: superficie positiva aunque no deberia evaluarse",
            "es_exterior": 0,
            "superficie_es_interior": 1,
            "superficie_coincidencia": 1,
            "eficiencia_coincidencia": 1,
            "esperado": 1,
        },
        {
            "caso": 17,
            "categoria": "Inusual",
            "descripcion": "Interior: superficie negativa aunque no deberia evaluarse",
            "es_exterior": 0,
            "superficie_es_interior": 1,
            "superficie_coincidencia": 0,
            "eficiencia_coincidencia": 1,
            "esperado": 1,
        },
        {
            "caso": 18,
            "categoria": "Inusual",
            "descripcion": "Exterior: ambas coincidencias negativas, pintura apta",
            "es_exterior": 1,
            "superficie_es_interior": 0,
            "superficie_coincidencia": 0,
            "eficiencia_coincidencia": 0,
            "esperado": 0,
        },
        {
            "caso": 19,
            "categoria": "Inusual",
            "descripcion": "Interior: todas las coincidencias favorables pero pintura exterior",
            "es_exterior": 0,
            "superficie_es_interior": 0,
            "superficie_coincidencia": 1,
            "eficiencia_coincidencia": 1,
            "esperado": 0,
        },
        {
            "caso": 20,
            "categoria": "Inusual",
            "descripcion": "Exterior: coincidencias positivas pero pintura interior",
            "es_exterior": 1,
            "superficie_es_interior": 1,
            "superficie_coincidencia": 1,
            "eficiencia_coincidencia": 1,
            "esperado": 0,
        },

        # ----------------------------------------------------
        # F. PRUEBAS DE INVARIANCIA
        # La recomendacion interior no deberia cambiar cuando
        # solamente cambia la coincidencia de superficie.
        # ----------------------------------------------------

        {
            "caso": 21,
            "categoria": "Invariancia",
            "descripcion": "Interior: superficie -1, eficiencia positiva",
            "es_exterior": 0,
            "superficie_es_interior": 1,
            "superficie_coincidencia": -1,
            "eficiencia_coincidencia": 1,
            "esperado": 1,
        },
        {
            "caso": 22,
            "categoria": "Invariancia",
            "descripcion": "Interior: superficie 0, eficiencia positiva",
            "es_exterior": 0,
            "superficie_es_interior": 1,
            "superficie_coincidencia": 0,
            "eficiencia_coincidencia": 1,
            "esperado": 1,
        },
        {
            "caso": 23,
            "categoria": "Invariancia",
            "descripcion": "Interior: superficie 1, eficiencia positiva",
            "es_exterior": 0,
            "superficie_es_interior": 1,
            "superficie_coincidencia": 1,
            "eficiencia_coincidencia": 1,
            "esperado": 1,
        },

        # ----------------------------------------------------
        # G. COMBINACIONES POCO REPRESENTADAS
        # ----------------------------------------------------

        {
            "caso": 24,
            "categoria": "Poco representado",
            "descripcion": "Exterior: superficie positiva y eficiencia no evaluada",
            "es_exterior": 1,
            "superficie_es_interior": 0,
            "superficie_coincidencia": 1,
            "eficiencia_coincidencia": -1,
            "esperado": 0,
        },
        {
            "caso": 25,
            "categoria": "Poco representado",
            "descripcion": "Interior: pintura apta y ambas coincidencias negativas",
            "es_exterior": 0,
            "superficie_es_interior": 1,
            "superficie_coincidencia": 0,
            "eficiencia_coincidencia": 0,
            "esperado": 0,
        },
    ]

    return pd.DataFrame(casos)


# ============================================================
# 4. EJECUTAR LAS PRUEBAS
# ============================================================

def probar_predicciones_avanzadas():

    modelo = cargar_modelo()
    casos = crear_casos_prueba()

    # Solo las variables que el modelo utiliza como entrada.
    X_prueba = casos[VARIABLES_ENTRADA]

    # Generar predicciones con el modelo ya entrenado.
    predicciones = modelo.predict(X_prueba)

    casos["prediccion"] = predicciones.astype(int)

    casos["correcto"] = (
        casos["prediccion"] == casos["esperado"]
    )

    print("\n" + "=" * 65)
    print("       PRUEBAS AVANZADAS DEL MODELO DE PINTURAS")
    print("=" * 65)

    for _, fila in casos.iterrows():

        estado = "CORRECTO" if fila["correcto"] else "FALLO"

        tipo = (
            "Exterior"
            if fila["es_exterior"] == 1
            else "Interior"
        )

        uso_pintura = (
            "Interior"
            if fila["superficie_es_interior"] == 1
            else "Exterior"
        )

        print(f"\nCaso {fila['caso']} [{fila['categoria']}]")
        print(f"  Escenario: {fila['descripcion']}")
        print(f"  Solicitud: {tipo}")
        print(f"  Pintura apta para: {uso_pintura}")
        print(
            "  Coincidencia superficie: "
            f"{fila['superficie_coincidencia']}"
        )
        print(
            "  Coincidencia eficiencia: "
            f"{fila['eficiencia_coincidencia']}"
        )
        print(f"  Resultado esperado: {fila['esperado']}")
        print(f"  Prediccion del modelo: {fila['prediccion']}")
        print(f"  Evaluacion: {estado}")

    # --------------------------------------------------------
    # RESUMEN GENERAL
    # --------------------------------------------------------

    total = len(casos)
    correctos = int(casos["correcto"].sum())
    fallidos = total - correctos
    porcentaje = correctos / total * 100

    print("\n" + "=" * 65)
    print("                  RESUMEN GENERAL")
    print("=" * 65)

    print(f"Casos probados: {total}")
    print(f"Predicciones coincidentes: {correctos}")
    print(f"Predicciones diferentes: {fallidos}")
    print(f"Coincidencia con los resultados esperados: {porcentaje:.2f}%")

    # --------------------------------------------------------
    # RESUMEN POR CATEGORIA
    # --------------------------------------------------------

    print("\n===== RESULTADOS POR CATEGORIA =====")

    resumen = casos.groupby("categoria").agg(
        total=("correcto", "size"),
        correctos=("correcto", "sum"),
    )

    resumen["fallidos"] = resumen["total"] - resumen["correctos"]

    resumen["coincidencia_pct"] = (
        resumen["correctos"] / resumen["total"] * 100
    ).round(2)

    print(resumen.to_string())

    # --------------------------------------------------------
    # MOSTRAR CASOS QUE NECESITAN REVISION
    # --------------------------------------------------------

    fallos = casos[~casos["correcto"]]

    if not fallos.empty:
        print("\n===== CASOS QUE NECESITAN REVISION =====")

        for _, fila in fallos.iterrows():
            print(
                f"Caso {fila['caso']}: {fila['descripcion']}"
            )
            print(
                f"  Esperado: {fila['esperado']} | "
                f"Prediccion: {fila['prediccion']}"
            )
    else:
        print("\nTodas las predicciones coincidieron con lo esperado.")

    # --------------------------------------------------------
    # COMPROBAR INVARIANCIA PARA INTERIORES
    # --------------------------------------------------------

    invariancia = casos[
        casos["categoria"] == "Invariancia"
    ]

    predicciones_invariancia = invariancia["prediccion"].tolist()

    print("\n===== PRUEBA DE INVARIANCIA =====")

    if len(set(predicciones_invariancia)) == 1:
        print(
            "El modelo produjo la misma prediccion en los tres "
            "casos de interior."
        )
    else:
        print(
            "ATENCION: la prediccion cambia cuando solo cambia "
            "la coincidencia de superficie."
        )
        print(
            "Predicciones obtenidas: "
            f"{predicciones_invariancia}"
        )

    # Guardar los resultados para analizarlos posteriormente.
    ruta_resultados = (
        BASE_DIR / "resultados_pruebas_avanzadas.csv"
    )

    casos.to_csv(
        ruta_resultados,
        index=False,
        encoding="utf-8-sig",
    )

    print(f"\nResultados guardados en: {ruta_resultados}")


# ============================================================
# 5. PUNTO DE ENTRADA
# ============================================================

if __name__ == "__main__":
    probar_predicciones_avanzadas()
