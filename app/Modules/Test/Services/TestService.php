<?php

namespace App\Modules\Test\Services;

use Illuminate\Support\Facades\DB;
use Illuminate\Support\Str;

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
        $datosClave = [];

        // Primer paso: obtener las correspondencias
        foreach ($respuestas as $respuesta) {

            $resultado = $this->obtenerTablaCorrespondencias(
                $respuesta['id'],
                $respuesta['opcion']
            );

            // Acumular las correspondencias encontradas
            $datosClave = array_merge(
                $datosClave,
                $resultado
            );
        }

        // Segundo paso: obtener las pinturas
        $pinturas = $this->obtenerPinturas();

        // Por ahora no se generan recomendaciones.
        // Se devuelven los datos para comprobar el funcionamiento.
        return [
            'datos_clave' => $datosClave,
            'pinturas' => $pinturas,
        ];
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
                'acabado',
                'eficiencia',
                'gama_color',
                'estilo_decorativo',
                'imagen',
                'nombre',
                'color',
                'descripcion',
                'precio',
                'stock'
            )
            ->get()
            ->map(fn ($pintura) => (array) $pintura)
            ->all();
    }
}