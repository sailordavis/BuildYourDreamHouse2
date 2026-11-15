<?php

namespace App\Modules\Test\Services;

use Illuminate\Support\Facades\DB;
use Illuminate\Support\Str;
use App\Models\Resultado;
use App\Models\Respuesta;
use Illuminate\Support\Facades\Auth;

class TestService
{
    
    /**
     * Procesa las respuestas del test.
     *
     * Obtiene las correspondencias asociadas a cada respuesta
     * y consulta las pinturas registradas en la base de datos.
     */
    public function procesarRespuestas(array $respuestas): array
{
    return DB::transaction(function () use ($respuestas) {

        // 1. Crear el resultado asociado al usuario autenticado
        $resultado = Resultado::create([
            'usuario_id' => Auth::id(),
        ]);

        $datosClave = [];

        // 2. Guardar cada respuesta y obtener sus correspondencias
        foreach ($respuestas as $respuesta) {

            // Registrar la respuesta asociada al resultado creado
            Respuesta::create([
                'resultado_id' => $resultado->id,
                'num_pregunta' => $respuesta['id'],
                'opcion_value' => $respuesta['opcion'],
            ]);

            // Consultar las correspondencias de la respuesta
            $correspondencias = $this->obtenerTablaCorrespondencias(
                $respuesta['id'],
                $respuesta['opcion']
            );

            // Acumular las correspondencias encontradas
            $datosClave = array_merge(
                $datosClave,
                $correspondencias
            );
        }

        // 3. Obtener las pinturas disponibles
        $pinturas = $this->obtenerPinturas();

        

        //4. Crear el vector donde almacenara las coincidencias idenficadas
        //junto a otros parametros que formaran parte de  las variables de entrada que 
        //recibira el modelo 
        $datosEntrada = $this->prepararDatosEntrada($resultado->id,$datosClave,$pinturas);

        return $datosEntrada;
    });
}

    /**
     * Obtiene las correspondencias asociadas a una pregunta y opción.
     */
    private function obtenerTablaCorrespondencias(
        int $preguntaId,
        string $opcionValue
    ): array {
        return DB::table('correspondencias')
            ->select(
                'atributo_objetivo',
                'valor_relacionado',
                'peso'
            )
            ->where('pregunta_id', $preguntaId)
            ->where('opcion_value', $opcionValue)
            ->get()
            ->map(fn ($fila) => (array) $fila)
            ->all();
    }

    /**
     * Obtiene las pinturas registradas en la base de datos.
     */
    private function obtenerPinturas(): array
    {
        return DB::table('pinturas')
            ->select(
                'id',
                'superficie',
                'eficiencia',
            )
            ->get()
            ->map(fn ($pintura) => (array) $pintura)
            ->all();
    }

    

public function prepararDatosEntrada(
    int $resultadoId,
    array $datosClave,
    array $pinturas
): array {

    // 1. Obtener la respuesta de la pregunta 1
    $respuestaUbicacion = Respuesta::where(
        'resultado_id',
        $resultadoId
    )
        ->where('num_pregunta', 1)
        ->value('opcion_value');

    // 2. Determinar si el usuario eligió Exterior
    $esExterior = strtolower(trim($respuestaUbicacion ?? '')) === 'exterior'
        ? 1
        : 0;

    $datosEntrada = [];

    // 3. Construir un vector por cada pintura
    foreach ($pinturas as $pintura) {

        // Determinar si la superficie de la pintura es interior
        $esInterior = strtolower(trim(
            $pintura['superficie'] ?? ''
        )) === 'interior' ? 1 : 0;

        // Identificar las coincidencias de esta pintura
        $coincidenciasClave = $this->identificarCoincidencias(
            $datosClave,
            $pintura
        );

        // 4. Crear el vector de entrada para el modelo
        $datosEntrada[] = [
            // Identificadores
            'resultado_id' => $resultadoId,
            'pintura_id' => $pintura['id'],

            // Variables de entrada del modelo
            'es_exterior' => $esExterior,
            'superficie_es_interior' => $esInterior,

            'superficie_coincidencia' => $esExterior === 0
                ? -1
                : $coincidenciasClave['superficie_coincidencia'],

            'eficiencia_coincidencia' =>
                $coincidenciasClave['eficiencia_coincidencia'],
        ];
    }

    return $datosEntrada;
}





public function identificarCoincidencias(
    array $datosClave,
    array $pintura
): array {

    $superficieCoincidencia = 0;
    $eficienciaCoincidencia = 0;

    foreach ($datosClave as $fila2) {

        $atributo = strtolower(trim(
            $fila2['atributo_objetivo'] ?? ''
        ));

        $valorRelacionado = strtolower(trim(
            $fila2['valor_relacionado'] ?? ''
        ));

        // Comparar la superficie de la pintura
        if ($atributo === 'superficie') {

            $valorPintura = strtolower(trim(
                $pintura['superficie'] ?? ''
            ));

            if (
                $valorRelacionado !== '' &&
                $valorPintura !== '' &&
                strpos($valorPintura, $valorRelacionado) !== false
            ) {
                $superficieCoincidencia = 1;
            }
        }

        // Comparar la eficiencia de la pintura
        if ($atributo === 'eficiencia') {

            $valorPintura = strtolower(trim(
                $pintura['eficiencia'] ?? ''
            ));

            if (
                $valorRelacionado !== '' &&
                $valorPintura !== '' &&
                strpos($valorPintura, $valorRelacionado) !== false
            ) {
                $eficienciaCoincidencia = 1;
            }
        }
    }

    return [
        'superficie_coincidencia' => $superficieCoincidencia,
        'eficiencia_coincidencia' => $eficienciaCoincidencia,
    ];
}


}
   
