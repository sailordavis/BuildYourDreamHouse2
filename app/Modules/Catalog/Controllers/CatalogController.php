<?php

namespace App\Modules\Catalog\Controllers;

use App\Http\Controllers\Controller;
use Illuminate\Http\Request;
use App\Modules\Catalog\Services\CatalogService;

class CatalogController extends Controller
{
    protected CatalogService $catalogService;

    public function __construct(CatalogService $catalogService)
    {
        $this->catalogService = $catalogService;
    }

    // Función para mostrar las pinturas clasificadas
    public function showProduct(Request $request)
    {
        // Validar la estructura del JSON recibido
        $datos = $request->validate([
            '*.pregunta' => 'required|integer',
            '*.clasificacion' => 'required|string',
            '*.submodulos' => 'required|array',
            '*.submodulos.*.Nombre' => 'required|string',
            '*.submodulos.*.pinturas' => 'present|array'
        ]);

        // Delegar la clasificación al Service
        $resultado = $this->catalogService->showProduct($datos);

        // Devolver la respuesta JSON
        return response()->json($resultado, 200);
    }
}