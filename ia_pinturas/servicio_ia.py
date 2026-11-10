
from fastapi import FastAPI
from pydantic import BaseModel, Field
from predecir_pintura import predecir_pintura

app = FastAPI(title="API de Recomendación de Pinturas")

class DatosPintura(BaseModel):
    es_exterior: int = Field(ge=0, le=1)
    superficie_es_interior: int = Field(ge=0, le=1)
    superficie_coincidencia: int = Field(ge=-1, le=1)
    eficiencia_coincidencia: int = Field(ge=0, le=1)

@app.get("/")
def inicio():
    return {"mensaje": "Servicio de IA de pinturas activo"}

@app.post("/predecir")
def predecir(datos: DatosPintura):
    resultado = predecir_pintura(
        es_exterior=datos.es_exterior,
        superficie_es_interior=datos.superficie_es_interior,
        superficie_coincidencia=datos.superficie_coincidencia,
        eficiencia_coincidencia=datos.eficiencia_coincidencia,
    )

    return resultado