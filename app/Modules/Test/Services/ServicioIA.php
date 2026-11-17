
<?php

namespace App\Modules\Test\Services;

use Illuminate\Support\Facades\Http;

class ServicioIA
{
    private string $url = 'http://127.0.0.1:8001';

    public function predecirPintura(array $datos): array
    {
        $respuesta = Http::acceptJson()
            ->timeout(10)
            ->post($this->url . '/predecir', [
                'es_exterior' => $datos['es_exterior'],
                'superficie_es_interior' => $datos['superficie_es_interior'],
                'superficie_coincidencia' => $datos['superficie_coincidencia'],
                'eficiencia_coincidencia' => $datos['eficiencia_coincidencia'],
            ]);

        if ($respuesta->failed()) {
            throw new \RuntimeException(
                'La API de IA respondió con HTTP '
                . $respuesta->status()
                . ': '
                . $respuesta->body()
            );
        }

        $resultado = $respuesta->json();

        if (
            !is_array($resultado)
            || !isset($resultado['es_recomendable'])
            || !in_array($resultado['es_recomendable'], [0, 1], true)
        ) {
            throw new \RuntimeException(
                'La API de IA devolvió una predicción inválida.'
            );
        }

        return $resultado;
    }
}