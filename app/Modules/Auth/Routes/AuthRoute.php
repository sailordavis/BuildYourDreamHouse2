
<?php

use Illuminate\Support\Facades\Route;
use App\Modules\Auth\Controllers\AuthController;

Route::prefix('auth')->group(function () {

    // Rutas públicas
    Route::post('/register', [AuthController::class, 'register']);

    Route::post('/login', [AuthController::class, 'login']);

    // Rutas protegidas con Sanctum
    Route::middleware(['auth:sanctum'])->group(function () {

        Route::get('/me', [AuthController::class, 'me']);

        Route::post('/logout', [AuthController::class, 'logout']);

    });

});

