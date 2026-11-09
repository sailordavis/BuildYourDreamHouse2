
from pathlib import Path
import joblib

from sklearn.tree import DecisionTreeClassifier

from preparar_datos import preparar_datos


# Rutas del proyecto
BASE_DIR = Path(__file__).resolve().parent
CARPETA_MODELO = BASE_DIR / "modelo"
RUTA_MODELO = CARPETA_MODELO / "modelo_pinturas.joblib"


def entrenar_modelo():
    # 1. Cargar y preparar los datos
    X, y, identificadores = preparar_datos()

    # 2. Crear el árbol de decisiones
    modelo = DecisionTreeClassifier(
        max_depth=4,
        random_state=42
    )

    # 3. Entrenar el modelo
    modelo.fit(X, y)

    # 4. Guardar el modelo entrenado
    CARPETA_MODELO.mkdir(parents=True, exist_ok=True)
    joblib.dump(modelo, RUTA_MODELO)

    print("\nEntrenamiento completado.")
    print(f"Ejemplos utilizados: {len(X)}")
    print(f"Modelo guardado en: {RUTA_MODELO}")

    return modelo


if __name__ == "__main__":
    entrenar_modelo()
