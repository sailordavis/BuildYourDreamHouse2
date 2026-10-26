<?php

namespace App\Modules\Catalog\Services;

use Illuminate\Support\Facades\DB;
use Illuminate\Support\Str;

class CatalogService
{
    /*
    |--------------------------------------------------------------------------
    | Función principal para clasificar las pinturas
    |--------------------------------------------------------------------------
    */

    public function showProduct(array $datos)
    {
        // Obtener todas las pinturas disponibles
        $pinturas = $this->obtenerPinturas();

        // Recorrer los módulos del JSON
        foreach ($datos as &$modulo) {

            // Recorrer los submódulos
            foreach ($modulo['submodulos'] as &$submodulo) {

                // Obtener las correspondencias del submódulo
                $datosClave = $this->obtenerTablaCorrespondencias(
                    $modulo['pregunta'],
                    $submodulo['Nombre']
                );

                // Asignar las pinturas correspondientes
                $submodulo['pinturas'] = $this->agregarPinturas(
                    $pinturas,
                    $datosClave
                );
            }

            unset($submodulo);
        }

        unset($modulo);

        // Devolver el JSON modificado
        return $datos;
    }


    /*
    |--------------------------------------------------------------------------
    | Obtener las correspondencias de una pregunta y opción
    |--------------------------------------------------------------------------
    */

    private function obtenerTablaCorrespondencias(
        int $pregunta_id,
        string $opcion_value
    ) {
        return DB::table('correspondencias')
            ->select(
                'atributo_objetivo',
                'valor_relacionado',
                'peso'
            )
            ->where('pregunta_id', $pregunta_id)
            ->where('opcion_value', $opcion_value)
            ->get()
            ->map(fn ($fila) => (array) $fila)
            ->all();
    }


    /*
    |--------------------------------------------------------------------------
    | Obtener todas las pinturas disponibles
    |--------------------------------------------------------------------------
    */

    private function obtenerPinturas()
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
            ->map(fn ($fila) => (array) $fila)
            ->all();
    }


    /*
    |--------------------------------------------------------------------------
    | Ordenar las pinturas por puntuación descendente
    |--------------------------------------------------------------------------
    */

    private function ordenarPorPesoDesc(array &$pesos)
    {
        usort($pesos, function ($a, $b) {
            return $b['peso'] <=> $a['peso'];
        });
    }


    /*
    |--------------------------------------------------------------------------
    | Asignar las pinturas a su respectivo submódulo
    |--------------------------------------------------------------------------
    */

    private function agregarPinturas(
        array $pinturas,
        array $coincidencias
    ) {
        $grupo = [];

        // Recorrer todas las pinturas
        foreach ($pinturas as $fila1) {

            $peso = 0;

            // Recorrer las correspondencias
            foreach ($coincidencias as $fila2) {

                $atributo = $fila2['atributo_objetivo'];

                // Comprobar que el atributo exista en la pintura
                if (!array_key_exists($atributo, $fila1)) {
                    continue;
                }

                // Normalizar los valores
                $valor1 = $this->normalizar($fila1[$atributo]);
                $valor2 = $this->normalizar($fila2['valor_relacionado']);

                // Comparar los valores
                if ($valor2 !== '' && str_contains($valor1, $valor2)) {
                    $peso += (float) $fila2['peso'];
                }
            }

            // Agregar la pintura si obtuvo puntuación
            if ($peso > 0) {

                $grupo[] = [
                    'id' => $fila1['id'],
                    'imagen' => $fila1['imagen'],
                    'nombre' => $fila1['nombre'],
                    'color' => $fila1['color'],
                    'descripcion' => $fila1['descripcion'],
                    'precio' => $fila1['precio'],
                    'stock' => $fila1['stock'],
                    'peso' => $peso
                ];
            }
        }

        // Ordenar las pinturas
        $this->ordenarPorPesoDesc($grupo);

        return $grupo;
    }


    /*
    |--------------------------------------------------------------------------
    | Normalizar texto para realizar comparaciones
    |--------------------------------------------------------------------------
    */

    private function normalizar($texto)
    {
        if ($texto === null) {
            return '';
        }

        return Str::ascii(Str::lower((string) $texto));
    }
}