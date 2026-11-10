
from pathlib import Path
import joblib
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent
RUTA_MODELO = BASE_DIR / "modelo" / "modelo_pinturas.joblib"

VARIABLES_ENTRADA = [
    "es_exterior",
    "superficie_es_interior",
    "superficie_coincidencia",
    "eficiencia_coincidencia",
]


def predecir_pintura(
    es_exterior,
    superficie_es_interior,
    superficie_coincidencia,
    eficiencia_coincidencia,
):
    # Validar los valores recibidos.
    if es_exterior not in (0, 1):
        raise ValueError("es_exterior debe ser 0 o 1.")

    if superficie_es_interior not in (0, 1):
        raise ValueError(
            "superficie_es_interior debe ser 0 o 1."
        )

    if superficie_coincidencia not in (-1, 0, 1):
        raise ValueError(
            "superficie_coincidencia debe ser -1, 0 o 1."
        )

    if eficiencia_coincidencia not in (0, 1):
        raise ValueError(
            "eficiencia_coincidencia debe ser 0 o 1."
        )

    # Construir las variables en el mismo orden del entrenamiento.
    datos = pd.DataFrame(
        [[
            es_exterior,
            superficie_es_interior,
            superficie_coincidencia,
            eficiencia_coincidencia,
        ]],
        columns=VARIABLES_ENTRADA,
    )

    # Cargar el modelo entrenado.
    modelo = joblib.load(RUTA_MODELO)

    # Obtener la clasificación.
    prediccion = int(modelo.predict(datos)[0])

    return {
        "es_recomendable": prediccion,
        "mensaje": (
            "Pintura recomendable"
            if prediccion == 1
            else "Pintura no recomendable"
        ),
    }



if __name__ == "__main__":
    casos_prueba = [
        {
            "nombre": "Interior apto y eficiente",
            "datos": (0, 1, -1, 1),
            "esperado": 1,
        },
        {
            "nombre": "Interior con eficiencia insuficiente",
            "datos": (0, 1, -1, 0),
            "esperado": 0,
        },
        {
            "nombre": "Exterior con pintura de interior",
            "datos": (1, 1, 1, 1),
            "esperado": 0,
        },
        {
            "nombre": "Exterior apto, superficie coincidente y eficiente",
            "datos": (1, 0, 1, 1),
            "esperado": 1,
        },
        {
            "nombre": "Exterior con superficie no coincidente",
            "datos": (1, 0, 0, 1),
            "esperado": 0,
        },
    ]

    for caso in casos_prueba:
        resultado = predecir_pintura(*caso["datos"])

        estado = (
            "CORRECTO"
            if resultado["es_recomendable"] == caso["esperado"]
            else "REVISAR"
        )

        print(f"\nCaso: {caso['nombre']}")
        print(f"Resultado: {resultado['mensaje']}")
        print(f"Esperado: {caso['esperado']}")
        print(f"Validación: {estado}")

