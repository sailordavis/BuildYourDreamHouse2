<?php

namespace App\Modules\Test\Controllers;

use App\Http\Controllers\Controller;
use Illuminate\Http\Request;
use App\Modules\Test\Services\TestService;

class TestController extends Controller
{
    protected TestService $testService;

    public function __construct(TestService $testService)
    {
        $this->testService = $testService;
    }

    public function procesarRespuestas(Request $request)
    {
        // Validar la estructura de las respuestas recibidas
        $datosValidados = $request->validate([
            'datos' => 'required|array|min:1',
            'datos.*.id' => 'required|integer',
            'datos.*.opcion' => 'required|string',
        ]);

        // Delegar el procesamiento al servicio
        $coincidencias = $this->testService->procesarRespuestas(
            $datosValidados['datos']
        );

        // Devolver las coincidencias en formato JSON
        return response()->json($coincidencias, 200);
    }

}